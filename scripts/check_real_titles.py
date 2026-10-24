import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

for cat in ["total_kr", "diet", "finance", "cooking"]:
    print(f"\n==================== {cat} ====================")
    for idx, itm in enumerate(db[cat][:10]):
        print(f"#{idx+1}: Title: {itm['title']}")
        print(f"     Channel: {itm['author']}")
        print(f"     URL: https://www.youtube.com/shorts/{itm['youtubeId']}")
