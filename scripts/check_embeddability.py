import urllib.request
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

# Test embed status for each video
# In YouTube oembed, if embedding is disabled, it returns 401 or html has "unplayable"
unembeddable = []
embeddable = {}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://kimkimstar.github.io/staridium/'
}

for cat, items in db.items():
    embeddable[cat] = []
    for itm in items:
        vid = itm['youtubeId']
        embed_url = f"https://www.youtube.com/embed/{vid}"
        try:
            req = urllib.request.Request(embed_url, headers=headers)
            with urllib.request.urlopen(req, timeout=3) as res:
                content = res.read().decode('utf-8', errors='ignore')
                # Check for playabilityStatus
                if '"UNPLAYABLE"' in content or '"LIVE_STREAM_OFFLINE"' in content or '"LOGIN_REQUIRED"' in content:
                    print(f"[{cat}] {vid} is UNPLAYABLE: {itm['title'][:30]}")
                    unembeddable.append((cat, vid, itm['title']))
                else:
                    embeddable[cat].append(itm)
        except Exception as e:
            print(f"[{cat}] {vid} error {e}")
            unembeddable.append((cat, vid, str(e)))

print("\n--- Summary ---")
for cat, itms in embeddable.items():
    print(f"{cat:12}: {len(itms)} / {len(db[cat])} fully embeddable and playable")
