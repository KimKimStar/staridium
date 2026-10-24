import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

print("Categories in DB:")
for k, v in db.items():
    print(f"  {k:12}: {len(v)} real Korean shorts")
