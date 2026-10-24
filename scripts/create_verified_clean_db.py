import urllib.request
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

print("Verifying cleaned database...")
verified_clean = {}

for cat, items in db.items():
    verified_clean[cat] = []
    for itm in items:
        vid = itm['youtubeId']
        raw_t = itm['title']
        clean_t = re.sub(r'#[a-zA-Z0-9_\uac00-\ud7a3]+', '', raw_t)
        clean_t = re.sub(r'[\U00010000-\U0010ffff]', '', clean_t)
        clean_t = re.sub(r'[\r\n\t]+', ' ', clean_t)
        clean_t = re.sub(r'\s+', ' ', clean_t).strip()
        
        # Clean title from trailing junk
        clean_t = clean_t.replace("!!", "!").replace("??", "?")
        
        if len(clean_t) >= 5 and "제훈체" not in clean_t and "엄지원" not in clean_t and not clean_t.startswith("★"):
            verified_clean[cat].append({
                "youtubeId": vid,
                "title": clean_t,
                "author": itm['author'].strip(),
                "thumbnail": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
                "videoUrl": f"https://www.youtube.com/shorts/{vid}",
                "subIndex": len(verified_clean[cat]) % 3
            })

for cat, itms in verified_clean.items():
    print(f"{cat:12}: {len(itms)} clean real videos")
    for itm in itms[:2]:
        print(f"   [{itm['youtubeId']}] {itm['author']} : {itm['title']}")

with open("3_바이럴분석_SaaS_ViralScope/scripts/verified_clean_shorts_db.json", "w", encoding="utf-8") as f:
    json.dump(verified_clean, f, ensure_ascii=False, indent=2)

print("Saved verified_clean_shorts_db.json!")
