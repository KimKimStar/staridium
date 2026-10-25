import urllib.request
import urllib.parse
import json
import re
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

SEARCH_TOPICS = {
    "golf": "골프 레슨 스윙 쇼츠",
    "soccer": "축구 손흥민 이강인 개인기 쇼츠",
    "camping": "캠핑 차박 텐트 꿀템 쇼츠",
    "music": "아이유 뉴진스 노래 댄스 챌린지 쇼츠",
    "game": "롤 게임 꿀팁 배그 쇼츠",
    "car": "자동차 운전 꿀팁 중고차 쇼츠",
    "health": "헬스 운동 벤치프레스 득근 쇼츠",
    "movie": "영화 드라마 리뷰 명장면 쇼츠",
    "study": "공부 자극 공부법 수능 쇼츠",
    "love": "연애 꿀팁 심리 소개팅 쇼츠",
    "fishing": "낚시 손맛 대물 꿀팁 쇼츠",
    "magic": "마술 트릭 신기한 마술 쇼츠"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}

collected_domains = {}

for domain, query in SEARCH_TOPICS.items():
    print(f"\nSearching YouTube for domain '{domain}' with query '{query}'...")
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as res:
            html = res.read().decode('utf-8', errors='ignore')
            
            # Find candidate IDs
            shorts_ids = re.findall(r'/shorts/([a-zA-Z0-9_-]{11})', html)
            v_ids = re.findall(r'"videoId":\s*"([a-zA-Z0-9_-]{11})"', html)
            all_ids = list(dict.fromkeys(shorts_ids + v_ids))
            print(f"  Found {len(all_ids)} candidate IDs")
            
            valid_items = []
            for vid in all_ids:
                if len(valid_items) >= 12:
                    break
                oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
                try:
                    oreq = urllib.request.Request(oembed_url, headers=headers)
                    with urllib.request.urlopen(oreq, timeout=3) as ores:
                        if ores.status == 200:
                            data = json.loads(ores.read().decode('utf-8'))
                            title = data.get('title', '').strip()
                            author = data.get('author_name', '').strip()
                            if title and author:
                                valid_items.append({
                                    "youtubeId": vid,
                                    "title": title,
                                    "author": author,
                                    "thumbnail": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
                                })
                                print(f"    [OK] {vid}: {title[:35]} ({author})")
                except Exception:
                    pass
            
            collected_domains[domain] = valid_items
            print(f"  Total valid verified items for {domain}: {len(valid_items)}")
    except Exception as e:
        print(f"  Error fetching {domain}: {e}")

output_path = "3_바이럴분석_SaaS_ViralScope/scripts/verified_search_domains.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(collected_domains, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully saved verified search domains to {output_path}!")
