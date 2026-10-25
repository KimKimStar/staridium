import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Inspect titles in db to see what keywords exist
all_titles = []
for cat, items in db.items():
    for it in items:
        all_titles.append((it['youtubeId'], it['title'], it['author'], cat))

print(f"Total titles: {len(all_titles)}")

# Check if any titles contain golf, camping, soccer, etc.
for kw in ['골프', '축구', '캠핑', '아이유', '게임', '차', '자동차', '영화', '음악', '노래', '고양이', '강아지']:
    matches = [t for t in all_titles if kw in t[1]]
    print(f"Keyword '{kw}': {len(matches)} matches")
    if matches:
        print(f"  Sample: {matches[0]}")
