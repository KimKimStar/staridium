import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

for cat, items in db.items():
    print(f"\n=== {cat} ({len(items)} items) ===")
    for itm in items[:3]:
        print(f"  [{itm['youtubeId']}] {itm['author']} - {itm['title']}")
        print(f"    Thumb: {itm['thumbnail']}")
