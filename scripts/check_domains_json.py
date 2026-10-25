import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open("3_바이럴분석_SaaS_ViralScope/scripts/verified_search_domains.json", "r", encoding="utf-8") as f:
    domains = json.load(f)

for dom, items in domains.items():
    print(f"Domain: {dom:10} -> {len(items)} items")
    for it in items[:2]:
        print(f"   [{it['youtubeId']}] {it['title'][:35]} ({it['author']})")
