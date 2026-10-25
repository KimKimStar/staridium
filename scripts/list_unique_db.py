import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open(r'3_바이럴분석_SaaS_ViralScope\scripts\authentic_korean_shorts_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

all_items = []
seen = set()
for cat, items in db.items():
    for it in items:
        vid = it['youtubeId']
        if vid not in seen:
            seen.add(vid)
            all_items.append((cat, vid, it['title'], it['author']))

print(f'Total unique verified videos in authentic DB: {len(all_items)}')
for cat, vid, title, author in all_items[:20]:
    print(f'[{cat}] {vid} - {title[:35]} ({author})')
