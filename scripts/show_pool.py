import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('3_바이럴분석_SaaS_ViralScope/scripts/validated_yt_pool.json', 'r', encoding='utf-8') as f:
    pool = json.load(f)

print(f"Total verified IDs in pool: {len(pool)}")
for p in pool[:10]:
    print(p['id'], "-", p['author'][:25], ":", p['title'][:40])
