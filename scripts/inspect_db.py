import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\scripts\authentic_korean_shorts_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

print('Categories in DB:', len(db))
for cat, items in db.items():
    print(f'  {cat}: {len(items)} items')
    for it in items[:2]:
        print(f'    [{it["youtubeId"]}] {it["title"][:35]} ({it["author"]})')
