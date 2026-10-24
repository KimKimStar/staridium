import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load the verified category photos dictionary
with open("3_바이럴분석_SaaS_ViralScope/scripts/verified_category_photos.json", "r", encoding="utf-8") as f:
    photos = json.load(f)

# Ensure all pools have odd count for co-primality with 4
for cat, pool in photos.items():
    if len(pool) % 2 == 0:
        pool.pop()

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Generate JS code for CATEGORY_PHOTOS
cat_photos_js = "    var CATEGORY_PHOTOS = " + json.dumps(photos, ensure_ascii=False, indent=6) + ";\n"

# Generate getDiverseCategoryThumbnail function
func_js = """
    // Rich, High-Resolution Topic Thumbnail Generator (Zero Stale Repeats, 100% Topic-Matched)
    function getDiverseCategoryThumbnail(topicKey, rank, pOffset, timeFilter) {
      var pool = (CATEGORY_PHOTOS && CATEGORY_PHOTOS[topicKey]) ? CATEGORY_PHOTOS[topicKey] : CATEGORY_PHOTOS["total_kr"];
      if (!pool || pool.length === 0) pool = CATEGORY_PHOTOS["total_kr"];

      var photoIndex = (rank - 1 + (pOffset * 5)) % pool.length;
      var photoId = pool[photoIndex];

      var crops = ["entropy", "center", "faces", "top"];
      var cropMode = crops[(rank - 1 + pOffset) % crops.length];

      return "https://images.unsplash.com/photo-" + photoId + "?w=600&h=1067&fit=crop&crop=" + cropMode + "&auto=format&q=80";
    }
"""

# Replace or add CATEGORY_PHOTOS and getDiverseCategoryThumbnail
if "var CATEGORY_PHOTOS =" in html:
    html = re.sub(r'var CATEGORY_PHOTOS = \{.*?\};\s*', '', html, flags=re.DOTALL)
if "function getDiverseCategoryThumbnail" in html:
    html = re.sub(r'function getDiverseCategoryThumbnail\(.*?\n    \}\n', '', html, flags=re.DOTALL)

# Insert right before generateDetailedVideoAnalysis
marker = "    // Comprehensive AI Deep-Dive Video Analyzer:"
if marker in html:
    html = html.replace(marker, cat_photos_js + func_js + "\n" + marker)
    print("Inserted CATEGORY_PHOTOS and getDiverseCategoryThumbnail!")
else:
    print("Marker not found, inserting before generateVideosForFilter...")
    html = html.replace("    function generateVideosForFilter(", cat_photos_js + func_js + "\n    function generateVideosForFilter(")

# Now update realThumbnail assignment in generateVideosForFilter
# Replace:
# `var realThumbnail = "https://i.ytimg.com/vi/" + realYtId + "/hqdefault.jpg";`
# with:
# `var realThumbnail = getDiverseCategoryThumbnail(topicKey, i, pOffset, timeFilter);`
old_thumb_assign = 'var realThumbnail = "https://i.ytimg.com/vi/" + realYtId + "/hqdefault.jpg";'
new_thumb_assign = 'var realThumbnail = getDiverseCategoryThumbnail(topicKey, i, pOffset, timeFilter);'

if old_thumb_assign in html:
    html = html.replace(old_thumb_assign, new_thumb_assign)
    print("Updated realThumbnail to use getDiverseCategoryThumbnail!")
else:
    print("old_thumb_assign not found, searching with regex...")
    html = re.sub(r'var realThumbnail = [^;]+;', new_thumb_assign, html)
    print("Replaced realThumbnail with regex")

# Also in renderVideos, fallback thumbnail should use getDiverseCategoryThumbnail:
old_render_thumb = "var realThumb = v.thumbnail || ('https://i.ytimg.com/vi/' + v.youtubeId + '/hqdefault.jpg');"
new_render_thumb = "var realThumb = v.thumbnail || getDiverseCategoryThumbnail(currentTopicKey, i + 1, 0, activeTimeFilter);"
if old_render_thumb in html:
    html = html.replace(old_render_thumb, new_render_thumb)
    print("Updated renderVideos fallback thumbnail!")

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated index.html successfully!")
