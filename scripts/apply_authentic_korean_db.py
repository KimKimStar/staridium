import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load the authentic database of 315 Korean shorts
with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Rebuild TOPIC_SPECIFIC_ITEMS with authentic Korean Shorts data
topic_js = "    var TOPIC_SPECIFIC_ITEMS = {\n"
cat_keys = list(db.keys())

for c_idx, cat in enumerate(cat_keys):
    items = db[cat]
    topic_js += f"      // {cat} ({len(items)} authentic Korean shorts)\n      {cat}: [\n"
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
print("Replaced TOPIC_SPECIFIC_ITEMS with 315 authentic Korean shorts!")

# 2. Update VERIFIED_YT_IDS to be a flat list of all 315 authentic YouTube IDs
all_verified_ids = []
for cat in cat_keys:
    for itm in db[cat]:
        if itm['youtubeId'] not in all_verified_ids:
            all_verified_ids.append(itm['youtubeId'])

yt_ids_js = "var VERIFIED_YT_IDS = [\n  " + ",\n  ".join([json.dumps(all_verified_ids[i:i+8])[1:-1] for i in range(0, len(all_verified_ids), 8)]) + "\n];"
html = re.sub(r'var VERIFIED_YT_IDS = \[.*?\];', yt_ids_js, html, flags=re.DOTALL)
print(f"Updated VERIFIED_YT_IDS with {len(all_verified_ids)} unique authentic Korean YouTube IDs!")

# 3. Update generateVideosForFilter
# Ensure realThumbnail is ALWAYS the authentic YouTube thumbnail of that exact video
# var realYtId = baseItem.youtubeId || VERIFIED_YT_IDS[(i - 1 + pOffset) % VERIFIED_YT_IDS.length];
# var realThumbnail = "https://i.ytimg.com/vi/" + realYtId + "/hqdefault.jpg";
gen_replace_old = re.search(r'var realYtId = baseItem\.youtubeId.*?\n\s*var realThumbnail = [^;]+;', html, re.DOTALL)
if gen_replace_old:
    new_thumb_block = """var realYtId = baseItem.youtubeId || VERIFIED_YT_IDS[(i - 1 + pOffset) % VERIFIED_YT_IDS.length];
        var realId = realYtId;
        var exactUrl = "https://www.youtube.com/shorts/" + realYtId;
        var realThumbnail = "https://i.ytimg.com/vi/" + realYtId + "/hqdefault.jpg";"""
    html = html[:gen_replace_old.start()] + new_thumb_block + html[gen_replace_old.end():]
    print("Updated generateVideosForFilter to strictly use authentic YouTube video thumbnail!")
else:
    print("gen_replace_old pattern not matched, checking manual replace...")
    html = re.sub(r'var realThumbnail = [^;]+;', 'var realThumbnail = "https://i.ytimg.com/vi/" + realYtId + "/hqdefault.jpg";', html)

# 4. In renderVideos, ensure fallback also uses the authentic YouTube thumbnail:
html = re.sub(
    r'var realThumb = [^;]+;',
    'var realThumb = v.thumbnail || ("https://i.ytimg.com/vi/" + v.youtubeId + "/hqdefault.jpg");',
    html
)
print("Updated renderVideos thumbnail fallback to authentic YouTube thumbnail!")

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied authentic Korean shorts database to index.html successfully!")
