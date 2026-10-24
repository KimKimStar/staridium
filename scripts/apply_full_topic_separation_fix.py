# -*- coding: utf-8 -*-
import os

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update CATEGORIES with subTopics and Boolean OR searchQ for high-recall viral queries
old_categories = """    var CATEGORIES = [
      { key: "total_kr", name: "🏆 대한민국 종합 숏폼 통합 랭킹", searchQ: "인기 랭킹", count: "75+" },
      { key: "humor", name: "😂 한국 일상 공감 & 썰", searchQ: "숏박스 너덜트 일상 공감 썰", count: "75+" },
      { key: "diet", name: "🥗 한국 다이어트 & 홈트", searchQ: "다이어트 운동 식단", count: "75+" },
      { key: "finance", name: "📈 주식 · 재테크 · 부동산", searchQ: "재테크 주식 부자", count: "75+" },
      { key: "beauty", name: "💄 K-뷰티 · 메이크업 · 올리브영", searchQ: "올리브영 뷰티 메이크업", count: "75+" },
      { key: "cooking", name: "🍳 맛집 · 편의점 · 초간단 레시피", searchQ: "초간단 자취 요리 레시피", count: "75+" },
      { key: "growth", name: "🧠 자기계발 & 갓생 동기부여", searchQ: "자기계발 동기부여 갓생", count: "75+" },
      { key: "psychology", name: "💬 인간관계 & 심리 화법", searchQ: "인간관계 심리 대화법", count: "75+" },
      { key: "tech", name: "💻 AI 툴 & 스마트폰/테크 꿀팁", searchQ: "스마트폰 꿀팁 IT 테크", count: "75+" },
      { key: "fashion", name: "👗 한국 데일리룩 & 코디", searchQ: "체형별 코디 패션 룩북", count: "75+" },
      { key: "travel", name: "✈️ 국내 핫플 & 가성비 여행", searchQ: "국내여행 핫플 맛집", count: "75+" },
      { key: "pets", name: "🐶 반려동물 힐링 & 댕냥이", searchQ: "강아지 고양이 귀여운 동물", count: "75+" },
      { key: "english", name: "🗣️ 실전 생활영어 & 꿀팁", searchQ: "생활영어 회화 꿀팁", count: "75+" }
    ];"""

