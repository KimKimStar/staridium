import urllib.request
import urllib.parse
import json
import re
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

CATEGORIES_QUERIES = {
    "total_kr": "한국 인기 급상승 쇼츠",
    "diet": "다이어트 식단 홈트 쇼츠",
    "finance": "재테크 주식 돈모으기 쇼츠",
    "cooking": "초간단 요리 레시피 쇼츠",
    "beauty": "올리브영 뷰티 스킨케어 쇼츠",
    "tech": "스마트폰 꿀기능 IT 쇼츠",
    "pets": "강아지 고양이 반려동물 쇼츠",
    "psychology": "인간관계 대화법 심리 쇼츠",
    "humor": "일상 공감 스케치코미디 쇼츠",
    "growth": "자기계발 갓생 동기부여 쇼츠",
    "fashion": "데일리룩 패션 코디 쇼츠",
    "travel": "국내여행 핫플 숙소 쇼츠",
    "english": "원어민 실전 생활영어 쇼츠"
}

collected_database = {}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}

for cat_key, query in CATEGORIES_QUERIES.items():
    print(f"Scraping category: {cat_key} with query: '{query}'...")
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as res:
            html = res.read().decode('utf-8', errors='ignore')
            
            # Find shorts IDs
            shorts_ids = re.findall(r'/shorts/([a-zA-Z0-9_-]{11})', html)
            v_ids = re.findall(r'"videoId":\s*"([a-zA-Z0-9_-]{11})"', html)
            all_ids = list(dict.fromkeys(shorts_ids + v_ids))
            
            print(f"  Found {len(all_ids)} raw candidate IDs for {cat_key}")
            
            cat_items = []
            for vid in all_ids:
                if len(cat_items) >= 15:
                    break
                # Validate with oembed
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
                                cat_items.append({
                                    "youtubeId": vid,
                                    "title": title,
                                    "author": author,
                                    "thumbnail": thumb,
                                    "subIndex": len(cat_items) % 3
                                })
                except Exception:
                    pass
            
            print(f"  Successfully collected {len(cat_items)} authentic Korean shorts for {cat_key}")
            collected_database[cat_key] = cat_items
    except Exception as e:
        print(f"  Error scraping {cat_key}: {e}")

print("\nTotal categories collected:", len(collected_database))
with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "w", encoding="utf-8") as f:
    json.dump(collected_database, f, ensure_ascii=False, indent=2)

print("Saved to authentic_korean_shorts_db.json!")
