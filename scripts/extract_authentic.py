import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/scripts/apply_authentic_thumbnails.py', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'(\w+):\s*\[(.*?)\]', text, re.DOTALL)
cat_dict = {}
for cat, content in matches:
    items = re.findall(r'\{\s*id:\s*"([^"]+)",\s*thumbnail:\s*"([^"]+)",\s*title:\s*"([^"]+)",\s*ytChannel:\s*"([^"]+)",\s*subIndex:\s*(\d+)\s*\}', content)
    cat_dict[cat] = []
    for itm in items:
        cat_dict[cat].append({
            'id': itm[0],
            'thumbnail': itm[1],
            'title': itm[2],
            'ytChannel': itm[3],
            'subIndex': int(itm[4])
        })

print("Extracted categories:", list(cat_dict.keys()))
for c, itms in cat_dict.items():
    print(f"{c:12}: {len(itms)} items")

with open('3_바이럴분석_SaaS_ViralScope/scripts/extracted_categories.json', 'w', encoding='utf-8') as out:
    json.dump(cat_dict, out, ensure_ascii=False, indent=2)
print("Saved extracted_categories.json")