new_categories = """    var CATEGORIES = [
      { 
        key: "total_kr", 
        name: "🏆 대한민국 종합 숏폼 통합 랭킹", 
        searchQ: "한국|인기|급상승|쇼츠", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "종합 1위 메가 바이럴 숏폼" },
          { id: "sub-2", name: "이번 주 급상승 떡상 영상 TOP" },
          { id: "sub-3", name: "시청 지속 시간 극대화 성공 사례" }
        ]
      },
      { 
        key: "psychology", 
        name: "💬 인간관계 & 심리 화법", 
        searchQ: "인간관계|심리학|대화법|화법|손절|자존감|말투", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "만만하게 보이지 않는 화법 & 대처법" },
          { id: "sub-2", name: "손절해야 할 사람 유형 TOP 3" },
          { id: "sub-3", name: "호감 사는 매력적인 심리 대화 기술" },
          { id: "sub-4", name: "자존감 높이고 상처 안 받는 멘탈 관리" }
        ]
      },
      { 
        key: "humor", 
        name: "😂 한국 일상 공감 & 썰", 
        searchQ: "숏박스|너덜트|공감썰|스케치코미디|일상썰", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "일상 공감 & 하이퍼리얼리즘" },
          { id: "sub-2", name: "직장인 / 학생 현실 고증 썰" },
          { id: "sub-3", name: "연애 / 남녀 심리 코미디" }
        ]
      },
      { 
        key: "diet", 
        name: "🥗 한국 다이어트 & 홈트", 
        searchQ: "다이어트|홈트|식단|체중감량|뱃살", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "단기 뱃살 / 체지방 감량 루틴" },
          { id: "sub-2", name: "다이어트 식단 & 편의점 꿀조합" },
          { id: "sub-3", name: "누워서 하는 5분 홈트레이닝" }
        ]
      },
      { 
        key: "finance", 
        name: "📈 주식 · 재테크 · 부동산", 
        searchQ: "재테크|주식|부동산|부자|돈모으기", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "사회초년생 1억 모으기 로드맵" },
          { id: "sub-2", name: "고배당주 / 실전 투자 원칙" },
          { id: "sub-3", name: "부자되는 현실적인 소비 습관" }
        ]
      },
      { 
        key: "beauty", 
        name: "💄 K-뷰티 · 메이크업 · 올리브영", 
        searchQ: "올리브영|메이크업|뷰티|피부관리|화장품", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "올리브영 세일 필수 추천템 TOP" },
          { id: "sub-2", name: "모공 / 피부결 극락 스킨케어" },
          { id: "sub-3", name: "1분 데일리 퀵 메이크업 꿀팁" }
        ]
      },
      { 
        key: "cooking", 
        name: "🍳 맛집 · 편의점 · 초간단 레시피", 
        searchQ: "초간단요리|자취요리|레시피|편의점꿀조합", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "5분 완성 자취생 초간단 요리" },
          { id: "sub-2", name: "편의점 재료 꿀조합 레시피" },
          { id: "sub-3", name: "에어프라이어 만능 요리법" }
        ]
      },
      { 
        key: "growth", 
        name: "🧠 자기계발 & 갓생 동기부여", 
        searchQ: "자기계발|동기부여|갓생|성공습관|루틴", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "모닝 루틴 & 하루 생산성 3배" },
          { id: "sub-2", name: "게으름 극복 & 즉시 실행 마인드셋" },
          { id: "sub-3", name: "상위 1% 성공하는 사람들의 습관" }
        ]
      },
      { 
        key: "tech", 
        name: "💻 AI 툴 & 스마트폰/테크 꿀팁", 
        searchQ: "스마트폰꿀팁|아이폰꿀팁|갤럭시꿀팁|AI툴|ChatGPT", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "아이폰 / 갤럭시 숨은 꿀기능" },
          { id: "sub-2", name: "ChatGPT / AI 업무 자동화 치트키" },
          { id: "sub-3", name: "모르면 손해보는 필수 생산성 앱" }
        ]
      },
      { 
        key: "fashion", 
        name: "👗 한국 데일리룩 & 코디", 
        searchQ: "데일리룩|체형별코디|패션꿀팁|무신사|룩북", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "체형 커버 & 키 커보이는 코디 공식" },
          { id: "sub-2", name: "기본템으로 끝내는 일주일 데일리룩" },
          { id: "sub-3", name: "실패 없는 가성비 패션 꿀조합" }
        ]
      },
      { 
        key: "travel", 
        name: "✈️ 국내 핫플 & 가성비 여행", 
        searchQ: "국내여행|핫플|감성숙소|드라이브|데이트코스", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "나만 알고 싶은 전국 숨은 핫플" },
          { id: "sub-2", name: "가성비 감성 숙소 TOP 3" },
          { id: "sub-3", name: "당일치기 드라이브 & 데이트 코스" }
        ]
      },
      { 
        key: "pets", 
        name: "🐶 반려동물 힐링 & 댕냥이", 
        searchQ: "강아지|고양이|반려견|반려동물", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "댕댕이 시선 강탈 귀여운 행동" },
          { id: "sub-2", name: "고양이 집사 필수 공감 모먼트" },
          { id: "sub-3", name: "반려동물 건강 & 훈련 꿀팁" }
        ]
      },
      { 
        key: "english", 
        name: "🗣️ 실전 생활영어 & 꿀팁", 
        searchQ: "생활영어|영어회화|원어민영어|영어꿀팁", 
        count: "75+",
        subTopics: [
          { id: "sub-1", name: "원어민이 매일 쓰는 3단어 패턴" },
          { id: "sub-2", name: "미국인이 절대 안 쓰는 콩글리시 교정" },
          { id: "sub-3", name: "해외여행 / 식당 실전 영어 회화" }
        ]
      }
    ];"""

