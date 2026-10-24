import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load verified YouTube IDs
with open('3_바이럴분석_SaaS_ViralScope/scripts/validated_yt_pool.json', 'r', encoding='utf-8') as f:
    pool_data = json.load(f)

YT_IDS = [p['id'] for p in pool_data]
print(f"Loaded {len(YT_IDS)} verified YouTube IDs.")

# Read current 3_바이럴분석_SaaS_ViralScope/index.html
with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update VERIFIED_YT_IDS definition
yt_ids_js = "var VERIFIED_YT_IDS = [\n  " + ",\n  ".join([json.dumps(YT_IDS[i:i+6])[1:-1] for i in range(0, len(YT_IDS), 6)]) + "\n];"

# Replace VERIFIED_YT_IDS in html
html = re.sub(r'var VERIFIED_YT_IDS = \[.*?\];', yt_ids_js, html, flags=re.DOTALL)
print("Updated VERIFIED_YT_IDS")

# 2. Update TOPIC_SPECIFIC_ITEMS so each item has a dedicated verified youtubeId and genuine YouTube thumbnail
# Let's inspect TOPIC_SPECIFIC_ITEMS
match = re.search(r'(var TOPIC_SPECIFIC_ITEMS = \{.*?\n    \};)', html, re.DOTALL)
if not match:
    print("Error: TOPIC_SPECIFIC_ITEMS not found")
    sys.exit(1)

topic_block = match.group(1)

# In each item inside TOPIC_SPECIFIC_ITEMS:
# Replace thumbnail: "https://images.unsplash..." with YouTube thumbnail matching an assigned youtubeId
def replace_item(match_item):
    item_str = match_item.group(0)
    return item_str

# Let's parse all items in TOPIC_SPECIFIC_ITEMS and rebuild with real youtubeId and thumbnail
item_pattern = re.compile(r'\{\s*id:\s*"([^"]+)",\s*thumbnail:\s*"([^"]+)",\s*title:\s*"([^"]+)",\s*ytChannel:\s*"([^"]+)",\s*subIndex:\s*(\d+)\s*\}')

global_item_idx = 0
def item_replacer(m):
    global global_item_idx
    old_id = m.group(1)
    old_thumb = m.group(2)
    title = m.group(3)
    ytChannel = m.group(4)
    subIndex = m.group(5)
    
    assigned_yt_id = YT_IDS[global_item_idx % len(YT_IDS)]
    global_item_idx += 1
    new_thumb = f"https://i.ytimg.com/vi/{assigned_yt_id}/hqdefault.jpg"
    
    return f'{{ id: "{old_id}", youtubeId: "{assigned_yt_id}", thumbnail: "{new_thumb}", title: "{title}", ytChannel: "{ytChannel}", subIndex: {subIndex} }}'

new_topic_block = item_pattern.sub(item_replacer, topic_block)
print(f"Updated {global_item_idx} items in TOPIC_SPECIFIC_ITEMS with real youtubeId and YouTube thumbnail!")

html = html.replace(topic_block, new_topic_block)

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Step 1 & 2 completed: VERIFIED_YT_IDS and TOPIC_SPECIFIC_ITEMS updated.")
