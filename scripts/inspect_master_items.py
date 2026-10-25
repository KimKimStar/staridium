import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open("3_바이럴분석_SaaS_ViralScope/scripts/compiled_search_engine_data.json", "r", encoding="utf-8") as f:
    engine_data = json.load(f)

with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "r", encoding="utf-8") as f:
    core_db = json.load(f)

# Combine into one master search database of REAL items
all_master_videos = []
seen = set()

for dom_key, dom_val in engine_data["domains"].items():
    for v in dom_val["videos"]:
        if v["ytId"] not in seen:
            seen.add(v["ytId"])
            all_master_videos.append({
                "youtubeId": v["ytId"],
                "title": v["title"],
                "author": v["channel"],
                "thumbnail": v["thumbnail"],
                "cat": dom_key,
                "keywords": dom_val["keywords"]
            })

for cat_key, items in core_db.items():
    for it in items:
        yid = it["youtubeId"]
        if yid not in seen:
            seen.add(yid)
            all_master_videos.append({
                "youtubeId": yid,
                "title": it.get("title", ""),
                "author": it.get("author", it.get("ytChannel", "한국 크리에이터")),
                "thumbnail": it.get("thumbnail", f"https://i.ytimg.com/vi/{yid}/hqdefault.jpg"),
                "cat": cat_key,
                "keywords": [cat_key]
            })

print(f"Total authentic master videos: {len(all_master_videos)}")
print("Sample titles:")
for v in all_master_videos[:10]:
    print(f"  [{v['cat']}] {v['youtubeId']} | {v['title'][:40]} ({v['author']})")
