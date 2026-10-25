import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Flatten master pool of all 315 items
master_pool = []
seen = set()
for cat, items in db.items():
    for it in items:
        yid = it['youtubeId']
        if yid not in seen:
            seen.add(yid)
            master_pool.append(it)

print("Master pool size:", len(master_pool))

def get_hash_videos(kw, pool, count=8):
    # compute 32-bit hash
    h = 0
    for ch in kw:
        h = ((h * 31) + ord(ch)) & 0xFFFFFFFF
    
    stride = (h % 11) + 2 # stride 2~12
    offset = h % len(pool)
    
    selected = []
    seen_ids = set()
    for i in range(len(pool)):
        idx = (offset + i * stride) % len(pool)
        item = pool[idx]
        if item['youtubeId'] not in seen_ids:
            seen_ids.add(item['youtubeId'])
            selected.append(item)
            if len(selected) >= count:
                break
    return selected

test_kws = ["낚시", "마술", "우주", "식물", "피아노", "타로", "서핑"]
results = {}
for kw in test_kws:
    vids = get_hash_videos(kw, master_pool)
    ids = [v['youtubeId'] for v in vids]
    results[kw] = ids
    print(f"Keyword '{kw}': IDs = {ids[:4]} (total {len(ids)})")

# Check overlap between 낚시 and 마술
overlap = set(results["낚시"]).intersection(set(results["마술"]))
print(f"Overlap between 낚시 and 마술: {overlap}")
assert len(overlap) < 3, "Keywords should have distinct video distributions"
print("SUCCESS: Dynamic hash mapping generates distinct video sets for different keywords!")
