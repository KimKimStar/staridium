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

# Load verified_clean_shorts_db.json
db_path = os.path.join(script_dir, "verified_clean_shorts_db.json")
with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

# 1. Build a genuinely grand, multi-category TOPIC_SPECIFIC_ITEMS.total_kr
# We take the top items from each category in round-robin order to form the ultimate Korean viral leaderboard!
other_cats = ['humor', 'cooking', 'diet', 'tech', 'beauty', 'finance', 'psychology', 'growth', 'pets', 'travel', 'fashion', 'english']
curated_total_kr = []

# Collect top 2-3 items from each category
max_len = max(len(db.get(c, [])) for c in other_cats)
for rank_idx in range(max_len):
    for c in other_cats:
        c_items = db.get(c, [])
        if rank_idx < len(c_items):
            item = c_items[rank_idx]
            # avoid duplicates
            author_name = item.get('author') or item.get('ytChannel') or '한국 크리에이터'
            if not any(x['youtubeId'] == item['youtubeId'] for x in curated_total_kr):
                curated_total_kr.append({
                    "id": f"total_kr-{len(curated_total_kr) + 1}",
                    "youtubeId": item['youtubeId'],
                    "thumbnail": item['thumbnail'],
                    "title": item['title'],
                    "ytChannel": author_name,
                    "author": author_name,
                    "subIndex": len(curated_total_kr) % 3
                })
        if len(curated_total_kr) >= 30:
            break
    if len(curated_total_kr) >= 30:
        break

print(f"Constructed grand total_kr with {len(curated_total_kr)} diverse multi-category items!")
db['total_kr'] = curated_total_kr

# Save updated db
with open(db_path, "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

# 2. Build MASTER_VIDEO_REGISTRY
# Assign each unique video a stable, realistic master all-time view count
master_registry = {}
# Base view curve for all unique videos
all_unique_ids = []
for cat_name, items in db.items():
    for item in items:
        yId = item['youtubeId']
        if yId not in all_unique_ids:
            all_unique_ids.append(yId)

print(f"Total unique videos to calibrate: {len(all_unique_ids)}")

# Give top videos realistic mega-viral views (58M down to 12M)
for idx, yId in enumerate(all_unique_ids):
    # Stable deterministic calculation from yId hash
    char_sum = sum(ord(ch) for ch in yId)
    # Ranked views with natural variation
    tier_views = max(11500000, int(58000000 - (idx * 240000) + ((char_sum % 50) * 45000)))
    master_registry[yId] = tier_views

print(f"Calibrated master_registry with {len(master_registry)} videos.")
print("Sample views:")
for y in all_unique_ids[:5]:
    print(f"  {y}: {master_registry[y]:,} views ({(master_registry[y]/10000):.0f}만회)")

# 3. Update index.html
# Replace TOPIC_SPECIFIC_ITEMS in HTML with updated db
js_items = "    var TOPIC_SPECIFIC_ITEMS = " + json.dumps(db, ensure_ascii=False, indent=6) + ";\n"
js_registry = "    var MASTER_VIDEO_REGISTRY = " + json.dumps(master_registry, ensure_ascii=False, indent=6) + ";\n"

# Replace TOPIC_SPECIFIC_ITEMS block
pattern = r'var TOPIC_SPECIFIC_ITEMS = \{.*?\n    \};'
if re.search(pattern, html, re.DOTALL):
    html = re.sub(pattern, js_items.strip() + "\n\n" + js_registry.strip(), html, count=1, flags=re.DOTALL)
    print("Replaced TOPIC_SPECIFIC_ITEMS and injected MASTER_VIDEO_REGISTRY!")
else:
    print("TOPIC_SPECIFIC_ITEMS pattern not found!")

# 4. Update view calculation in generateVideosForFilter
# To guarantee 100% CONSISTENCY across all tabs and categories:
# baseViews is derived from MASTER_VIDEO_REGISTRY[realYtId]!
old_calc_marker = """        // Monotonic View Count Hierarchy
        var baseViews = 0;"""

new_calc_block = """        // Monotonic View Count Hierarchy (Single Source of Truth - Guaranteed Identical Everywhere!)
        var masterAllTimeViews = (window.MASTER_VIDEO_REGISTRY && window.MASTER_VIDEO_REGISTRY[realYtId]) ? window.MASTER_VIDEO_REGISTRY[realYtId] : 28500000;
        var periodRatio = 1.0;
        if (timeFilter === "1d") periodRatio = 0.048;      // 24h 실시간 조회수 (120만 ~ 280만)
        else if (timeFilter === "1w") periodRatio = 0.125; // 7일간 누적 조회수 (250만 ~ 720만)
        else if (timeFilter === "1m") periodRatio = 0.26;  // 1개월 누적 조회수 (500만 ~ 1500만)
        else if (timeFilter === "3m") periodRatio = 0.48;  // 3개월 누적 조회수 (1000만 ~ 2800만)
        else if (timeFilter === "6m") periodRatio = 0.72;  // 6개월 누적 조회수 (1800만 ~ 4200만)
        else periodRatio = 1.0;                            // 1년/역대 누적 조회수 (전체)

        var baseViews = Math.floor(masterAllTimeViews * periodRatio);"""

# Replace in html
# We search for baseViews calculation inside generateVideosForFilter
find_start = html.find("function generateVideosForFilter(")
if find_start != -1:
    pos_views = html.find("// Monotonic View Count Hierarchy", find_start)
    pos_views_end = html.find("// Apply Hourly Dynamic Rebalancing Delta", pos_views)
    if pos_views != -1 and pos_views_end != -1:
        html = html[:pos_views] + new_calc_block + "\n\n        " + html[pos_views_end:]
        print("Updated baseViews calculation to use MASTER_VIDEO_REGISTRY (Single Source of Truth)!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML updated successfully!")
