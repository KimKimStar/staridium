import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/scripts/validated_yt_pool.json', encoding='utf-8') as f:
    pool = json.load(f)

print(f"Total in pool: {len(pool)}")
for i, p in enumerate(pool):
    print(f"{i+1:2d}: {p['id']} - {p['author']} - {p['title']}")
