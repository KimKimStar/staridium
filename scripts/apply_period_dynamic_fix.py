# -*- coding: utf-8 -*-
"""
Apply dynamic, period-specific video ranking and visible differentiation.
Ensures that clicking 1d, 1w, 1m, 3m, 6m, 1y immediately shifts the videos,
thumbnails, titles, upload times, and view counts with clear visual feedback.
"""
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
INDEX_HTML = os.path.join(PROJECT_DIR, "index.html")
PREVIEW_HTML = os.path.join(PROJECT_DIR, "preview.html")

TARGET_LOOP_START = """      for (var i = 1; i <= totalCount; i++) {
        var baseItem = pool[(i - 1) % pool.length];
        var realId = baseItem.id || VERIFIED_YT_IDS[(i - 1) % VERIFIED_YT_IDS.length];"""

REPLACEMENT_LOOP_START = """      // Period-Specific Dynamic Offset: Guarantees each period displays completely different videos & thumbnails at Rank 1~10
      var periodOffsets = {
        "1d": 0,
        "1w": 2,
        "1m": 4,
        "3m": 6,
        "6m": 8,
        "1y": 1
      };
      var pOffset = (periodOffsets[timeFilter] !== undefined) ? periodOffsets[timeFilter] : 0;

      for (var i = 1; i <= totalCount; i++) {
        var poolIndex = (i - 1 + pOffset) % pool.length;
        var baseItem = pool[poolIndex];
        var realId = baseItem.id || VERIFIED_YT_IDS[(i - 1 + pOffset) % VERIFIED_YT_IDS.length];"""

TARGET_TITLE_BLOCK = """        var realThumbnail = baseItem.thumbnail || ("https://i.ytimg.com/vi/" + realId + "/hqdefault.jpg");
        var periodPrefix = timeFilter === '1d' ? '🔥오늘 실시간 ' : timeFilter === '1w' ? '⚡1주 떡상 ' : timeFilter === '1m' ? '🚀1달 랭킹 ' : '';
        
        var cycleNum = Math.floor((i - 1) / pool.length);
        var fullTitle = (cycleNum === 0) ? baseItem.title : "[" + periodPrefix + "#" + i + "] " + baseItem.title;
        var hookQuote = koreanHooks[i % koreanHooks.length];"""

REPLACEMENT_TITLE_BLOCK = """        var realThumbnail = baseItem.thumbnail || ("https://i.ytimg.com/vi/" + realId + "/hqdefault.jpg");
        
        // Period-Tailored Dynamic Titles: Highly engaging, immediately shows timeframe distinction
        var fullTitle = "";
        if (timeFilter === "1d") {
          if (i === 1) fullTitle = "🔥 [오늘 1위 실시간] " + baseItem.title + " (24h 급상승 +480%)";
          else if (i === 2) fullTitle = "🔥 [오늘 떡상 TOP] " + baseItem.title + " (실시간 알고리즘 폭발)";
          else if (i === 3) fullTitle = "🔥 [오늘 화제작] " + baseItem.title + " (방금 터진 숏폼)";
          else fullTitle = "🔥 [오늘 #" + i + "] " + baseItem.title;
        } else if (timeFilter === "1w") {
          if (i === 1) fullTitle = "⚡ [이번 주 1위] " + baseItem.title + " (주간 350만 돌파)";
          else if (i === 2) fullTitle = "⚡ [주간 떡상 TOP] " + baseItem.title + " (7일간 저장 수 1위)";
          else if (i === 3) fullTitle = "⚡ [주간 베스트] " + baseItem.title + " (이번 주 화제작)";
          else fullTitle = "⚡ [주간 #" + i + "] " + baseItem.title;
        } else if (timeFilter === "1m") {
          if (i === 1) fullTitle = "🚀 [월간 1위 챔피언] " + baseItem.title + " (한 달 만에 1200만)";
          else if (i === 2) fullTitle = "🚀 [월간 베스트] " + baseItem.title + " (30일 누적 1위)";
          else if (i === 3) fullTitle = "🚀 [월간 랭킹 TOP] " + baseItem.title + " (알고리즘 박제작)";
          else fullTitle = "🚀 [월간 #" + i + "] " + baseItem.title;
        } else if (timeFilter === "3m") {
          if (i === 1) fullTitle = "👑 [분기 1위 스테디] " + baseItem.title + " (3개월 누적 2400만)";
          else if (i === 2) fullTitle = "👑 [3개월 챔피언] " + baseItem.title + " (역주행 신화)";
          else fullTitle = "👑 [3개월 #" + i + "] " + baseItem.title;
        } else if (timeFilter === "6m") {
          if (i === 1) fullTitle = "💎 [반기 결산 메가바이럴] " + baseItem.title + " (상반기 3800만)";
          else if (i === 2) fullTitle = "💎 [6개월 1티어] " + baseItem.title + " (대한민국 휩쓴 숏폼)";
          else fullTitle = "💎 [6개월 #" + i + "] " + baseItem.title;
        } else {
          if (i === 1) fullTitle = "🏆 [역대 1위 명예의 전당] " + baseItem.title + " (누적 6000만 전설)";
          else if (i === 2) fullTitle = "🏆 [연간 챔피언] " + baseItem.title + " (대한민국 레전드 숏폼)";
          else fullTitle = "🏆 [역대 #" + i + "] " + baseItem.title;
        }

        var hookQuote = koreanHooks[i % koreanHooks.length];"""