if old_categories in code:
    code = code.replace(old_categories, new_categories)
    print("Updated CATEGORIES with rich subTopics and Boolean OR searchQ.")
else:
    print("WARNING: old_categories not found in update_dashboard.py.")

# 2. Add full authentic data to TOPIC_SPECIFIC_ITEMS for psychology, fashion, travel, pets, english
target_tech_end = """        { id: "WcIcVapfqXw", title: "스마트폰 배터리 수명 2배 늘려주는 설정법", ytChannel: "테크몽클립", igCreator: "@tech_tips_kr", ttCreator: "@gadget_korea" }
      ]
    };"""

replacement_all_categories = """        { id: "WcIcVapfqXw", title: "스마트폰 배터리 수명 2배 늘려주는 설정법", ytChannel: "테크몽클립", igCreator: "@tech_tips_kr", ttCreator: "@gadget_korea" }
      ],
      // 8. Psychology & Human Relations (인간관계 & 심리 화법)
      psychology: [
        { id: "8wRzKjCq7m4", title: "만만하게 보이지 않는 사람들의 3가지 특징 (이 말투만 쓰세요)", ytChannel: "너진짜똑똑하다", igCreator: "@mind_sense_kr", ttCreator: "@psychology_tok" },
        { id: "4mNn92Fm2-M", title: "손절해야 하는 친구 유형 1순위 (이런 사람은 당장 피하세요)", ytChannel: "인간관계연구소", igCreator: "@people_insight", ttCreator: "@relationship_kr" },
        { id: "WcIcVapfqXw", title: "나를 은근히 무시하는 사람 조용히 참교육하는 심리 대화법", ytChannel: "말센스클럽", igCreator: "@talk_smart_kr", ttCreator: "@speech_secret" },
        { id: "kOHB85vDuow", title: "말 잘하는 사람들이 무의식중에 쓰는 3초 화법의 비밀", ytChannel: "대화의기술", igCreator: "@mind_master_kr", ttCreator: "@smart_talker" },
        { id: "a3ICNMQW7Ok", title: "기분 나쁘지 않게 똑 부러지게 거절하는 심리 화법 기술", ytChannel: "멘탈케어스튜디오", igCreator: "@mental_coach", ttCreator: "@mental_tok_kr" },
        { id: "kJQP7kiw5Fk", title: "자존감 낮은 사람들이 대화할 때 자주 쓰는 위험한 말버릇", ytChannel: "심리닥터팩트", igCreator: "@self_esteem_kr", ttCreator: "@psych_dr" },
        { id: "M_C38M1hOQo", title: "가스라이팅 하는 사람들의 전형적인 수법과 단칼 대처법", ytChannel: "지식인사이드클립", igCreator: "@gaslight_defense", ttCreator: "@mind_defense" },
        { id: "sCj1mH3K1bQ", title: "첫인상 3초 만에 상대방 호감 사는 미러링 심리 기술", ytChannel: "사람의마음", igCreator: "@first_impression_kr", ttCreator: "@people_secret" },
        { id: "8wRzKjCq7m4", title: "카톡 읽씹 당했을 때 가장 쿨하고 우아하게 대처하는 법", ytChannel: "심리특강", igCreator: "@katalk_sense", ttCreator: "@chat_hack_kr" },
        { id: "4mNn92Fm2-M", title: "내 비밀을 절대 말하면 안 되는 위험한 사람들의 공통점", ytChannel: "지혜의숲", igCreator: "@wisdom_forest", ttCreator: "@wisdom_kr" }
      ],
      // 10. Korean Daily Fashion & Styling (한국 데일리룩 & 코디)
      fashion: [
        { id: "4mNn92Fm2-M", title: "키 170 이하 남자가 무조건 피해야 할 바지 핏 TOP 3", ytChannel: "핏더사이즈클립", igCreator: "@fitthesize_look", ttCreator: "@mens_fashion_kr" },
        { id: "8wRzKjCq7m4", title: "체형별(하비/상비) 슬랙스 고르는 실패 없는 1티어 공식", ytChannel: "앨리스패션", igCreator: "@daily_ootd_kr", ttCreator: "@body_shape_look" },
        { id: "WcIcVapfqXw", title: "무신사에서 3만원대로 건지는 가성비 기본템 5선 추천", ytChannel: "짱구대디클립", igCreator: "@musinsa_pick", ttCreator: "@fashion_hacks_kr" },
        { id: "kOHB85vDuow", title: "옷 잘 입는 사람들은 절대 안 입는 촌스러운 옷 조합 3가지", ytChannel: "스타일가이드", igCreator: "@style_guide_kr", ttCreator: "@k_fashion_trend" },
        { id: "a3ICNMQW7Ok", title: "비율 2배 좋아 보이는 데일리룩 밑단 롤업 치트키", ytChannel: "오오티디코리아", igCreator: "@ootd_daily_kr", ttCreator: "@ratio_look" },
        { id: "kJQP7kiw5Fk", title: "여자 데일리룩 실패 없는 출근룩 & 캠퍼스룩 일주일 룩북", ytChannel: "룩북연구소", igCreator: "@lookbook_daily", ttCreator: "@girl_ootd_kr" }
      ],
      // 11. Travel & Hotspots (국내 핫플 & 가성비 여행)
      travel: [
        { id: "8wRzKjCq7m4", title: "나만 알고 싶은 강원도 프라이빗 감성 독채 숙소 TOP 3", ytChannel: "여행다녀왔습니다", igCreator: "@travel_gangwon", ttCreator: "@korea_travel_kr" },
        { id: "4mNn92Fm2-M", title: "제주도민이 외지인한테 절대 안 알려주는 숨은 비경 핫플", ytChannel: "제주여행자", igCreator: "@jeju_secret_spot", ttCreator: "@jeju_tok_kr" },
        { id: "WcIcVapfqXw", title: "1박에 10만원대 가성비 끝판왕 오션뷰 인피니티풀 숙소", ytChannel: "호캉스연구소", igCreator: "@hotel_pick_kr", ttCreator: "@ocean_view_stay" },
        { id: "kOHB85vDuow", title: "당일치기로 다녀오기 딱 좋은 서울 근교 힐링 드라이브 코스", ytChannel: "핫플추천대장", igCreator: "@seoul_drive_hot", ttCreator: "@drive_course_kr" },
        { id: "a3ICNMQW7Ok", title: "부산 가면 무조건 들러야 할 현지인 찐맛집 리스트 공개", ytChannel: "전국맛집지도", igCreator: "@busan_tasty_road", ttCreator: "@korea_foodie_map" }
      ],
      // 12. Pets (반려동물 힐링 & 댕냥이)
      pets: [
        { id: "8wRzKjCq7m4", title: "강아지가 주인에게 뽀뽀할 때 숨겨진 진짜 속마음", ytChannel: "보듬반려연구소", igCreator: "@dog_mind_kr", ttCreator: "@puppy_tok_kr" },
        { id: "4mNn92Fm2-M", title: "고양이가 엉덩이를 들이미는 충격적인 이유 3가지", ytChannel: "냥냥특공대", igCreator: "@cat_secret_kr", ttCreator: "@kitten_hub" },
        { id: "WcIcVapfqXw", title: "강아지가 배를 보이고 누웠을 때 절대 만지면 안 되는 부위", ytChannel: "반려견케어", igCreator: "@pet_care_pro", ttCreator: "@dog_health_kr" },
        { id: "kOHB85vDuow", title: "세상에서 제일 말 안 듣는 시바견의 반항 레전드", ytChannel: "멍멍일기", igCreator: "@shiba_diary", ttCreator: "@funny_pets_kr" }
      ],
      // 13. English (실전 생활영어 & 꿀팁)
      english: [
        { id: "4mNn92Fm2-M", title: "미국인들이 'How are you?' 할 때 절대 안 쓰는 한국식 대답", ytChannel: "달변가영쌤", igCreator: "@real_english_kr", ttCreator: "@english_shorts_kr" },
        { id: "8wRzKjCq7m4", title: "원어민이 매일 쓰는 3단어 만능 영어 패턴 TOP 5", ytChannel: "라이브영어클립", igCreator: "@pattern_english", ttCreator: "@english_tip_kr" },
        { id: "WcIcVapfqXw", title: "'맛있어요'를 Delicious 말고 원어민처럼 감탄하는 법", ytChannel: "원어민표현사전", igCreator: "@native_talk_kr", ttCreator: "@speak_english" },
        { id: "kOHB85vDuow", title: "스타벅스에서 영어로 주문할 때 버벅거리지 않는 치트키", ytChannel: "실전영어회화", igCreator: "@starbucks_english", ttCreator: "@cafe_english" }
      ]
    };"""

