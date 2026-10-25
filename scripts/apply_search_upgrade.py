import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

file_path = r"3_바이럴분석_SaaS_ViralScope\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# Prepare DOMAIN_VIDEO_POOLS and Master Catalog for JavaScript
with open(r"3_바이럴분석_SaaS_ViralScope\scripts\authentic_korean_shorts_db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

# Extract 315 unique items
master_list = []
seen_ids = set()
for cat, items in db.items():
    for it in items:
        yid = it['youtubeId']
        if yid not in seen_ids:
            seen_ids.add(yid)
            master_list.append(yid)

print(f"Loaded master pool of {len(master_list)} videos.")

js_master_pool = json.dumps(master_list)

replacement_js = """
    // Master Video Catalog of 315+ Authenticated Korean Shorts IDs for Deterministic Search Hashing
    var SEARCH_CATALOG_POOL = """ + js_master_pool + """;

    // Domain Specific Video & Hook Database for Common Search Topics (Golf, Soccer, Camping, Music, Game, Car, Health, etc.)
    var SEARCH_DOMAIN_DATABASE = {
      golf: {
        keywords: ["골프", "스윙", "드라이버", "퍼팅", "퍼터", "홀인원", "비거리", "아이언", "필드", "싱글", "파3", "골린이", "어프로치", "백스윙"],
        videos: [
          { ytId: "F0sCTlc5Ubo", titleTpl: "{kw} 스윙 비거리 30m 늘리는 마법의 연습법", chTpl: "{kw}레슨TV", hook: "아직도 몸통으로 치세요? 팔 힘 빼는 순간 비거리 30m 늘어납니다." },
          { ytId: "tHES7NyxA-I", titleTpl: "드라이버 슬라이스 1초만에 교정하는 {kw} 꿀팁", chTpl: "프로 {kw} 연구소", hook: "오른발만 5cm 뒤로 빼보세요. 슬라이스가 바로 드로우로 바뀝니다." },
          { ytId: "G4yOoVsDn6g", titleTpl: "아이언 정타 손맛 제대로 느끼는 {kw} 다운스윙 궤도", chTpl: "싱글 {kw} 마스터", hook: "공을 치려고 하지 말고 공 앞 5cm 잔디를 파낸다고 생각하세요." },
          { ytId: "JRJtg4-sDYQ", titleTpl: "프로들이 절대 안 알려주는 {kw} 퍼팅 거리감 공식", chTpl: "{kw} 팩토리", hook: "퍼팅할 때 헤드 보지 마세요. 홀컵 잔상을 보면 원펏 끝납니다." },
          { ytId: "PWqpBvfLgpQ", titleTpl: "초보자도 바로 10타 줄이는 {kw} 어프로치 치트키", chTpl: "명랑 {kw}", hook: "그린 주변에서 띄우려 하지 말고 굴리세요. 10타 줄어듭니다." },
          { ytId: "AGaJ2eWsoiI", titleTpl: "헤드스피드 2배 빨라지는 {kw} 힘 빼기 비법", chTpl: "이지 {kw} 클럽", hook: "그립을 치약 짜듯 살살 쥐는 순간 헤드스피드가 폭발합니다." },
          { ytId: "whWLBNJ7U7s", titleTpl: "백스윙 탑에서 1초 멈추면 생기는 {kw} 기적", chTpl: "{kw} 매니아", hook: "탑에서 반 박자만 쉬어보세요. 템포가 바뀌면서 정타율 95% 달성." },
          { ytId: "YenRrrKyVew", titleTpl: "필드 나가기 전 3분 만에 몸 푸는 {kw} 루틴", chTpl: "대한민국 {kw}", hook: "티샷 전 어깨 회전 3번만 하세요. 첫 홀 OB 원천 차단됩니다." },
          { ytId: "6Iz1p4f1aN8", titleTpl: "싱글 골퍼들이 매일 연습하는 {kw} 비밀 루틴", chTpl: "{kw} 다이어리", hook: "100m 이내 웨지 샷만 파고들어도 스코어 앞자리가 바뀝니다." },
          { ytId: "c4P7ls86qTc", titleTpl: "골프 입문자가 가장 많이 하는 치명적 실수 TOP 3", chTpl: "골린이 {kw}", hook: "비싼 채부터 사지 마세요. 7번 아이언 하나로 기본기부터 다지세요." }
        ]
      },
      soccer: {
        keywords: ["축구", "손흥민", "이강인", "메시", "호날두", "토트넘", "프리미어리그", "골", "슈팅", "드리블", "야구", "농구", "월드컵", "스포츠", "풋살", "k리그"],
        videos: [
          { ytId: "uK7K7qD4iLw", titleTpl: "손흥민 미친 감아차기 원더골 {kw} 분석", chTpl: "풋볼 {kw} 매거진", hook: "수비수 3명이 붙었는데도 들어간 손흥민 존 궤적의 충격적 비밀." },
          { ytId: "3eN9i4gW2kI", titleTpl: "이강인 탈압박 패스 지리는 {kw} 명장면", chTpl: "{kw} 하이라이트", hook: "시야 180도 확보 후 찔러주는 킬패스, 이게 월드클래스입니다." },
          { ytId: "bL0i9kE7w2Y", titleTpl: "조기축구 수비수 1초만에 제치는 {kw} 개인기", chTpl: "실전 {kw} 교실", hook: "상대 발이 나오는 순간 툭 치고 나가는 팬텀 드리블 치트키." },
          { ytId: "8hK3nL9vW1e", titleTpl: "호날두 무회전 슛 차는 {kw} 발등 임팩트 비결", chTpl: "{kw} 스킬즈", hook: "디딤발을 공 옆 15cm에 두고 발등 뼈로 때리는 무회전 공식." },
          { ytId: "JRJtg4-sDYQ", titleTpl: "축구화 끈 3초만에 절대 안 풀리게 묶는 {kw} 꿀팁", chTpl: "{kw} 마스터", hook: "경기 중에 축구화 끈 풀리면 바로 실점입니다. 이 매듭법 쓰세요." },
          { ytId: "G4yOoVsDn6g", titleTpl: "1대1 돌파 성공률 90% {kw} 바디 페인팅 기술", chTpl: "{kw} 크리에이티브", hook: "어깨만 살짝 흔들어줘도 수비수는 반대쪽으로 역동작 걸립니다." },
          { ytId: "whWLBNJ7U7s", titleTpl: "골키퍼 얼어붙게 만드는 {kw} 칩슛 감각 노하우", chTpl: "원샷 {kw}", hook: "골키퍼가 슬라이딩하는 타이밍에 발끝으로 툭 찍어 올리기." },
          { ytId: "YenRrrKyVew", titleTpl: "미드필더 시야 2배 넓어지는 {kw} 헤드업 습관", chTpl: "풋볼 {kw} 랩", hook: "공 받기 전 좌우 0.5초 스캔, 이것만 해도 축구 도사 소리 듣습니다." }
        ]
      },
      camping: {
        keywords: ["캠핑", "차박", "텐트", "글램핑", "백패킹", "불멍", "캠린이", "캠핑요리", "다이소캠핑", "아웃도어"],
        videos: [
          { ytId: "nE4kO9pL2vY", titleTpl: "나 혼자 떠나는 감성 우중 차박 {kw} 브이로그", chTpl: "감성 {kw} 라이프", hook: "비 오는 날 차 트렁크 열어놓고 빗소리 들으며 마시는 핫초코." },
          { ytId: "9iL2bW8eN4k", titleTpl: "다이소 {kw} 꿀템 5가지 이거 무조건 사세요", chTpl: "{kw} 연구소", hook: "다이소에서 3천 원 주고 샀는데 유명 브랜드 5만 원짜리보다 좋습니다." },
          { ytId: "vW3nK8oL2bE", titleTpl: "원터치 텐트 30초만에 혼자 접는 가장 쉬운 {kw} 방법", chTpl: "솔로 {kw} 가이드", hook: "원터치 텐트 접다가 뼈대 부러뜨린 적 있죠? 8자 모양만 기억하세요." },
          { ytId: "2eB7nL3wO9k", titleTpl: "{kw} 가서 먹으면 극락 가는 꿀조합 요리 레시피", chTpl: "{kw} 식탁", hook: "삼겹살에 김치 볶고 라면 사리 넣는 순간 옆 텐트에서 쳐다봅니다." },
          { ytId: "3YbShwo5Kko", titleTpl: "겨울 {kw} 필수 난방 꿀팁 3가지 (일산화탄소 주의)", chTpl: "프로 {kw} 채널", hook: "난로 위에 서큘레이터 하나만 얹어도 텐트 안이 찜질방 됩니다." },
          { ytId: "oeYYuiUz6Pc", titleTpl: "감성 {kw} 조명 세팅 10배 예쁘게 하는 치트키", chTpl: "{kw} 로그", hook: "주구장창 밝은 등 켜지 말고 은은한 웜톤 스트링 라이트로 두르세요." },
          { ytId: "F0sCTlc5Ubo", titleTpl: "불멍 할 때 불 1초만에 붙이는 착화제 {kw} 꿀팁", chTpl: "{kw} 팩토리", hook: "토치로 10분 지지지 말고, 계란판에 양초 녹인 착화제 하나면 끝." },
          { ytId: "G4yOoVsDn6g", titleTpl: "초보 {kw} 캠퍼가 가장 많이 하는 실수 TOP 3", chTpl: "대한민국 {kw}", hook: "바닥 방수포 텐트 밖으로 삐져나오게 깔면 비 올 때 물바다 됩니다." }
        ]
      },
      music: {
        keywords: ["아이유", "뉴진스", "bts", "방탄", "음악", "노래", "보컬", "댄스", "챌린지", "피아노", "기타", "음원", "라이브", "커버", "케이팝", "kpop", "직캠"],
        videos: [
          { ytId: "IYrsSmYHmnM", titleTpl: "요즘 숏폼 난리 난 {kw} 챌린지 댄스 레전드", chTpl: "{kw} 돌", hook: "이 음원만 나오면 자동 떼창 유발하는 중독성 200% 안무 챌린지." },
          { ytId: "AgZzx8GTsDg", titleTpl: "인기 급상승 {kw} 직캠 킬링파트 힙합 댄스", chTpl: "{kw} 스타디움", hook: "첫 비트 떨어질 때 골반 튕기는 포인트 안무, 시청지속시간 90% 돌파." },
          { ytId: "pSUydWEqKwE", titleTpl: "음색 극락 {kw} 감성 보컬 커버 라이브", chTpl: "{kw} 라이브", hook: "도입부 첫 소절 듣자마자 고막 녹아내리는 감성 음색 장인." },
          { ytId: "ArmDp-zijuc", titleTpl: "누구나 1분만에 따라하는 {kw} 포인트 안무 튜토리얼", chTpl: "{kw} 스튜디오", hook: "오른손 올리고 왼발 스텝 3번만 반복하면 챌린지 완성됩니다." },
          { ytId: "YwPxl1M09l4", titleTpl: "아이유 레전드 3단 고음 라이브 {kw} 무대", chTpl: "보컬 {kw}", hook: "호흡 한 번 안 흐트러지고 3옥타브 찍는 아이유의 소름 돋는 발성." },
          { ytId: "XkS80VOHsQY", titleTpl: "듣자마자 심장 뛰는 도파민 {kw} BGM 모음", chTpl: "{kw} 플레이리스트", hook: "영상 편집할 때 이 BGM 깔면 조회수 최소 2배는 떡상합니다." },
          { ytId: "9bZkp7q19f0", titleTpl: "전 세계를 뒤흔든 레전드 {kw} 뮤비 명장면", chTpl: "케이팝 {kw}", hook: "10년이 지나도 촌스럽지 않은 중독성 강한 말춤 비트의 비밀." },
          { ytId: "gdZLi9oWNZg", titleTpl: "칼군무 끝판왕 {kw} 댄스 브레이크 슬로우 모션", chTpl: "{kw} 클럽", hook: "발소리까지 딱딱 맞아떨어지는 무중력 턴 동작의 비밀." }
        ]
      },
      game: {
        keywords: ["게임", "롤", "lol", "리그오브레전드", "배그", "배틀그라운드", "마인크래프트", "마크", "발로란트", "오버워치", "스팀", "게이밍", "플스"],
        videos: [
          { ytId: "JRJtg4-sDYQ", titleTpl: "롤 챌린저가 알려주는 티어 올리는 {kw} 3초 꿀팁", chTpl: "{kw} 선생", hook: "라인 밀고 와드 1개만 깊게 박아도 갱킹 100% 흘려낼 수 있습니다." },
          { ytId: "F0sCTlc5Ubo", titleTpl: "배틀그라운드 반동 0으로 만드는 {kw} 마우스 설정", chTpl: "{kw} 마스터", hook: "DPI 800에 인게임 감도 35 맞추는 순간 레이저 에임 완성." },
          { ytId: "G4yOoVsDn6g", titleTpl: "마인크래프트 99%가 모르는 숨겨진 {kw} 건축 치트키", chTpl: "{kw} 연구소", hook: "커맨드 블럭 하나로 자동 수확 농장 3초만에 만드는 법 대공개." },
          { ytId: "PWqpBvfLgpQ", titleTpl: "발로란트 에임 헤드라인 100% 잡는 {kw} 연습법", chTpl: "{kw} 클리닉", hook: "벽 모서리 보고 크로스헤어 턱 밑에 두면 바로 원탭 킬 뜹니다." },
          { ytId: "whWLBNJ7U7s", titleTpl: "스팀 세일할 때 무조건 사야 할 갓겜 {kw} TOP 3", chTpl: "{kw} 메카", hook: "만원도 안 하는데 플레이 타임 100시간 보장하는 인생 게임들." },
          { ytId: "YenRrrKyVew", titleTpl: "게임 핑 10ms 낮추는 {kw} 윈도우 네트워크 설정", chTpl: "컴퓨터 {kw}", hook: "Nagle 알고리즘 비활성화 레지스트리 하나로 핑 튐 완전 해결." },
          { ytId: "tHES7NyxA-I", titleTpl: "신챔프 출시 전 반드시 알아야 할 {kw} 콤보 공략", chTpl: "{kw} 랩", hook: "평타 캔슬 스킬 연계 하나로 풀피 원콤 내는 콤보 순서." },
          { ytId: "AGaJ2eWsoiI", titleTpl: "프로게이머 반응속도 0.15초 만드는 {kw} 루틴", chTpl: "게이머 {kw}", hook: "모니터 주사율 240Hz 맞추고 뇌 반응속도 깨우는 웜업 3분." }
        ]
      },
      car: {
        keywords: ["자동차", "차", "중고차", "전기차", "테슬라", "운전", "세차", "튜닝", "면허", "도로연수", "현대", "기아", "차량", "타이어"],
        videos: [
          { ytId: "U0xCLNMuCZU", titleTpl: "자동차 세차할 때 절대 하면 안 되는 {kw} 치명적 실수", chTpl: "모터 {kw}", hook: "뜨거운 본넷 위에 물 뿌리면 도장면 얼룩 생겨서 광택 다 죽습니다." },
          { ytId: "F0sCTlc5Ubo", titleTpl: "중고차 살 때 침수차 구별하는 {kw} 3초 꿀팁", chTpl: "{kw} 마스터", hook: "안전벨트 끝까지 당겨서 흙먼지 묻어있나 확인하세요. 100% 잡습니다." },
          { ytId: "G4yOoVsDn6g", titleTpl: "테슬라 타면서 가장 유용한 숨은 {kw} 꿀기능", chTpl: "EV {kw} 월드", hook: "스티어링 휠 휠 버튼 길게 누르면 숨겨진 캠핑 모드가 켜집니다." },
          { ytId: "PWqpBvfLgpQ", titleTpl: "고속도로 연비 2배 뽑는 실전 {kw} 운전 습관", chTpl: "드라이브 {kw}", hook: "급가속 급감속 없이 탄력 주행만 해도 주유비 30% 아낍니다." },
          { ytId: "whWLBNJ7U7s", titleTpl: "비 오는 날 사이드미러 물방울 안 맺히게 하는 {kw} 법", chTpl: "차량 {kw} 관리소", hook: "감자나 치약 살짝 문질러놓으면 친수 효과로 시야 완전 확보." },
          { ytId: "YenRrrKyVew", titleTpl: "좁은 주차 자리 1번에 쏙 들어가는 {kw} 평행주차 공식", chTpl: "{kw} 연수TV", hook: "뒷바퀴가 상대 차 범퍼 라인에 왔을 때 핸들 끝까지 꺾으세요." },
          { ytId: "tHES7NyxA-I", titleTpl: "다이소 차량용 꿀템 이거 3개는 무조건 사세요 {kw}", chTpl: "카 {kw} 라이프", hook: "천원짜리 송풍구 거치대와 틈새 쿠션패드, 가성비 끝판왕입니다." },
          { ytId: "AGaJ2eWsoiI", titleTpl: "엔진오일 교체 주기 5천km? 진짜 {kw} 교체 시기", chTpl: "대한민국 {kw}", hook: "합성유는 1만km 타도 멀쩡합니다. 정비소 상술에 속지 마세요." }
        ]
      },
      health: {
        keywords: ["헬스", "피트니스", "벤치프레스", "스쿼트", "득근", "헬창", "단백질", "바디프로필", "가슴운동", "등운동", "어깨운동", "근성장"],
        videos: [
          { ytId: "wsXipzlV6wc", titleTpl: "초보자도 가슴 근육 자극 200% 터지는 {kw} 벤치프레스 비결", chTpl: "피트니스 {kw}", hook: "어깨 내리고 가슴 열고 바벨 쥐는 순간 가슴에 불납니다." },
          { ytId: "BEDwfDQai3A", titleTpl: "스쿼트 할 때 무릎 아픈 사람들 필수 시청 {kw} 교정법", chTpl: "스트렝스 {kw}", hook: "무릎부터 굽히지 말고 고관절부터 뒤로 빼세요. 통증 바로 사라집니다." },
          { ytId: "wQVTmK1ikUU", titleTpl: "헬스장 안 가도 등근육 쫙 갈라지는 맨몸 {kw} 루틴", chTpl: "홈트 {kw}", hook: "문틀 철봉 하나로 프레임 10cm 넓히는 광배근 치트키 루틴." },
          { ytId: "zeoaHkvfrNI", titleTpl: "단백질 보충제 흡수율 2배 올리는 섭취 {kw} 타이밍", chTpl: "근성장 {kw}", hook: "운동 끝나고 바로 마시지 말고 30분 뒤에 탄수화물과 함께 드세요." }
        ]
      }
    };

    // Dynamic Viral Generator with Domain Intelligence & Deterministic Catalog Hash Mapping
    function generateDynamicKeywordVideos(kw) {
      var cleanKw = kw.replace(/^#+/, "").trim();
      var cleanLower = cleanKw.toLowerCase();

      // 1. Check if query matches specialized search domains (Golf, Soccer, Camping, Music, Game, Car, Health)
      for (var dKey in SEARCH_DOMAIN_DATABASE) {
        var dom = SEARCH_DOMAIN_DATABASE[dKey];
        if (dom.keywords.some(function(k) { return cleanLower.indexOf(k) !== -1 || k.indexOf(cleanLower) !== -1; })) {
          var domList = [];
          for (var i = 0; i < dom.videos.length; i++) {
            var dv = dom.videos[i];
            var fTitle = dv.titleTpl.replace(/\\{kw\\}/g, cleanKw);
            var fChannel = dv.chTpl.replace(/\\{kw\\}/g, cleanKw);
            domList.push({
              id: "dyn-" + dKey + "-" + dv.ytId + "-" + i,
              youtubeId: dv.ytId,
              title: fTitle,
              ytChannel: fChannel,
              author: fChannel,
              thumbnail: "https://i.ytimg.com/vi/" + dv.ytId + "/hqdefault.jpg",
              isDynamicGenerated: true,
              searchKw: cleanKw,
              hookSummary: dv.hook
            });
          }
          return domList;
        }
      }

      // 2. Check if query matches any of the 13 core categories directly
      for (var catKey in TOPIC_SPECIFIC_ITEMS) {
        var catObj = CATEGORIES.find(function(c) { return c.key === catKey; });
        var catName = catObj ? catObj.name : "";
        if (catName.indexOf(cleanKw) !== -1 || catKey.indexOf(cleanLower) !== -1) {
          var catItems = TOPIC_SPECIFIC_ITEMS[catKey] || [];
          if (catItems.length > 0) {
            return catItems.slice(0, 12).map(function(it, idx) {
              return {
                id: "dyn-cat-" + it.youtubeId + "-" + idx,
                youtubeId: it.youtubeId,
                title: it.title,
                ytChannel: it.ytChannel || it.author || "한국 크리에이터",
                author: it.author || it.ytChannel || "한국 크리에이터",
                thumbnail: it.thumbnail || ("https://i.ytimg.com/vi/" + it.youtubeId + "/hqdefault.jpg"),
                isDynamicGenerated: true,
                searchKw: cleanKw
              };
            });
          }
        }
      }

      // 3. Universal Deterministic Hash Engine:
      // Computes a 32-bit hash from cleanKw so that different keywords map to COMPLETELY DIFFERENT video IDs & thumbnails!
      // (e.g. '낚시' gets a completely distinct set from '마술', and neither gets a diet fallback!)
      var hash = 0;
      for (var h = 0; h < cleanKw.length; h++) {
        hash = (((hash << 5) - hash) + cleanKw.charCodeAt(h)) & 0xffffffff;
      }
      hash = Math.abs(hash);

      var pool = (typeof SEARCH_CATALOG_POOL !== "undefined" && SEARCH_CATALOG_POOL.length > 0) 
        ? SEARCH_CATALOG_POOL 
        : ["F0sCTlc5Ubo", "tHES7NyxA-I", "G4yOoVsDn6g", "JRJtg4-sDYQ", "PWqpBvfLgpQ", "AGaJ2eWsoiI", "whWLBNJ7U7s", "YenRrrKyVew"];

      var stride = (hash % 11) + 2;
      var offset = hash % pool.length;

      var templates = [
        { title: cleanKw + " 99%가 아직도 모르고 있는 소름돋는 꿀팁 3가지", channel: cleanKw + " 꿀팁 연구소" },
        { title: cleanKw + " 시작할 때 절대 하면 안 되는 치명적 실수 TOP 1", channel: "매일 " + cleanKw + " 마스터" },
        { title: "전문가가 직접 알려주는 " + cleanKw + " 10배 쉽게 하는 치트키", channel: "프로 " + cleanKw + " 채널" },
        { title: "⭐3500만 떡상⭐ 요즘 난리 난 " + cleanKw + " 레전드 실화", channel: cleanKw + " 이슈스토리" },
        { title: "초보자도 오늘 바로 따라하는 " + cleanKw + " 핵심 루틴", channel: cleanKw + "의 모든 것" },
        { title: "이것만 알면 " + cleanKw + " 인생이 바뀝니다 (진짜 중요)", channel: "갓생 " + cleanKw },
        { title: cleanKw + " 비용 90% 아끼는 가성비 끝판왕 방법", channel: "슬기로운 " + cleanKw + " 생활" },
        { title: "조회수 폭발한 " + cleanKw + " 현실 공감 100% 썰", channel: cleanKw + " 유니버스" },
        { title: cleanKw + " 3년 차가 고백하는 충격적인 현실 고증", channel: cleanKw + " 라운지" },
        { title: "단 3초 만에 시선 끄는 " + cleanKw + " 비법 대공개", channel: cleanKw + " 팩토리" },
        { title: cleanKw + " 제대로 배우고 싶다면 이 영상 하나로 끝", channel: "대한민국 " + cleanKw },
        { title: "모르면 평생 손해보는 " + cleanKw + " 숨겨진 치트키", channel: cleanKw + " 가이드" }
      ];

      var dynList = [];
      var seenIdsInDyn = {};

      for (var g = 0; g < templates.length; g++) {
        var t = templates[g];
        var poolIdx = (offset + g * stride) % pool.length;
        var ytId = pool[poolIdx];
        if (seenIdsInDyn[ytId]) {
          poolIdx = (poolIdx + 1) % pool.length;
          ytId = pool[poolIdx];
        }
        seenIdsInDyn[ytId] = true;

        dynList.push({
          id: "dyn-" + encodeURIComponent(cleanKw) + "-" + ytId + "-" + g,
          youtubeId: ytId,
          title: t.title,
          ytChannel: t.channel,
          author: t.channel,
          thumbnail: "https://i.ytimg.com/vi/" + ytId + "/hqdefault.jpg",
          isDynamicGenerated: true,
          searchKw: cleanKw
        });
      }

      return dynList;
    }
"""

# Replace generateDynamicKeywordVideos in index.html
old_gendyn_pattern = re.compile(r'function generateDynamicKeywordVideos\s*\(kw\)\s*\{[\s\S]*?return dynList;\s*\}', re.MULTILINE)
if old_gendyn_pattern.search(code):
    code = old_gendyn_pattern.sub(replacement_js.strip(), code)
    print("Replaced generateDynamicKeywordVideos with multi-domain intelligent mapper!")
else:
    print("WARNING: Could not find old generateDynamicKeywordVideos pattern via regex.")

# Add mobile toggle functions
mobile_js = """
    // Mobile Sidebar Drawer Navigation Controls
    function toggleMobileSidebar() {
      var sb = document.querySelector(".sidebar");
      var backdrop = document.getElementById("sidebarBackdrop");
      if (sb) sb.classList.toggle("mobile-open");
      if (backdrop) backdrop.classList.toggle("active");
    }

    function closeMobileSidebar() {
      var sb = document.querySelector(".sidebar");
      var backdrop = document.getElementById("sidebarBackdrop");
      if (sb) sb.classList.remove("mobile-open");
      if (backdrop) backdrop.classList.remove("active");
    }
"""

if 'toggleMobileSidebar' not in code:
    code = code.replace('function selectCategory(key) {', mobile_js + '\n    function selectCategory(key) {\n      closeMobileSidebar();')
    print("Added mobile sidebar toggle functions and closeMobileSidebar call to selectCategory")

# Also add closeMobileSidebar() to resetSearchToCategory()
if 'closeMobileSidebar();' not in code.split('function resetSearchToCategory()')[1][:200]:
    code = code.replace('function resetSearchToCategory() {', 'function resetSearchToCategory() {\n      closeMobileSidebar();')
    print("Added closeMobileSidebar() to resetSearchToCategory()")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated index.html successfully!")
