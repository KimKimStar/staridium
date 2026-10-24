import urllib.request
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's clean and verify the titles in authentic_korean_shorts_db.json
with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

def clean_title(t):
    # Remove #hashtags
    t = re.sub(r'#[a-zA-Z0-9_\uac00-\ud7a3]+', '', t)
    # Remove emojis that break CP949 or looks spammy
    t = re.sub(r'[\U00010000-\U0010ffff]', '', t)
    # Remove excessive punctuation
    t = re.sub(r'\s+', ' ', t).strip()
    return t

cleaned_db = {}
for cat, items in db.items():
    cleaned_db[cat] = []
    for itm in items:
        ct = clean_title(itm['title'])
        if len(ct) >= 6 and not ct.startswith("★") and "광고" not in ct:
            cleaned_db[cat].append({
                "youtubeId": itm['youtubeId'],
                "title": ct,
                "author": itm['author'],
                "thumbnail": f"https://i.ytimg.com/vi/{itm['youtubeId']}/hqdefault.jpg",
                "subIndex": itm.get('subIndex', 0)
            })

for cat, itms in cleaned_db.items():
    print(f"{cat:12}: {len(itms)} clean items")
    for itm in itms[:2]:
        print(f"   [{itm['youtubeId']}] {itm['author']} - {itm['title']}")
