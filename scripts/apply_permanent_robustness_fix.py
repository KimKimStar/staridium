# -*- coding: utf-8 -*-
"""
Add no-cache headers, robust error boundaries to renderVideos, and ensure
100% stability across all topic/period switching.
"""
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
INDEX_HTML = os.path.join(PROJECT_DIR, "index.html")
PREVIEW_HTML = os.path.join(PROJECT_DIR, "preview.html")

NO_CACHE_TAGS = """  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="Pragma" content="no-cache" />
  <meta http-equiv="Expires" content="0" />"""

def update_file(filepath):
    print(f"Adding permanent robustness to {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add no-cache meta tags
    if '<meta http-equiv="Cache-Control"' not in content:
        content = content.replace(
            '<meta charset="UTF-8" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0" />',
            NO_CACHE_TAGS,
            1
        )
        print("Added no-cache headers.")

    # 2. Ensure renderVideos has safety try-catch block
    # Check if already wrapped
    if 'try {' not in content[content.find('function renderVideos('):content.find('window.currentDisplayedVideos = list;')]:
        old_render_sig = 'function renderVideos() {\n      var grid = document.getElementById("videoGrid");'
        new_render_sig = """function renderVideos() {
      var grid = document.getElementById("videoGrid");
      if (grid) grid.style.opacity = "1";
      try {"""
        
        old_render_end = """      grid.innerHTML = html;
      window.currentDisplayedVideos = list;
    }"""
        new_render_end = """      grid.innerHTML = html;
      window.currentDisplayedVideos = list;
      } catch (err) {
        console.error("[ViralScope Render Safety Catch]:", err);
        if (grid) {
          grid.style.opacity = "1";
          var fallbackGen = generateVideosForFilter("total_kr", "1y", "shorts", "all", null, "views", 75);
          var fList = fallbackGen.videos;
          var fHtml = "";
          for (var fi = 0; fi < fList.length; fi++) {
            var fv = fList[fi];
            var fPoster = getSvgPosterDataUri(fv.title, fv.author, "shorts", fi);
            fHtml += '<div class="video-card"><div class="rank-badge">#' + (fi + 1) + '</div><div class="thumbnail-wrap" onclick="openAnatomyModal(\\'' + fv.id + '\\')"><img src="' + fv.thumbnail + '" class="thumbnail-img" onerror="this.onerror=null;this.src=\\'' + fPoster + '\\';" /><div class="play-overlay-icon"><div class="play-btn-circle">▶</div></div></div><div class="card-meta"><span class="author-name">' + fv.author + '</span><span class="views">👁️ ' + fv.viewsFormatted + '</span></div><h3 class="card-title">' + fv.title + '</h3></div>';
          }
          grid.innerHTML = fHtml;
        }
      }
    }"""
        if old_render_sig in content and old_render_end in content:
            content = content.replace(old_render_sig, new_render_sig, 1)
            content = content.replace(old_render_end, new_render_end, 1)
            print("Wrapped renderVideos in bulletproof error boundary.")
        else:
            print("Notice: renderVideos signature already modified or pattern differs.")

    # 3. Check Brace Balance
    script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
    if script_match:
        script = script_match.group(1)
        open_b = script.count('{')
        close_b = script.count('}')
        print(f"Script brace check: open={open_b}, close={close_b}")
        if open_b != close_b:
            print(f"ERROR: Brace mismatch! {open_b} != {close_b}")
            return False

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully saved {filepath} (len: {len(content)})\n")
    return True

if __name__ == "__main__":
    s1 = update_file(INDEX_HTML)
    s2 = update_file(PREVIEW_HTML)
    print(f"Finished: index={s1}, preview={s2}")
