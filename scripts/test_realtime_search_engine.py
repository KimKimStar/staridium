import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

# Load all 462 master videos
with open("3_바이럴분석_SaaS_ViralScope/scripts/compiled_search_engine_data.json", "r", encoding="utf-8") as f:
    engine_data = json.load(f)

with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "r", encoding="utf-8") as f:
    core_db = json.load(f)

master_videos = []
seen = set()

# Add all domain videos
for dkey, dval in engine_data["domains"].items():
    kws = dval.get("keywords", [])
    for v in dval["videos"]:
        if v["ytId"] not in seen:
            seen.add(v["ytId"])
            master_videos.append({
                "youtubeId": v["ytId"],
                "title": v["title"],
                "author": v["channel"],
                "thumbnail": v["thumbnail"],
                "category": dkey,
                "keywords": kws
            })

# Add core db videos
for ckey, items in core_db.items():
    for it in items:
        yid = it["youtubeId"]
        if yid not in seen:
            seen.add(yid)
            master_videos.append({
                "youtubeId": yid,
                "title": it.get("title", ""),
                "author": it.get("author", it.get("ytChannel", "한국 크리에이터")),
                "thumbnail": it.get("thumbnail", f"https://i.ytimg.com/vi/{yid}/hqdefault.jpg"),
                "category": ckey,
                "keywords": [ckey]
            })

print(f"Total Master Search Catalog: {len(master_videos)} videos")

# Full-Text Search Function
def search_catalog(query):
    q = query.strip().lower()
    tokens = [t for t in re.split(r'[\s,+#]+', q) if t]
    if not tokens:
        return []
    
    scored = []
    for v in master_videos:
        title_lower = v["title"].lower()
        author_lower = v["author"].lower()
        kws_lower = [k.lower() for k in v["keywords"]]
        cat_lower = v["category"].lower()
        
        score = 0
        # 1. Exact phrase match in title
        if q in title_lower:
            score += 100
        # 2. Token match in title
        for t in tokens:
            if t in title_lower:
                score += 30
        # 3. Match in keywords/tags
        for k in kws_lower:
            if q == k:
                score += 50
            elif q in k or k in q:
                score += 25
            for t in tokens:
                if t in k or k in t:
                    score += 15
        # 4. Match in author/channel
        if q in author_lower:
            score += 40
        for t in tokens:
            if t in author_lower:
                score += 20
        # 5. Match in category
        if q == cat_lower or any(t == cat_lower for t in tokens):
            score += 20
            
        if score > 0:
            scored.append((score, v))
            
    scored.sort(key=lambda x: x[0], reverse=True)
    return [x[1] for x in scored]

test_queries = [
    "골프", "스윙", "드라이버", "손흥민", "축구", "이강인", 
    "캠핑", "차박", "아이유", "라면", "불닭", "주차", "운전", 
    "낚시", "마술", "다이어트", "주식", "고양이"
]

for tq in test_queries:
    matches = search_catalog(tq)
    print(f"\nQuery: '{tq}' -> {len(matches)} matches")
    for m in matches[:3]:
        print(f"  [OK] {m['title'][:40]} | {m['author']}")