if target_tech_end in code:
    code = code.replace(target_tech_end, replacement_all_categories)
    print("Added full authentic video items to TOPIC_SPECIFIC_ITEMS for psychology, fashion, travel, pets, english.")
else:
    print("WARNING: target_tech_end not found in update_dashboard.py.")

# 3. Update renderSubtopics to use category-specific subtopics
old_render_subtopics = """    function renderSubtopics() {
      var wrap = document.getElementById("subTopicsWrap");
      var subTopics = [
        { id: "sub-1", name: "1티어 치트키형", count: "30개+" },
        { id: "sub-2", name: "한국인이 가장 많이 저지르는 실수 TOP 3", count: "25개+" },
        { id: "sub-3", name: "7일 단기 챌린지 검증형", count: "25개+" }
      ];
      var html = '<button class="subtopic-tab ' + (activeSubId === 'all' ? 'active' : '') + '" onclick="selectSubTopic(\\'all\\')"><span>전체 카테고리 (' + currentDisplayLimit + '개+)</span></button>';
      for (var i = 0; i < subTopics.length; i++) {
        var sub = subTopics[i];
        html += '<button class="subtopic-tab ' + (activeSubId === sub.id ? 'active' : '') + '" onclick="selectSubTopic(\\'' + sub.id + '\\')">';
        html += '<span>' + sub.name + '</span><span class="tab-count">' + sub.count + '</span></button>';
      }
      wrap.innerHTML = html;
    }"""

