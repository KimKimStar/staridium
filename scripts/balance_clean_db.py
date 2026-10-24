import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("3_바이럴분석_SaaS_ViralScope/scripts/verified_clean_shorts_db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

# Make total_kr have the top #1 item from every single category plus top viral items
total_kr_items = []
seen = set()

# First add the best items from each category to total_kr
for cat in ["diet", "finance", "cooking", "tech", "humor", "psychology", "growth", "beauty", "pets", "fashion", "travel", "english"]:
    for itm in db[cat][:2]:
        if itm['youtubeId'] not in seen:
            seen.add(itm['youtubeId'])
            total_kr_items.append({
                "youtubeId": itm['youtubeId'],
                "title": itm['title'],
                "author": itm['author'],
                "thumbnail": itm['thumbnail'],
                "videoUrl": itm['videoUrl'],
                "subIndex": len(total_kr_items) % 3
            })

for itm in db['total_kr']:
    if itm['youtubeId'] not in seen and len(total_kr_items) < 25:
        seen.add(itm['youtubeId'])
        total_kr_items.append(itm)

db['total_kr'] = total_kr_items[:25]
print("total_kr now has", len(db['total_kr']), "mega-viral items!")

# If growth has < 25, pad with clean motivation items
if len(db['growth']) < 25:
    db['growth'].append({
        "youtubeId": "ciwAl-uHnAo",
        "title": "성공하는 사람들의 아침 10분 모닝 루틴",
        "author": "모닝갓생",
        "thumbnail": "https://i.ytimg.com/vi/ciwAl-uHnAo/hqdefault.jpg",
        "videoUrl": "https://www.youtube.com/shorts/ciwAl-uHnAo",
        "subIndex": 0
    })
    db['growth'].append({
        "youtubeId": "pcWmS1qANPU",
        "title": "20대에 이것 깨달으면 인생 10년 앞서갑니다",
        "author": "동기부여스쿨",
        "thumbnail": "https://i.ytimg.com/vi/pcWmS1qANPU/hqdefault.jpg",
        "videoUrl": "https://www.youtube.com/shorts/pcWmS1qANPU",
        "subIndex": 1
    })

with open("3_바이럴분석_SaaS_ViralScope/scripts/verified_clean_shorts_db.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Saved perfectly balanced clean shorts database!")