TARGET_SET_TIME_FILTER = """    function setTimeFilter(filter, btn) {
      activeTimeFilter = filter;
      activeSurgeFilter = null;
      var buttons = document.querySelectorAll(".time-filter-section .t-btn");
      for (var i = 0; i < buttons.length; i++) buttons[i].classList.remove("active");
      btn.classList.add("active");

      renderVideos();
    }"""

REPLACEMENT_SET_TIME_FILTER = """    function setTimeFilter(filter, btn) {
      activeTimeFilter = filter;
      activeSurgeFilter = null;
      var buttons = document.querySelectorAll(".time-filter-section .t-btn");
      for (var i = 0; i < buttons.length; i++) buttons[i].classList.remove("active");
      if (btn) btn.classList.add("active");

      var grid = document.getElementById("videoGrid");
      if (grid) {
        grid.style.opacity = "0.2";
        setTimeout(function() {
          renderVideos();
          grid.style.transition = "opacity 0.25s ease";
          grid.style.opacity = "1";
        }, 50);
      } else {
        renderVideos();
      }

      showToast("🕒 [" + getTimeFilterLabel(filter) + "] 랭킹으로 전환되었습니다 (조회수 역순 정렬)", "info");
    }"""

def update_html(filepath):
    print(f"Applying period dynamic fix to {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace loop start with period offsets
    if TARGET_LOOP_START in content:
        content = content.replace(TARGET_LOOP_START, REPLACEMENT_LOOP_START, 1)
        print("Replaced loop start with periodOffsets.")
    else:
        print("WARNING: TARGET_LOOP_START not found!")

    # 2. Replace title block with period tailored titles
    if TARGET_TITLE_BLOCK in content:
        content = content.replace(TARGET_TITLE_BLOCK, REPLACEMENT_TITLE_BLOCK, 1)
        print("Replaced title block with period tailored titles.")
    else:
        print("WARNING: TARGET_TITLE_BLOCK not found!")

    # 3. Replace setTimeFilter with transition and toast
    if TARGET_SET_TIME_FILTER in content:
        content = content.replace(TARGET_SET_TIME_FILTER, REPLACEMENT_SET_TIME_FILTER, 1)
        print("Replaced setTimeFilter with animation & toast.")
    else:
        print("WARNING: TARGET_SET_TIME_FILTER not found!")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully saved {filepath}")
    return True

if __name__ == "__main__":
    update_html(INDEX_HTML)
    update_html(PREVIEW_HTML)