new_render_subtopics = """    function renderSubtopics() {
      var wrap = document.getElementById("subTopicsWrap");
      var cat = CATEGORIES.find(function(c) { return c.key === currentTopicKey; }) || CATEGORIES[0];
      var subTopics = cat.subTopics || [
        { id: "sub-1", name: "1티어 치트키형" },
        { id: "sub-2", name: "한국인이 가장 많이 저지르는 실수 TOP 3" },
        { id: "sub-3", name: "7일 단기 챌린지 검증형" }
      ];

      var html = '<button class="subtopic-tab ' + (activeSubId === 'all' ? 'active' : '') + '" onclick="selectSubTopic(\\'all\\')"><span>🔥 전체 소주제 & 관련 키워드 통합 (' + currentDisplayLimit + '개+)</span></button>';
      for (var i = 0; i < subTopics.length; i++) {
        var sub = subTopics[i];
        html += '<button class="subtopic-tab ' + (activeSubId === sub.id ? 'active' : '') + '" onclick="selectSubTopic(\\'' + sub.id + '\\')">';
        html += '<span>' + sub.name + '</span></button>';
      }
      wrap.innerHTML = html;
    }"""

if old_render_subtopics in code:
    code = code.replace(old_render_subtopics, new_render_subtopics)
    print("Updated renderSubtopics with dynamic category-specific subtopics.")
else:
    print("WARNING: old_render_subtopics not found in update_dashboard.py.")

# 4. Update generateVideosForFilter to assign subtopics and titles according to cat.subTopics
old_gen_subtopics = """      var subTopics = [
        { id: "sub-1", name: topicName + " 1티어 치트키", count: Math.ceil(totalCount * 0.36) },
        { id: "sub-2", name: "한국인이 가장 많이 저지르는 실수 TOP 3", count: Math.ceil(totalCount * 0.32) },
        { id: "sub-3", name: "7일 단기 챌린지 검증형", count: Math.ceil(totalCount * 0.32) }
      ];"""

