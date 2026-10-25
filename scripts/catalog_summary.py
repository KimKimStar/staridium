import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Collect all IDs and their titles/authors
catalog = {}
for cat, items in db.items():
    for it in items:
        vid = it['youtubeId']
        if vid not in catalog:
            catalog[vid] = {
                'id': vid,
                'title': it.get('title', ''),
                'author': it.get('author', it.get('ytChannel', '')),
                'cat': cat
            }

print(f"Loaded {len(catalog)} unique catalog items.")
# print samples per category
cats = set(x['cat'] for x in catalog.values())
for c in sorted(cats):
    items_c = [x for x in catalog.values() if x['cat'] == c]
    print(f"Cat {c:12}: {len(items_c)} items (e.g. {items_c[0]['id']} - {items_c[0]['title'][:25]})")
