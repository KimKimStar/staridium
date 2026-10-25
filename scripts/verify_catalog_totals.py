import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open("3_바이럴분석_SaaS_ViralScope/scripts/verified_search_domains.json", "r", encoding="utf-8") as f:
    domains_data = json.load(f)

# Also load authentic_korean_shorts_db.json
with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "r", encoding="utf-8") as f:
    core_db = json.load(f)

print(f"Loaded {len(domains_data)} verified search domains.")
for k, v in domains_data.items():
    print(f"  {k}: {len(v)} verified videos")

# Let's count total verified unique videos across all databases
all_unique = {}
for k, items in core_db.items():
    for it in items:
        all_unique[it['youtubeId']] = it

for k, items in domains_data.items():
    for it in items:
        all_unique[it['youtubeId']] = it

print(f"Total unique verified playable videos in master catalog: {len(all_unique)}")