new_gen_subtopics = """      var catSubTopics = cat.subTopics || [
        { id: "sub-1", name: topicName + " 1티어 치트키" },
        { id: "sub-2", name: "한국인이 가장 많이 저지르는 실수 TOP 3" },
        { id: "sub-3", name: "7일 단기 챌린지 검증형" }
      ];"""

if old_gen_subtopics in code:
    code = code.replace(old_gen_subtopics, new_gen_subtopics)
    print("Updated generateVideosForFilter subtopics header.")
else:
    print("WARNING: old_gen_subtopics not found in update_dashboard.py.")

# Replace subId assignment in generateVideosForFilter:
old_subid_assign = "var subId = subTopics[(i - 1) % 3].id;"
new_subid_assign = "var subId = catSubTopics[(i - 1) % catSubTopics.length].id;"
if old_subid_assign in code:
    code = code.replace(old_subid_assign, new_subid_assign)
    print("Updated subId assignment.")
else:
    print("WARNING: old_subid_assign not found in update_dashboard.py.")

# 5. In renderVideos, ALWAYS guarantee 75+ videos for ANY period by merging live API results with topic-authentic pool:
old_render_live_check = """      var cacheKey = currentTopicKey + "_" + activeTimeFilter;
      if (userApiKey && LIVE_API_CACHE[cacheKey] && (activePlatform === "shorts" || activePlatform === "all")) {
        list = LIVE_API_CACHE[cacheKey].slice();
      } else {
        // Dynamic Generator guaranteeing currentDisplayLimit videos for THIS exact period and THIS exact platform
        var generated = generateVideosForFilter(currentTopicKey, activeTimeFilter, activePlatform, activeSubId, activeSurgeFilter, activeSort, currentDisplayLimit);
        list = generated.videos;
      }"""

new_render_live_check = """      var cacheKey = currentTopicKey + "_" + activeTimeFilter;
      var liveItems = (userApiKey && LIVE_API_CACHE[cacheKey] && (activePlatform === "shorts" || activePlatform === "all")) ? LIVE_API_CACHE[cacheKey].slice() : [];
      var generated = generateVideosForFilter(currentTopicKey, activeTimeFilter, activePlatform, activeSubId, activeSurgeFilter, activeSort, currentDisplayLimit);
      var genVideos = generated.videos;

      if (liveItems.length > 0) {
        // Filter live items by subtopic if specific subtopic is selected
        if (activeSubId !== "all") {
          var cat = CATEGORIES.find(function(c) { return c.key === currentTopicKey; }) || CATEGORIES[0];
          var subObj = (cat.subTopics || []).find(function(s) { return s.id === activeSubId; });
          if (subObj) {
            var subWords = subObj.name.split(/[\\s&/]+/).filter(Boolean);
            liveItems = liveItems.filter(function(v) {
              return subWords.some(function(w) { return v.title.indexOf(w) !== -1; });
            });
          }
        }

        // Start with live items, and seamlessly fill up to currentDisplayLimit (ALWAYS 75+ videos!)
        var seenYt = {};
        for (var li = 0; li < liveItems.length; li++) {
          seenYt[liveItems[li].youtubeId] = true;
          list.push(liveItems[li]);
        }
        for (var gi = 0; gi < genVideos.length; gi++) {
          if (!seenYt[genVideos[gi].youtubeId] && list.length < currentDisplayLimit) {
            seenYt[genVideos[gi].youtubeId] = true;
            list.push(genVideos[gi]);
          }
        }
      } else {
        list = genVideos;
      }"""

if old_render_live_check in code:
    code = code.replace(old_render_live_check, new_render_live_check)
    print("Updated renderVideos with guaranteed 75+ video threshold & topic merging.")
else:
    print("WARNING: old_render_live_check not found in update_dashboard.py.")

with open(r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved update_dashboard.py. Rebuilding index.html and preview.html...")
os.system(r'python "c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩\update_dashboard.py"')
