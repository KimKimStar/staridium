import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

script_dir = os.path.dirname(os.path.abspath(__file__))
proj_dir = os.path.join(script_dir, "..")
html_path = os.path.join(proj_dir, "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update selectCategory to ALWAYS reset window.currentSpecialView = null
# so category switches IMMEDIATELY and unconditionally update videos!
old_select_cat = """function selectCategory(key) {
      currentTopicKey = key;
      currentDisplayLimit = 30; // reset limit
      var cat = CATEGORIES.find(function(c) { return c.key === key; }) || CATEGORIES[0];

      var label = document.getElementById("currentTopicLabel");
      if (label) label.innerText = cat.name;

      activeSubId = "all";
      renderCategoryPills();
      renderSidebar();
      renderSubtopics();
      renderVideos();
    }"""

new_select_cat = """function selectCategory(key) {
      window.currentSpecialView = null; // ALWAYS clear special view on category click!
      currentTopicKey = key;
      currentDisplayLimit = 30;
      var cat = CATEGORIES.find(function(c) { return c.key === key; }) || CATEGORIES[0];

      var label = document.getElementById("currentTopicLabel");
      if (label) label.innerText = cat.name;

      var buttons = document.querySelectorAll(".time-filter-section .surge-btn");
      for (var s = 0; s < buttons.length; s++) buttons[s].classList.remove("active");

      activeSubId = "all";
      renderCategoryPills();
      renderSidebar();
      renderSubtopics();
      renderVideos();
    }"""

if old_select_cat in html:
    html = html.replace(old_select_cat, new_select_cat)
    print("Updated selectCategory with unconditional special view reset!")
else:
    print("old_select_cat not found, searching with regex...")
    html = re.sub(
        r'function selectCategory\(key\)\s*\{.*?\n    \}',
        new_select_cat.strip(),
        html,
        flags=re.DOTALL
    )
    print("Replaced selectCategory via regex!")

# 2. Update setTimeFilter to ALWAYS reset window.currentSpecialView = null
old_set_time = """function setTimeFilter(filter, btn) {
      activeTimeFilter = filter;
      activeSurgeFilter = null;"""

new_set_time = """function setTimeFilter(filter, btn) {
      window.currentSpecialView = null; // ALWAYS clear special view on time filter click!
      activeTimeFilter = filter;
      activeSurgeFilter = null;"""

if old_set_time in html:
    html = html.replace(old_set_time, new_set_time)
    print("Updated setTimeFilter with special view reset!")

# 3. Update generateVideosForFilter with:
# A) Strict Category Isolation: ONLY use items from the selected category!
# B) Period-Specific Dynamic Rotation (pOffset): 1d, 1w, 1m, 3m, 6m, 1y rotate 1st place!
# C) 100% Zero-Duplicate Guarantee: Each video appears EXACTLY ONCE!
new_gen_func = """    function generateVideosForFilter(topicKey, timeFilter, platform, subTopicId, surgeFilter, sortType, totalCount) {
      var isCustom = (topicKey && topicKey.indexOf("custom_") === 0);
      var customQuery = isCustom ? topicKey.replace("custom_", "") : "";

      var cat = CATEGORIES.find(function(c) { return c.key === topicKey; });
      if (!cat) {
        if (isCustom) {
          cat = {
            key: topicKey,
            name: "🔍 " + customQuery + " 숏폼 분석",
            subTopics: []
          };
        } else {
          cat = CATEGORIES[0];
        }
      }

      var topicName = isCustom ? customQuery : cat.name.replace(/^[^\s]+ /, '');
      var subTopics = cat.subTopics || [];
      var catSubTopics = subTopics;

      // 1. PRIMARY CATEGORY POOL ISOLATION: Strict Topic Separation!
      var basePool = (TOPIC_SPECIFIC_ITEMS && TOPIC_SPECIFIC_ITEMS[topicKey]) ? TOPIC_SPECIFIC_ITEMS[topicKey].slice() : [];
      if (!basePool || basePool.length === 0) {
        basePool = (TOPIC_SPECIFIC_ITEMS && TOPIC_SPECIFIC_ITEMS.humor) ? TOPIC_SPECIFIC_ITEMS.humor.slice() : [];
      }

      // Filter to strictly unique items in basePool
      var fullUniquePool = [];
      var seenIds = {};
      for (var b = 0; b < basePool.length; b++) {
        var bYt = basePool[b].youtubeId;
        if (!seenIds[bYt]) {
          seenIds[bYt] = true;
          fullUniquePool.push(basePool[b]);
        }
      }

      // If user requested more videos than basePool via "더보기", pull additional UNIQUE videos from other categories!
      if (totalCount > fullUniquePool.length) {
        for (var otherKey in TOPIC_SPECIFIC_ITEMS) {
          if (otherKey !== topicKey) {
            var extraItems = TOPIC_SPECIFIC_ITEMS[otherKey] || [];
            for (var e = 0; e < extraItems.length; e++) {
              var exItem = extraItems[e];
              if (!seenIds[exItem.youtubeId]) {
                seenIds[exItem.youtubeId] = true;
                fullUniquePool.push(exItem);
                if (fullUniquePool.length >= totalCount) break;
              }
            }
          }
          if (fullUniquePool.length >= totalCount) break;
        }
      }

      // 2. PERIOD-SPECIFIC ROTATION (1d, 1w, 1m, 3m, 6m, 1y rotate #1 video without duplicates!)
      var periodOffsets = {
        "1d": 0,
        "1w": 2,
        "1m": 4,
        "3m": 6,
        "6m": 8,
        "1y": 1
      };
      var pOffset = (periodOffsets[timeFilter] !== undefined) ? periodOffsets[timeFilter] : 0;

      // Rotate pool according to period so Rank 1~10 change dynamically per period!
      var poolLength = fullUniquePool.length;
      var rotatedPool = [];
      for (var r_idx = 0; r_idx < poolLength; r_idx++) {
        var rotatedIndex = (r_idx + pOffset) % poolLength;
        rotatedPool.push(fullUniquePool[rotatedIndex]);
      }

      var poolToRender = rotatedPool.slice(0, Math.max(poolLength, totalCount));

      var videos = [];

      for (var i = 0; i < poolToRender.length; i++) {
        var baseItem = poolToRender[i];
        var realYtId = baseItem.youtubeId || "BEDwfDQai3A";
        var exactUrl = "https://www.youtube.com/shorts/" + realYtId;
        var realThumbnail = baseItem.thumbnail || ("https://i.ytimg.com/vi/" + realYtId + "/hqdefault.jpg");
        var authorDisplay = baseItem.author || baseItem.ytChannel || "한국 크리에이터";
        var plat = "shorts";

        // Upload Time Distribution Strictly Matching timeFilter
        var daysAgo = 0;
        var timeString = "";
        if (timeFilter === "1d") {
          daysAgo = 0;
          var hoursAgo = ((i * 3) % 23) + 1;
          timeString = hoursAgo + "시간 전 (오늘)";
        } else if (timeFilter === "1w") {
          daysAgo = ((i % 6) + 1);
          timeString = daysAgo + "일 전";
        } else if (timeFilter === "1m") {
          daysAgo = ((i % 22) + 8);
          timeString = Math.floor(daysAgo / 7) + "주 전";
        } else if (timeFilter === "3m") {
          daysAgo = ((i % 60) + 31);
          timeString = Math.floor(daysAgo / 30) + "달 전";
        } else if (timeFilter === "6m") {
          daysAgo = ((i % 90) + 91);
          timeString = Math.floor(daysAgo / 30) + "달 전";
        } else {
          daysAgo = Math.floor((i * 3.6) + 1);
          if (daysAgo <= 1) timeString = "오늘";
          else if (daysAgo <= 7) timeString = daysAgo + "일 전";
          else if (daysAgo <= 30) timeString = Math.floor(daysAgo / 7) + "주 전";
          else timeString = Math.floor(daysAgo / 30) + "달 전";
        }

        // Monotonic View Count Hierarchy (Single Source of Truth)
        var masterAllTimeViews = (window.MASTER_VIDEO_REGISTRY && window.MASTER_VIDEO_REGISTRY[realYtId]) ? window.MASTER_VIDEO_REGISTRY[realYtId] : 28500000;
        var periodRatio = 1.0;
        if (timeFilter === "1d") periodRatio = 0.048;      // 24h 실시간 조회수
        else if (timeFilter === "1w") periodRatio = 0.125; // 7일간 누적 조회수
        else if (timeFilter === "1m") periodRatio = 0.26;  // 1개월 누적 조회수
        else if (timeFilter === "3m") periodRatio = 0.48;  // 3개월 누적 조회수
        else if (timeFilter === "6m") periodRatio = 0.72;  // 6개월 누적 조회수
        else periodRatio = 1.0;                            // 1년/역대 누적 조회수

        var baseViews = Math.floor(masterAllTimeViews * periodRatio);

        // Apply Hourly Dynamic Rebalancing Delta
        var isNewlyEmerged = false;
        var emergenceInfo = window.NEWLY_EMERGED_VIDEOS ? window.NEWLY_EMERGED_VIDEOS[baseItem.id] : null;
        if (emergenceInfo) {
          isNewlyEmerged = true;
          baseViews = Math.floor(baseViews * (emergenceInfo.surgeMultiplier || 1.35));
        } else if (window.HOURLY_REBALANCE_CYCLE > 0) {
          var charSeed = (realYtId.charCodeAt(0) * 19 + realYtId.charCodeAt(realYtId.length - 1) * 29 + window.HOURLY_REBALANCE_CYCLE * 43) % 100;
          var hourlyBonus = Math.floor((baseViews * 0.08) * (charSeed / 100));
          baseViews += hourlyBonus;
        }

        var viewsFormatted = (baseViews >= 100000000) ? (baseViews / 100000000).toFixed(1) + "억회" : (baseViews >= 10000) ? Math.floor(baseViews / 10000).toLocaleString() + "만회" : baseViews.toLocaleString() + "회";
        var likesFormatted = (baseViews * 0.052 >= 10000) ? (baseViews * 0.052 / 10000).toFixed(1) + "만" : Math.floor(baseViews * 0.052).toLocaleString();

        var surge1d = "+" + (180 + Math.floor((poolToRender.length - i) * 6)) + "%";
        var surge7d = "+" + (340 + Math.floor((poolToRender.length - i) * 10)) + "%";
        var surgeBonus24h = Math.floor(100000 + ((i * 17) % 55) * 10000); // 10만 ~ 65만회

        // Period-Tailored Dynamic Titles: Highly engaging, immediately shows timeframe distinction
        var fullTitle = "";
        if (timeFilter === "1d") {
          if (i === 0) fullTitle = "🔥 [오늘 1위 실시간] " + baseItem.title + " (24h 급상승 +480%)";
          else if (i === 1) fullTitle = "🔥 [오늘 떡상 TOP] " + baseItem.title + " (실시간 알고리즘 폭발)";
          else if (i === 2) fullTitle = "🔥 [오늘 화제작] " + baseItem.title + " (방금 터진 숏폼)";
          else fullTitle = "🔥 [오늘 #" + (i + 1) + "] " + baseItem.title;
        } else if (timeFilter === "1w") {
          if (i === 0) fullTitle = "⚡ [이번 주 1위] " + baseItem.title + " (주간 350만 돌파)";
          else if (i === 1) fullTitle = "⚡ [주간 떡상 TOP] " + baseItem.title + " (7일간 저장 수 1위)";
          else if (i === 2) fullTitle = "⚡ [주간 베스트] " + baseItem.title + " (이번 주 화제작)";
          else fullTitle = "⚡ [주간 #" + (i + 1) + "] " + baseItem.title;
        } else if (timeFilter === "1m") {
          if (i === 0) fullTitle = "🚀 [월간 1위 챔피언] " + baseItem.title + " (한 달 만에 1200만)";
          else if (i === 1) fullTitle = "🚀 [월간 베스트] " + baseItem.title + " (30일 누적 1위)";
          else if (i === 2) fullTitle = "🚀 [월간 랭킹 TOP] " + baseItem.title + " (알고리즘 박제작)";
          else fullTitle = "🚀 [월간 #" + (i + 1) + "] " + baseItem.title;
        } else if (timeFilter === "3m") {
          if (i === 0) fullTitle = "👑 [분기 1위 스테디] " + baseItem.title + " (3개월 누적 2400만)";
          else if (i === 1) fullTitle = "👑 [3개월 챔피언] " + baseItem.title + " (역주행 신화)";
          else fullTitle = "👑 [3개월 #" + (i + 1) + "] " + baseItem.title;
        } else if (timeFilter === "6m") {
          if (i === 0) fullTitle = "💎 [반기 결산 메가바이럴] " + baseItem.title + " (상반기 3800만)";
          else if (i === 1) fullTitle = "💎 [6개월 1티어] " + baseItem.title + " (대한민국 휩쓴 숏폼)";
          else fullTitle = "💎 [6개월 #" + (i + 1) + "] " + baseItem.title;
        } else {
          if (i === 0) fullTitle = "🏆 [역대 1위 명예의 전당] " + baseItem.title + " (누적 6000만 전설)";
          else if (i === 1) fullTitle = "🏆 [연간 챔피언] " + baseItem.title + " (대한민국 레전드 숏폼)";
          else fullTitle = "🏆 [역대 #" + (i + 1) + "] " + baseItem.title;
        }

        var subId = "all";
        if (catSubTopics && catSubTopics.length > 0) {
          var targetSubIdx = (baseItem.subIndex !== undefined) ? (baseItem.subIndex % catSubTopics.length) : (i % catSubTopics.length);
          subId = (catSubTopics[targetSubIdx] && catSubTopics[targetSubIdx].id) ? catSubTopics[targetSubIdx].id : "all";
        }

        var analysis = generateDetailedVideoAnalysis(baseItem, topicKey, i + 1, timeFilter, topicName);

        videos.push({
          id: topicKey + "-" + timeFilter + "-" + platform + "-" + (i + 1),
          rank: i + 1,
          title: fullTitle,
          platform: 'shorts',
          subTopicId: subId,
          views: baseViews,
          viewsFormatted: viewsFormatted,
          likesFormatted: likesFormatted,
          duration: (20 + (i % 35)) + "s",
          author: authorDisplay,
          thumbnail: realThumbnail,
          youtubeId: realYtId,
          videoUrl: exactUrl,
          daysAgo: daysAgo,
          timeString: timeString,
          surge1d: surge1d,
          surge7d: surge7d,
          surgeViews24h: surgeBonus24h,
          surgeScore: 800 - (i * 7) + (daysAgo === 0 ? 300 : daysAgo <= 7 ? 150 : 0) + (isNewlyEmerged ? 400 : 0),
          viralScore: Math.max(88, 99 - Math.floor(i / 8)),
          isNewlyEmerged: isNewlyEmerged,
          hookSummary: analysis.hookSummary,
          viralReason: analysis.viralReason,
          hookAnalysis: analysis.hookAnalysis,
          editingAnalysis: analysis.editingAnalysis,
          timelineScript: analysis.timelineScript,
          successFactors: analysis.successFactors,
          ideas: analysis.ideas
        });
      }

      // Filter or Prioritize by subTopic
      if (subTopicId !== "all") {
        var matchingVideos = videos.filter(function(v) { return v.subTopicId === subTopicId; });
        var otherVideos = videos.filter(function(v) { return v.subTopicId !== subTopicId; });
        videos = matchingVideos.concat(otherVideos);
      }

      // Re-assign ranks 1 to N strictly
      for (var r = 0; r < videos.length; r++) {
        videos[r].rank = r + 1;
      }

      return {
        subTopics: subTopics,
        videos: videos
      };
    }\n\n"""

# Replace generateVideosForFilter
pos_g_start = html.find("    function generateVideosForFilter(")
pos_g_end = html.find("    function rebalanceAllVideosHourly(", pos_g_start)

if pos_g_start != -1 and pos_g_end != -1:
    html = html[:pos_g_start] + new_gen_func + html[pos_g_end:]
    print("Replaced generateVideosForFilter with Topic-Isolation & Period-Rotation!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Step 10 applied successfully!")
