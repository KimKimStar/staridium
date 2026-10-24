import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load verified clean shorts database
with open("3_바이럴분석_SaaS_ViralScope/scripts/verified_clean_shorts_db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 2. Add <meta name="referrer" content="strict-origin-when-cross-origin" /> to <head>
if '<meta name="referrer"' not in html:
    html = html.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0" />',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n  <meta name="referrer" content="strict-origin-when-cross-origin" />'
    )
    print("Added meta referrer tag to <head>")

# 3. Build pristine TOPIC_SPECIFIC_ITEMS
topic_js = "    var TOPIC_SPECIFIC_ITEMS = {\n"
cat_keys = list(db.keys())

for c_idx, cat in enumerate(cat_keys):
    items = db[cat]
    topic_js += f"      // {cat} ({len(items)} clean verified Korean shorts)\n      {cat}: [\n"
    item_lines = []
    for i, itm in enumerate(items):
        clean_title = itm['title'].replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ').strip()
        clean_author = itm['author'].replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ').strip()
        yid = itm['youtubeId']
        thumb = f"https://i.ytimg.com/vi/{yid}/hqdefault.jpg"
        subIdx = itm.get('subIndex', i % 3)
        item_lines.append(f'        {{ id: "{cat}-{i+1}", youtubeId: "{yid}", thumbnail: "{thumb}", title: "{clean_title}", ytChannel: "{clean_author}", subIndex: {subIdx} }}')
    topic_js += ",\n".join(item_lines) + "\n      ]"
    if c_idx < len(cat_keys) - 1:
        topic_js += ",\n\n"
    else:
        topic_js += "\n    };\n"

html = re.sub(r'var TOPIC_SPECIFIC_ITEMS = \{.*?\n    \};', topic_js.strip(), html, flags=re.DOTALL)
print("Updated TOPIC_SPECIFIC_ITEMS with clean Korean shorts!")

# 4. In generateVideosForFilter: ensure clean title and 100% matched URL
# Replace title formatting logic with clean direct title
title_gen_code = """
        var realYtId = baseItem.youtubeId;
        var realId = realYtId;
        var exactUrl = "https://www.youtube.com/shorts/" + realYtId;
        var realThumbnail = "https://i.ytimg.com/vi/" + realYtId + "/hqdefault.jpg";
        
        // Exact 100% Matching Video Title
        var fullTitle = baseItem.title;
"""

# Replace in generateVideosForFilter
html = re.sub(
    r'var realYtId = baseItem\.youtubeId.*?\n\s*var fullTitle = "";.*?else fullTitle = "[^"]+" \+ baseItem\.title;\s*\}',
    title_gen_code.strip(),
    html,
    flags=re.DOTALL
)
print("Updated title and URL assignment in generateVideosForFilter!")

# 5. Fix openAnatomyModal to eliminate Error 153
# Build clean embed URL with referrerpolicy and origin
modal_embed_code = """
      var platText = '🔴 YouTube Shorts 공식 실시간 플레이어';
      document.getElementById("modalPlayerPlatformLabel").innerText = platText;

      // Fix YouTube Error 153: Clean embed parameters, strict referrer policy & origin header
      var embedUrl = "https://www.youtube.com/embed/" + currentVideo.youtubeId + "?autoplay=1&mute=1&playsinline=1&rel=0&enablejsapi=1";
      if (window.location.protocol !== "file:") {
        embedUrl += "&origin=" + encodeURIComponent(window.location.origin);
      }

      var iframeWrap = document.getElementById("videoIframeWrap");
      iframeWrap.innerHTML = '<iframe src="' + embedUrl + '" title="' + currentVideo.title.replace(/"/g, '&quot;') + '" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="width:100%; height:100%; border:0; border-radius:12px;"></iframe>';

      // Set Exact Video URL in Modal
      document.getElementById("modalUrlInput").value = currentVideo.videoUrl;
      document.getElementById("modalOriginalLink").href = currentVideo.videoUrl;
"""

html = re.sub(
    r'var platText = \'🔴 YouTube Shorts.*?\n\s*document\.getElementById\("modalOriginalLink"\)\.href = currentVideo\.videoUrl;',
    modal_embed_code.strip(),
    html,
    flags=re.DOTALL
)
print("Updated openAnatomyModal with Error 153 prevention!")

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated index.html successfully!")
