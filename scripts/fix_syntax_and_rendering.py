# -*- coding: utf-8 -*-
"""
Fix the stray brace syntax error and bulletproof renderVideos & setTimeFilter.
Ensures rock-solid, 100% reliable rendering without any blank screens or glitched states.
"""
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
INDEX_HTML = os.path.join(PROJECT_DIR, "index.html")
PREVIEW_HTML = os.path.join(PROJECT_DIR, "preview.html")

STRAY_BRACE_BLOCK = """        // 100% Dedicated to YouTube Shorts for Authenticated Real-Time View Count Accuracy
        var plat = "shorts";
        var exactUrl = "https://www.youtube.com/shorts/" + realId;
        var authorDisplay = baseItem.ytChannel;
        }"""

CLEAN_BRACE_BLOCK = """        // 100% Dedicated to YouTube Shorts for Authenticated Real-Time View Count Accuracy
        var plat = "shorts";
        var exactUrl = "https://www.youtube.com/shorts/" + realId;
        var authorDisplay = baseItem.ytChannel;"""

OLD_SET_TIME_FILTER = """    function setTimeFilter(filter, btn) {
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

BULLETPROOF_SET_TIME_FILTER = """    function setTimeFilter(filter, btn) {
      activeTimeFilter = filter;
      activeSurgeFilter = null;
      var buttons = document.querySelectorAll(".time-filter-section .t-btn");
      for (var i = 0; i < buttons.length; i++) buttons[i].classList.remove("active");
      if (btn) btn.classList.add("active");

      var grid = document.getElementById("videoGrid");
      if (grid) {
        grid.style.opacity = "1";
        grid.classList.remove("grid-fade-in");
        void grid.offsetWidth; // force reflow for smooth animation
        grid.classList.add("grid-fade-in");
      }
      renderVideos();

      showToast("🕒 [" + getTimeFilterLabel(filter) + "] 랭킹으로 전환되었습니다 (조회수 역순 정렬)", "info");
    }"""

def fix_file(filepath):
    print(f"Fixing {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove Stray Brace
    if STRAY_BRACE_BLOCK in content:
        content = content.replace(STRAY_BRACE_BLOCK, CLEAN_BRACE_BLOCK, 1)
        print("Removed stray brace successfully.")
    else:
        print("WARNING: STRAY_BRACE_BLOCK pattern not matched!")

    # 2. Bulletproof setTimeFilter
    if OLD_SET_TIME_FILTER in content:
        content = content.replace(OLD_SET_TIME_FILTER, BULLETPROOF_SET_TIME_FILTER, 1)
        print("Replaced setTimeFilter with bulletproof synchronous version.")
    else:
        print("WARNING: OLD_SET_TIME_FILTER not matched!")

    # 3. Add CSS for grid-fade-in if not present
    if ".grid-fade-in" not in content:
        css_insert = """
    @keyframes gridFadeIn {
      from { opacity: 0.35; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .grid-fade-in {
      animation: gridFadeIn 0.25s ease-out;
    }
    """
        content = content.replace("</style>", css_insert + "\n  </style>", 1)
        print("Added .grid-fade-in CSS animation.")

    # 4. Verify Brace Balance
    script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
    if script_match:
        script = script_match.group(1)
        open_b = script.count('{')
        close_b = script.count('}')
        print(f"Brace balance check: open={open_b}, close={close_b}")
        if open_b != close_b:
            print(f"ERROR: Brace mismatch in {filepath}! Difference: {open_b - close_b}")
            return False

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully saved {filepath} (len: {len(content)})\n")
    return True

if __name__ == "__main__":
    s1 = fix_file(INDEX_HTML)
    s2 = fix_file(PREVIEW_HTML)
    print(f"Finished: index={s1}, preview={s2}")
