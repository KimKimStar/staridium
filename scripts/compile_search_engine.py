import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

# Read verified search domains
with open("3_바이럴분석_SaaS_ViralScope/scripts/verified_search_domains.json", "r", encoding="utf-8") as f:
    domains_data = json.load(f)

# Read authentic core DB
with open("3_바이럴분석_SaaS_ViralScope/scripts/authentic_korean_shorts_db.json", "r", encoding="utf-8") as f:
    core_db = json.load(f)

# Keywords mapping for search domains
DOMAIN_KEYWORDS = {
    "golf": ["골프", "스윙", "드라이버", "퍼팅", "퍼터", "홀인원", "비거리", "아이언", "필드", "싱글", "파3", "골린이", "어프로치", "백스윙", "다운스윙", "골프레슨"],
    "soccer": ["축구", "손흥민", "이강인", "조규성", "황희찬", "메시", "호날두", "토트넘", "프리미어리그", "골", "슈팅", "드리블", "야구", "농구", "월드컵", "스포츠", "풋살", "k리그", "개인기", "국대"],
    "camping": ["캠핑", "차박", "텐트", "글램핑", "백패킹", "불멍", "캠린이", "캠핑요리", "다이소캠핑", "아웃도어", "도킹텐트", "원터치", "매트", "캠핑장"],
    "music": ["아이유", "뉴진스", "bts", "방탄", "음악", "노래", "보컬", "댄스", "챌린지", "피아노", "기타", "음원", "라이브", "커버", "케이팝", "kpop", "직캠", "안무"],
    "game": ["게임", "롤", "lol", "리그오브레전드", "배그", "배틀그라운드", "마인크래프트", "마크", "발로란트", "오버워치", "스팀", "게이밍", "플스", "자크", "이즈", "오공"],
    "car": ["자동차", "차", "중고차", "전기차", "테슬라", "운전", "세차", "튜닝", "면허", "도로연수", "현대", "기아", "차량", "타이어", "주차", "평행주차", "후진주차", "초보운전"],
    "health": ["헬스", "피트니스", "벤치프레스", "벤치", "스쿼트", "득근", "헬창", "단백질", "바디프로필", "가슴운동", "등운동", "어깨운동", "근성장", "운동"],
    "movie": ["영화", "드라마", "넷플릭스", "웹툰", "명장면", "애니", "결말", "줄거리", "리뷰", "오징어게임", "빈센조", "소원"],
    "study": ["공부", "수능", "토익", "공시생", "영단어", "독서", "책", "집중력", "필기", "플래너", "이지영", "모닝루틴", "서울대", "오답노트"],
    "love": ["연애", "소개팅", "썸", "남친", "여친", "고백", "짝사랑", "이별", "재회", "결혼", "플러팅", "호감", "첫인상"],
    "fishing": ["낚시", "물고기", "투망", "오징어", "손맛", "대물", "바다낚시", "메기", "캐스팅", "복어"],
    "magic": ["마술", "트릭", "카드마술", "동전마술", "신기한마술", "손등관통", "마술사", "매직"],
    "ramen": ["라면", "불닭", "신라면", "짜파게티", "라면레시피", "꿀조합", "김종면", "라죽", "야식"]
}

# Build rich SEARCH_DOMAIN_DATABASE JSON
built_domains = {}
for dom_key, vids in domains_data.items():
    kws = DOMAIN_KEYWORDS.get(dom_key, [dom_key])
    clean_vids = []
    for it in vids:
        clean_vids.append({
            "ytId": it["youtubeId"],
            "title": it["title"],
            "channel": it["author"],
            "thumbnail": it.get("thumbnail", f"https://i.ytimg.com/vi/{it['youtubeId']}/hqdefault.jpg"),
            "hook": f"“{it['title'][:40]}...”"
        })
    built_domains[dom_key] = {
        "keywords": kws,
        "videos": clean_vids
    }

# Also collect master catalog of all 462 video IDs
all_ids_pool = []
seen = set()
for dom_key, vids in domains_data.items():
    for it in vids:
        yid = it["youtubeId"]
        if yid not in seen:
            seen.add(yid)
            all_ids_pool.append(yid)

for cat_key, items in core_db.items():
    for it in items:
        yid = it["youtubeId"]
        if yid not in seen:
            seen.add(yid)
            all_ids_pool.append(yid)

print(f"Total all_ids_pool length: {len(all_ids_pool)}")

output_dict = {
    "domains": built_domains,
    "pool": all_ids_pool
}

with open("3_바이럴분석_SaaS_ViralScope/scripts/compiled_search_engine_data.json", "w", encoding="utf-8") as f:
    json.dump(output_dict, f, ensure_ascii=False, indent=2)

print("Saved compiled search engine data successfully!")
