import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load the verified pool of 45 YouTube IDs
with open('3_바이럴분석_SaaS_ViralScope/scripts/validated_yt_pool.json', 'r', encoding='utf-8') as f:
    pool = json.load(f)

yt_ids = [p['id'] for p in pool]
print(f"Loaded {len(yt_ids)} verified YouTube IDs.")
