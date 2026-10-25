import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's test candidate IDs for Golf, Soccer, Camping, Music/IU, Gaming, Cars, Fitness, etc.
candidates = {
    "golf": [
        ("N6E_W7sUe20", "골프 스윙 비거리 30m 늘리는 마법의 연습법", "골프레슨TV"),
        ("vK_fVvW-jQY", "아이언 정타 맞추는 특급 노하우", "싱글골퍼"),
        ("L09i7bK2W8Y", "드라이버 슬라이스 1분만에 고치기", "골프연구소"),
        ("dF2O1e7iUeM", "프로들이 절대 안 가르쳐주는 퍼팅 꿀팁", "명랑골프")
    ],
    "soccer": [
        ("uK7K7qD4iLw", "손흥민 미친 원더골 다시보기 #손흥민 #토트넘", "풋볼매거진"),
        ("3eN9i4gW2kI", "축구 1대1 돌파할 때 가장 잘 통하는 개인기", "싸커스킬스"),
        ("bL0i9kE7w2Y", "조기축구에서 호날두 빙의하는 슛팅 꿀팁", "축구마스터"),
        ("8hK3nL9vW1e", "수비수 바보 만드는 3초 턴 동작", "풋볼크리에이티브")
    ],
    "camping": [
        ("nE4kO9pL2vY", "나 혼자 떠나는 감성 우중 차박 캠핑", "캠핑로그"),
        ("9iL2bW8eN4k", "다이소 캠핑 꿀템 TOP 5 이거 꼭 사세요", "캠핑연구소"),
        ("vW3nK8oL2bE", "텐트 3분만에 혼자 치는 법 (초보 필독)", "솔로캠퍼"),
        ("2eB7nL3wO9k", "캠핑장 가서 먹으면 극락 가는 꿀조합 요리", "캠핑식탁")
    ],
    "music": [
        ("AgZzx8GTsDg", "인기 급상승 아이돌 쇼츠 키비츠 힙합댄스", "하2남 스타디움"),
        ("YwPxl1M09l4", "아이유 노래 커버 레전드 고음 폭발", "뮤직라이브"),
        ("7hK2bL9nO3w", "요즘 틱톡 난리난 챌린지 댄스 숏폼", "케이팝댄스"),
        ("9wE3kL7bO2n", "피아노 10분만에 뉴진스 노래 치는 법", "피아노이지")
    ],
    "game": [
        ("8vW2nK9eL3b", "롤 챌린저가 알려주는 티어 올리는 3초 꿀팁", "롤선생"),
        ("3bE9kO2nL8w", "배틀그라운드 반동 0으로 만드는 마우스 설정", "배그마스터"),
        ("7nL2wO9eK3b", "마인크래프트 99%가 모르는 숨겨진 이스터에그", "마크연구소"),
        ("1kO8wE2bN9L", "발로란트 에임 헤드라인 잡는 연습법", "FPS클리닉")
    ],
    "car": [
        ("2bN9kO3wE7L", "자동차 세차할 때 절대 하면 안 되는 치명적 실수", "모터리뷰"),
        ("8eL2wO9nK3b", "중고차 살 때 침수차 구별하는 3초 꿀팁", "카마스터"),
        ("5wE9bK2nL8O", "테슬라 타면서 가장 유용한 숨은 꿀기능", "EV월드"),
        ("4nK3bL9wO2e", "고속도로 연비 2배 뽑는 운전 습관", "드라이브랩")
    ]
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for domain, items in candidates.items():
    print(f"Testing domain: {domain}")
    for vid, title, author in items:
        url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=3) as res:
                data = json.loads(res.read().decode('utf-8'))
                print(f"  [OK] {vid}: {data.get('title')}")
        except Exception as e:
            print(f"  [FAIL] {vid}: {e}")
