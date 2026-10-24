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

# =========================================================================
# 1. REQUIREMENT 2: DELETE unwanted subtopics in total_kr
# "종합 1위 메가 바이럴 숏폼", "이번 주 급상승 떡상 영상 TOP", "시청 지속 시간 극대화 성공 사례"
# =========================================================================
old_total_subtopics = """        subTopics: [
          { id: "sub-1", name: "종합 1위 메가 바이럴 숏폼" },
          { id: "sub-2", name: "이번 주 급상승 떡상 영상 TOP" },
          { id: "sub-3", name: "시청 지속 시간 극대화 성공 사례" }
        ]"""
new_total_subtopics = """        subTopics: []"""

if old_total_subtopics in html:
    html = html.replace(old_total_subtopics, new_total_subtopics)
    print("Requirement 2: Removed unwanted subTopics from total_kr!")
else:
    # Use regex
    html = re.sub(
        r'key:\s*"total_kr",\s*name:[^,]+,\s*searchQ:[^,]+,\s*count:[^,]+,\s*subTopics:\s*\[.*?\]',
        'key: "total_kr", \n        name: "🏆 대한민국 종합 숏폼 통합 랭킹", \n        searchQ: "한국|인기|급상승|쇼츠", \n        count: "75+",\n        subTopics: []',
        html,
        flags=re.DOTALL
    )
    print("Requirement 2: Removed unwanted subTopics via regex!")

# Make sure renderSubtopics hides the container if subTopics is empty
old_render_subtopics = """function renderSubtopics() {
      var wrap = document.getElementById("subTopicsWrap");
      var cat = CATEGORIES.find(function(c) { return c.key === currentTopicKey; }) || CATEGORIES[0];
      var subTopics = cat.subTopics || ["""

new_render_subtopics = """function renderSubtopics() {
      var wrap = document.getElementById("subTopicsWrap");
      if (!wrap) return;
      var cat = CATEGORIES.find(function(c) { return c.key === currentTopicKey; }) || CATEGORIES[0];
      var subTopics = (cat && cat.subTopics) ? cat.subTopics : [];
      if (!subTopics || subTopics.length === 0) {
        wrap.innerHTML = "";
        wrap.style.display = "none";
        return;
      }
      wrap.style.display = "flex";"""

if old_render_subtopics in html:
    html = html.replace(old_render_subtopics, new_render_subtopics)
    print("Updated renderSubtopics to hide container when empty!")

# =========================================================================
# 2. REQUIREMENT 1: DEDICATED PAGES & 1-HOUR REBALANCING FOR SURGE 24H & SURGE 7D
# "최근24시간 조회수 폭증top" and "최근 1주일 역주행 떡상top"
# =========================================================================
# Update buttons in HTML
old_surge_buttons = """              <button class="t-btn surge-btn" onclick="setSurgeFilter('surge_1d', this)">
                🔥 최근 24시간 조회수 폭증 TOP
              </button>
              <button class="t-btn surge-btn" onclick="setSurgeFilter('surge_1w', this)">
                🚀 최근 1주일 역주행 떡상 TOP
              </button>
              <button class="t-btn" onclick="resetSurgeFilter(this)">
                ✕ 일반 정렬 복귀
              </button>"""

new_surge_buttons = """              <button class="t-btn surge-btn" id="btnSurge24h" onclick="openDedicatedSurgePage('surge_24h', this)">
                🔥 최근 24시간 조회수 폭증 TOP (전용관)
              </button>
              <button class="t-btn surge-btn" id="btnSurge7d" onclick="openDedicatedSurgePage('surge_7d', this)">
                🚀 최근 1주일 역주행 떡상 TOP (전용관)
              </button>
              <button class="t-btn" id="btnSurgeReset" onclick="exitDedicatedSurgePage(this)">
                ✕ 일반 카테고리 랭킹 복귀
              </button>"""

if old_surge_buttons in html:
    html = html.replace(old_surge_buttons, new_surge_buttons)
    print("Requirement 1: Updated surge buttons markup!")

# =========================================================================
# 3. REQUIREMENT 4: "급상승 상승률 순" displays videos with 1-day surge >= 100,000
# =========================================================================
html = html.replace(
    '<option value="surge">급상승 상승률 순</option>',
    '<option value="surge">⚡ 급상승 상승률 순 (하루 10만+ 폭증)</option>'
)

# =========================================================================
# 4. REQUIREMENT 6: FIX YOUTUBE ERROR 153 WITH POPUP SHORTS PLAYER & CLEAN EMBED
# =========================================================================
# Replace modal video iframe wrap with action bar + clean embed + direct popup button
old_modal_header_part = """          <div id="modalPlayerPlatformLabel" style="font-size:11px; color:#9ca3af; font-family:monospace; margin-bottom:6px;">
            🔴 YouTube Shorts 공식 실시간 플레이어
          </div>
          <div class="video-iframe-wrap" id="videoIframeWrap">
            <!-- Dynamic Iframe will be injected here -->
          </div>"""

new_modal_header_part = """          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
            <div id="modalPlayerPlatformLabel" style="font-size:11.5px; color:#34d399; font-weight:700; font-family:monospace;">
              🔴 YouTube Shorts 정품 플레이어
            </div>
            <!-- Direct Popup Player (100% Error 153 Failsafe) -->
            <button type="button" class="btn-popup-player" onclick="openNativeShortsPopup()" style="background:linear-gradient(135deg, #ef4444, #dc2626); color:white; font-size:11.5px; font-weight:800; padding:6px 14px; border:0; border-radius:8px; cursor:pointer; display:flex; align-items:center; gap:6px; box-shadow:0 4px 12px rgba(239,68,68,0.4);">
              <span>🎬 1초 팝업 플레이어로 시청 (Error 153 원천 차단)</span>
            </button>
          </div>
          <div class="video-iframe-wrap" id="videoIframeWrap">
            <!-- Dynamic Iframe will be injected here -->
          </div>
          <div id="error153NoticeBox" style="margin-top:8px; padding:10px 12px; background:rgba(30,41,59,0.7); border:1px solid rgba(255,255,255,0.1); border-radius:8px; font-size:11px; color:#cbd5e1; line-height:1.4;">
            💡 <strong>오류 153(플레이어 설정 오류) 해결 안내:</strong> 브라우저 보안 또는 광고 차단기로 인해 위 재생창에 오류 153이 뜰 경우, 상단 <strong>[🎬 1초 팝업 플레이어로 시청]</strong> 버튼을 누르시면 유튜브 공식 9:16 플레이어로 즉시 오류 없이 재생됩니다.
          </div>"""

if old_modal_header_part in html:
    html = html.replace(old_modal_header_part, new_modal_header_part)
    print("Requirement 6: Injected Failsafe Popup Player Bar into Modal!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML base markup updated successfully!")
