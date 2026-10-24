import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("3_바이럴분석_SaaS_ViralScope/scripts/extracted_categories.json", "r", encoding="utf-8") as f:
    authentic_items = json.load(f)

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build the authentic TOPIC_SPECIFIC_ITEMS JavaScript object
topic_js = "    var TOPIC_SPECIFIC_ITEMS = {\n"

cat_keys = list(authentic_items.keys())
for idx, cat in enumerate(cat_keys):
    items = authentic_items[cat]
    topic_js += f"      // {cat}\n      {cat}: [\n"
    item_lines = []
    for itm in items:
        item_lines.append(f'        {{ id: "{itm["id"]}", thumbnail: "{itm["thumbnail"]}", title: "{itm["title"]}", ytChannel: "{itm["ytChannel"]}", subIndex: {itm["subIndex"]} }}')
    topic_js += ",\n".join(item_lines) + "\n      ]"
    if idx < len(cat_keys) - 1:
        topic_js += ",\n\n"
    else:
        topic_js += "\n    };\n"

# Replace TOPIC_SPECIFIC_ITEMS in index.html
html = re.sub(r'var TOPIC_SPECIFIC_ITEMS = \{.*?\n    \};', topic_js.strip(), html, flags=re.DOTALL)

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Restored authentic TOPIC_SPECIFIC_ITEMS with topic-specific titles & thumbnails!")
