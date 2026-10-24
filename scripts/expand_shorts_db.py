import urllib.request
import urllib.parse
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

SECONDARY_QUERIES = {
    "total_kr": "한국 숏폼 떡상 조회수 1위",
    "diet": "다이어트 전후 살빼는법 숏츠",
    "finance": "직장인 돈모으기 부자 숏츠",
    "cooking": "1분 요리 꿀조합 레시피 숏츠",
    "beauty": "올영 세일 꿀템 피부 숏츠",
    "tech": "아이폰 갤럭시 숨은기능 꿀팁 숏츠",
    "pets": "강아지 고양이 레전드 귀여운 숏츠",
    "psychology": "말잘하는법 호감 말투 심리 숏츠",
    "humor": "너덜트 숏박스 스케치코미디 숏츠",
    "growth": "동기부여 성공 습관 마인드셋 숏츠",
    "fashion": "남자 여자 가을 옷 코디 숏츠",
    "travel": "국내 힐링 여행지 드라이브 숏츠",
    "english": "원어민 1분 영어 회화 패턴 숏츠"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}

for cat_key, query in SECONDARY_QUERIES.items():
    current_items = db.get(cat_key, [])
    existing_ids = {itm['youtubeId'] for itm in current_items}
    
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as res:
            html = res.read().decode('utf-8', errors='ignore')
            shorts_ids = re.findall(r'/shorts/([a-zA-Z0-9_-]{11})', html)
            v_ids = re.findall(r'"videoId":\s*"([a-zA-Z0-9_-]{11})"', html)
            all_ids = [vid for vid in list(dict.fromkeys(shorts_ids + v_ids)) if vid not in existing_ids]
            
            added = 0
            for vid in all_ids:
                if len(current_items) >= 25 or added >= 10:
                    break
                oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
                try:
                    oreq = urllib.request.Request(oembed_url, headers=headers)
                    with urllib.request.urlopen(oreq, timeout=3) as ores:
                        if ores.status == 200:
                            odata = json.loads(ores.read().decode('utf-8'))
                            title = odata.get('title', '').strip()
                            author = odata.get('author_name', '').strip()
                            thumb = f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
                            if title and author:
                                current_items.append({
                                    "youtubeId": vid,
                                    "title": title,
                                    "author": author,
                                    "thumbnail": thumb,
                                    "subIndex": len(current_items) % 3
                                })
                                existing_ids.add(vid)
                                added += 1
                except Exception:
                    pass
            db[cat_key] = current_items
            print(f"{cat_key:12}: now {len(current_items)} authentic Korean shorts (added {added})")
    except Exception as e:
        print(f"Error on {cat_key}: {e}")

with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Finished updating authentic_korean_shorts_db.json!")
