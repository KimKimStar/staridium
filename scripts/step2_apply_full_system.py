import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update modal nav tabs to clearly reflect:
# ① 3초 훅 & 성공 요인
# ② 컷전환 · 편집 방식 · 노래(BGM)
# ③ 타임라인별 대사 스크립트
# 🚀 내 채널 즉시 적용 (떡상 기획안 3선)
html = html.replace(
    '<button class="m-tab-btn" id="tabBtnEditing" onclick="switchModalTab(\'editing\')">② 컷 전환 & 편집 방식</button>',
    '<button class="m-tab-btn" id="tabBtnEditing" onclick="switchModalTab(\'editing\')">② 컷전환 · 편집 방식 · 노래(BGM)</button>'
)

# 2. Add generateDetailedVideoAnalysis before generateVideosForFilter
generator_code = """
    // Comprehensive AI Deep-Dive Video Analyzer: Tailors 6 Core Viral Anatomy Metrics for Every Video
    function generateDetailedVideoAnalysis(baseItem, topicKey, rank, timeFilter, topicName) {
      var title = (baseItem && baseItem.title) ? baseItem.title : "";
      var author = (baseItem && baseItem.ytChannel) ? baseItem.ytChannel : "크리에이터";

      var CATEGORY_PROFILES = {
        total_kr: {
          tag: "종합 1위 떡상",
          hookScripts: [
            "“1분 만에 소름 돋게 만드는 한국인의 3가지 종특, 여러분도 100% 해당됩니다.”",
            "“다이소/올영 직원들이 퇴근할 때 몰래 사간다는 역대급 1티어 꿀템 공개!”",
            "“한국인 99%가 매일 무의식중에 돈 날리고 있는 충격적인 이유!”",
            "“올해 대한민국 숏폼 알고리즘 1위 찍은 30초 레전드 영상의 비밀!”"
          ],
          hookVisual: "화자 정면 1:1 아이컨택 120% 스냅 줌인 + 경고 사이렌 사운드 & 화면 흑백 반전 후 네온 옐로우 자막 쾅!",
          hookPsychology: "한국인 특유의 손실 회피 편향(Loss Aversion) 및 '나만 모르면 손해'라는 FOMO 심리를 0.2초 만에 자극",
          cutSpeed: "평균 0.75초 (대한민국 숏폼 최적 도파민 분비 템포)",
          style: "세로 9:16 모바일 풀스크린 점프컷 + 단어 단위 바운스 자막 + 0.8초마다 시각적 앵글 전환",
          bgm: "130 BPM 트렌딩 일렉트로닉 팝 & 딥 베이스 킥 (스마트폰 스크롤 즉각 정지용)",
          sfx: "00:01 도입부 Sub-Bass 드롭 -> 0.8초마다 Whoosh 컷전환음 -> 00:15 지점 레코드 스크래치 반전음",
          caption: "화면 중앙 형광 옐로우(#FACC15) + 블랙 3px 아웃라인 (Gmarket Sans Bold) + 안전영역 상단15%/하단20% 준수",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“이거 모르면 한국에서 평생 300만원 손해봅니다. 딱 15초만 집중하세요!”", visual: "화자 극단적 클로즈업 + 타이포그래피 경고 그래픽" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“대부분의 한국인들이 당연하게 여기는 이 습관, 사실은 시간과 돈을 통째로 날리는 최악의 실수입니다.”", visual: "실제 실패 사례 B-roll 컷 0.7초 간격 교차 편집" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“상위 1%만 아는 해결책은 바로 이 1가지입니다. 오늘부터 이것만 딱 바꿔보세요.”", visual: "손가락으로 콕 짚으며 3D 인포그래픽 화살표 노출" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“구체적인 방법과 링크는 고정댓글에 남겨뒀으니 지금 바로 확인하고 저장해두세요!”", visual: "하단 고정댓글 지목 모션 + 북마크 아이콘 점멸" }
          ],
          successFactors: [
            { title: "초반 2.5초 '시청 이탈 방지' 오픈 루프", desc: "시작하자마자 결말의 자극적인 반전 장면을 0.3초간 먼저 보여주어 끝까지 시청하게 만듦" },
            { title: "평균 컷 전환 0.75초 초고속 리듬", desc: "한 구도에 1초 이상 머무르지 않고 클로즈업, 리액션, 자막 그래픽을 연속 교차" },
            { title: "자연스러운 댓글 논쟁 및 저장 유도", desc: "도발적인 화두 제시와 고정댓글 유도로 알고리즘 핵심 지표인 북마크/댓글 수 폭발" }
          ],
          viralReason: "⚡ 24시간 실시간 알고리즘 오픈루프 + 0.75초 초고속 점프컷"
        },
        psychology: {
          tag: "심리 화법 치트키",
          hookScripts: [
            "“나를 은근히 무시하는 사람, 절대 화내지 마세요. 딱 이 한마디면 얼굴 빨개집니다.”",
            "“손절해야 하는 사람 유형 1순위! 이런 사람은 오늘 당장 카톡 차단하세요.”",
            "“말 잘하는 사람들이 무의식중에 쓰는 3초 화법의 비밀, 이것만 쓰면 호감도 200% 폭발합니다.”",
            "“기분 나쁘지 않게 똑 부러지게 거절하는 심리 기술, 평생 호구 안 잡히는 법!”"
          ],
          hookVisual: "화자 정면 1:1 시선 응시 + 흑백 대비 조명 + 침묵 0.5초 정적 후 핵심 한마디 대사 발화",
          hookPsychology: "인간관계 억울함에 대한 대리만족(카타르시스) 및 '즉시 써먹는 1문장 방어 기제' 갈망 자극",
          cutSpeed: "평균 1.05초 (화자의 음성과 텍스트 뉘앙스를 온전히 소화시키는 고밀도 템포)",
          style: "미니멀 시네마틱 톤 + 텍스트 페이드인 + 감정 고조 시 카메라 5% 슬로우 푸시인",
          bgm: "88 BPM 칠합(Chillhop) & 감성 Lo-Fi 피아노 루프 (차분하고 지적인 분위기)",
          sfx: "심장 박동 쿵..쿵.. -> 반격 대사 타이밍에 마이크 에코 + 유리 깨지는 임팩트음",
          caption: "차분한 연보라(#DDD6FE) & 웜화이트 텍스트 + 따옴표 강조 + 나눔명조 볼드",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“무례한 사람에게 참다참다 폭발하면 나만 이상한 사람 됩니다. 이렇게 말해보세요.”", visual: "화자 정면 1:1 아이컨택 + 흑백 조명 연출" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“'농담인데 왜 그래?'라며 선 넘는 사람들, 웃어넘기면 계속 호구 잡히고 화내면 예민한 사람 취급받습니다.”", visual: "무례한 대화 상황 재연 컷 0.8초 교차" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“그럴 땐 표정 하나 안 바꾸고 차분하게 되물어보세요. '그 말은 어떤 의도로 하신 거예요?' 이 한마디에 상황 종료됩니다.”", visual: "대사 타이포그래피 볼드 확대 + 정적 사운드 연출" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“기분 안 나쁘게 선 긋는 어른들의 대화법 5가지는 고정댓글에 적어뒀으니 꼭 저장해두세요!”", visual: "하단 고정댓글 손가락 지목 + 저장 북마크 아이콘" }
          ],
          successFactors: [
            { title: "압도적 공감대 형성", desc: "누구나 살면서 한 번쯤 겪어본 억울한 인간관계 순간을 0.5초 만에 소환하여 몰입" },
            { title: "즉시 입 밖으로 내뱉는 1문장 솔루션", desc: "복잡한 심리학 이론 대신 내일 당장 회사/친구에게 쓸 수 있는 킬러 대사 제공" },
            { title: "폭발적인 댓글 사연 공유", desc: "시청자들이 본인의 억울했던 경험담을 장문 댓글로 달며 알고리즘 상호작용 급증" }
          ],
          viralReason: "💬 관계 피로도 카타르시스 + 1초 킬러 대사 솔루션"
        },
        humor: {
          tag: "일상 공감 & 썰",
          hookScripts: [
            "“미용실에서 머리 망했을 때 거울 본 한국인 99%의 현실 리액션 ㅋㅋㅋ”",
            "“당근마켓에서 만난 역대급 네고 빌런 레전드 ㅋㅋㅋ 이건 진짜 실화냐?”",
            "“직장인 퇴근 5분 전에 상사가 불렀을 때 얼굴 표정 변화 현실 고증”",
            "“소개팅에서 첫눈에 반했을 때 남자들 고장 난 행동 모음 ㅋㅋㅋ”"
          ],
          hookVisual: "주인공 어색한 눈동자 굴림 + 클로즈업 + 땀 삐질 만화 이펙트 + 황당한 거울 속 비주얼",
          hookPsychology: "지독한 하이퍼리얼리즘 공감대 및 친구 태그 유발(웃음 공유 카타르시스)",
          cutSpeed: "평균 0.68초 (슬랩스틱 & 반전 펀치라인 최적화 초고속 컷)",
          style: "스케치 코미디 점프컷 + 사운드 묵음 펀치라인 + 적재적소 밈(Meme) 인서트",
          bgm: "128 BPM 코믹 펑크 베이스 & 익살스러운 슬랩스틱 튠",
          sfx: "레코드 스크래치 찌익! -> 카톡 알림음 톡! -> 황당한 비둘기 구구구 사운드",
          caption: "네온 옐로우 & 만화풍 블랙 테두리 + 격한 흔들림(Shake) 모션 효과",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“'손님, 머리 너무 잘 나왔죠?'라는 미용사 말에 나의 떨리는 동공...”", visual: "주인공 동공 지진 극접사 + 땀방울 CG" },
            { time: "00:03 - 00:12", stage: "상황 전개 (Agitation)", text: "“속으로는 '내 3만원...' 비명을 지르고 있지만 입에서는 '네.. 마음에 들어요ㅎㅎ' 나오는 K-사회생활.”", visual: "어색한 미소 짓는 주인공 3단 줌인" },
            { time: "00:12 - 00:24", stage: "클라이맥스 (Punchline)", text: "“집에 가는 엘리베이터 거울 보며 모자 깊게 눌러쓰고 친구한테 카톡으로 '나 머리 망함' 폭풍 전송 중.”", visual: "엘리베이터 거울 좌절 샷 + 카톡 타자음 연타" },
            { time: "00:24 - 00:32", stage: "행동 유도 (CTA)", text: "“너도 이런 적 있지? 머리 망해본 친구 소환해서 같이 웃자 ㅋㅋㅋ”", visual: "댓글창 친구 태그 유도 화살표 + 공유 버튼 펄스" }
          ],
          successFactors: [
            { title: "디테일한 하이퍼리얼리즘 표정 연기", desc: "미세한 눈동자 흔들림과 어색한 호흡을 포착해 시청자 몰입도 100% 달성" },
            { title: "카카오톡 단톡방 공유 폭발", desc: "'이거 완전 너잖아' 반응으로 메신저 공유 링크 클릭률 극대화" },
            { title: "20초 짧은 호흡의 무한 루프", desc: "군더더기 없는 짧은 러닝타임으로 1회 이상 반복 재생 유도" }
          ],
          viralReason: "😂 하이퍼리얼리즘 공감대 + 카톡 공유 폭발"
        },
        diet: {
          tag: "다이어트 & 홈트",
          hookScripts: [
            "“아직도 유산소 1시간씩 뛰세요? 솔직히 이거 모르면 뱃살 평생 안 빠집니다.”",
            "“의사들이 제발 이것만은 지키라고 경고한 3일 뱃살 삭제 식단 루틴!”",
            "“밤마다 야식 먹고도 체지방 8% 유지하는 사람들의 3가지 비밀 공개!”",
            "“누워서 딱 3분만 따라 하세요. 다음 날 아침 바지 사이즈가 달라집니다.”"
          ],
          hookVisual: "화자 허리둘레 측정 0.4초 컷 -> 충격적인 뱃살 Before/After 흑백 전환 -> 붉은색 경고 자막 120% 스냅 줌인",
          hookPsychology: "체중 감량 정체기 불안감(Frustration) 자극 및 즉각적 해결을 원하는 긴급성(Urgency) 극대화",
          cutSpeed: "평균 0.75초 (홈트 동작 및 식단 비주얼 도파민 템포)",
          style: "세로 9:16 모바일 풀스크린 + 타이머 카운트다운 CG + 주요 부위 하이라이트 원형 포인터",
          bgm: "132 BPM 업비트 EDM 하우스 & 에너제틱 드럼 비트",
          sfx: "도입부 쿵(Heavy Kick) -> 운동 전환 시 호루라기 휘슬 -> 식단 공개 시 팅(Chime)",
          caption: "중앙 상단 볼드 옐로우(#FDE047) + 블랙 테두리 3px + 핵심 키워드 레드 하이라이트",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“아직도 굶어서 살 빼세요? 이 1가지만 바꾸면 자면서도 살 빠집니다.”", visual: "화자 복부 클로즈업 + 타이머 경고음" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“매일 닭가슴살만 먹고 유산소 1시간 뛰어도 체중계 안 바뀌는 이유, 바로 인슐린 저항성 때문입니다.”", visual: "체중계 올라가서 한숨 쉬는 B-roll 3단 점프컷" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“식사 전 '사과식초 1스푼'과 '채소 먼저 먹기', 딱 이 2단계만 지켜보세요. 혈당 스파이크가 60% 잡힙니다.”", visual: "식사 순서 인포그래픽 3D 화살표 + 실물 식단 클로즈업" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“제가 7일간 직접 먹고 3kg 뺀 식단 조합표는 고정댓글에 링크 걸어뒀으니 저장해두고 오늘 저녁부터 바로 해보세요!”", visual: "하단 화살표 펄스 모션 + 저장 북마크 아이콘" }
          ],
          successFactors: [
            { title: "결말 先공개 훅", desc: "시작 2초 내에 성공 체형 변화 애프터를 0.3초간 노출하여 이탈률 18% 감소" },
            { title: "시청 지속 루프", desc: "'자면서도 빠지는 원리'라는 도발적 명제로 끝까지 시청할 이유 부여" },
            { title: "저장(Save) 트리거", desc: "'식단표 고정댓글'로 알고리즘 가중치가 가장 높은 북마크 수 확보" }
          ],
          viralReason: "🥗 손실 회피 인슐린 원리 + 북마크 저장 폭발"
        },
        finance: {
          tag: "재테크 · 1억 모으기",
          hookScripts: [
            "“월 250 받아서 언제 집 사냐고요? 통장 3개로 쪼갰더니 3년 만에 1억 모였습니다.”",
            "“한국인들이 무의식중에 은행에 갖다 바치는 아까운 수수료와 이자 TOP 3!”",
            "“월급 200만원 직장인이 무조건 사 모아야 할 미국 배당 ETF 포트폴리오!”",
            "“부자들은 절대 안 사고 가난한 사람들만 줄 서서 사는 소비 습관의 비밀!”"
          ],
          hookVisual: "은행 잔고 캡처 화면 블러 처리 후 붉은색 상승 화살표 팝업 + 화자 진지한 아이컨택 바운스 줌인",
          hookPsychology: "상대적 박탈감(FOMO) 극복 욕구 및 실천 가능한 구체적 액션 플랜 제시로 신뢰도 확보",
          cutSpeed: "평균 0.88초 (통장 내역 및 금융 데이터 전달 최적 리듬)",
          style: "스플릿 스크린(통장/소비내역 비교) + 핵심 숫자 카운팅 모션 그래픽 + 형광펜 밑줄 효과",
          bgm: "122 BPM 모던 테크노 비트 & 딥 신스 베이스 (지적이고 신뢰감 있는 톤)",
          sfx: "돈 세는 찰칵 효과음 -> 통장 개설 띵동 -> 지출 경고 버저음",
          caption: "네온 그린(#22C55E) & 클린 화이트 배색 + Pretendard Bold + 숫자 볼드 140%",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“월급 200만원대 직장인이 무조건 따라 해야 하는 1억 모으기 3통장 법칙!”", visual: "화자 정면 바운스 줌인 + 잔고 1억 텍스트 그래픽" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“열심히 아끼는데 돈이 안 모이는 분들의 공통점, 월급 통장에서 생활비와 고정비가 섞여 나가기 때문입니다.”", visual: "지출 내역 영수증 컷 교차 편집" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“월급날 즉시 저축 통장으로 50% 자동이체, 생활비는 체크카드로 한도 고정, 비상금은 CMA에 묶으세요.”", visual: "통장 3개 분배 인포그래픽 3D 화살표" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“사회초년생 추천 고금리 파킹통장 TOP 3 리스트는 고정댓글에 정리해뒀으니 캡처해서 보관하세요!”", visual: "하단 고정댓글 지목 + 저장 북마크 아이콘" }
          ],
          successFactors: [
            { title: "현실적 숫자 제시", desc: "'10억'이 아닌 '월 250 직장인의 1억'이라는 손에 잡히는 타깃 설정" },
            { title: "스크린샷 캡처 유도", desc: "15초 지점 통장 분배 도표로 일시정지 및 공유 행동 3.5배 증가" },
            { title: "손실 회피 화법", desc: "'안 하면 매달 50만원씩 손해' 프레임으로 끝까지 몰입" }
          ],
          viralReason: "📈 손실 회피 통장 분배법 + 스크린샷 캡처 유발"
        },
        cooking: {
          tag: "초간단 꿀맛 레시피",
          hookScripts: [
            "“라면 끓일 때 물부터 올리지 마세요! 대파 기름에 이것 한 스푼 넣으면 5성급 호텔 라면 됩니다.”",
            "“백종원도 감탄한 5분 만에 끝내는 레전드 볶음밥 조합 대공개!”",
            "“편의점 음식으로 만드는 1인 가구 극락 야식 레시피 TOP 3!”",
            "“자취생들 주목! 프라이팬 하나로 끝내는 고깃집 된장찌개 황금 비율!”"
          ],
          hookVisual: "팬에 지글지글 끓어오르는 대파 기름 고화질 극접사(Macro) + 면발 들어올리는 0.5초 슬로모션",
          hookPsychology: "초간단 대비 극상의 맛(가성비 도파민) 및 지금 당장 주방으로 뛰어가고 싶은 시각적 자극",
          cutSpeed: "평균 0.65초 (재료 손질부터 완성까지 군더더기 제로 스피드 리듬)",
          style: "탑다운 버티컬 뷰(Top-down) + 레시피 계량 자막(1스푼, 반 컵) 팝업 + 조리 ASMR 강조",
          bgm: "118 BPM 경쾌한 어쿠스틱 스윙 팝 (요리 욕구를 자극하는 밝은 분위기)",
          sfx: "도마 칼질 탁탁탁탁 -> 불 켜는 파이어 화륵 -> 기름 지글지글 ASMR -> 면치기 후루룩",
          caption: "따뜻한 오렌지(#FB923C) & 크림 화이트 + 재료 분량 옐로우 박스 표기",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“진짜 딱 5분만 투자해보세요. 평생 끓여먹던 라면 맛의 신세계가 열립니다.”", visual: "지글지글 기름에 볶아지는 양념 극접사" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“맨날 똑같은 라면에 질리셨죠? 물 붓기 전에 식용유 두 스푼에 대파와 고춧가루를 먼저 볶아주세요.”", visual: "파기름 내는 빠른 손놀림 0.6초 컷" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“불향이 확 올라올 때 물을 붓고 쌈장 반 스푼을 퐁당! 국물이 진한 사골육수처럼 묵직해집니다.”", visual: "보글보글 끓어오르는 국물 비주얼 + 면 투하" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“정확한 재료 계량과 꿀조합은 고정댓글에 적어뒀으니 오늘 야식으로 무조건 해 드셔보세요!”", visual: "완성된 라면 한 젓가락 들어올리는 클로즈업 + 저장 유도" }
          ],
          successFactors: [
            { title: "시각 & 청각 ASMR 융합", desc: "칼질과 볶는 소리를 BGM보다 크게 믹싱해 침샘 폭발" },
            { title: "실패 없는 3단계 단순화", desc: "누구나 집에 있는 재료(대파, 쌈장)로 진입장벽 최소화" },
            { title: "주말 야식 타깃 바이럴", desc: "저장해두고 장 보러 가거나 야식 시점에 다시 보게 만드는 저장 장치" }
          ],
          viralReason: "🍳 지글지글 극접사 ASMR + 3단계 초간단 레시피"
        },
        beauty: {
          tag: "올영 세일 & 꿀피부",
          hookScripts: [
            "“올리브영 세일할 때 비싼 에센스 사지 마세요. 피부과 의사들이 몰래 쓰는 5천원짜리 꿀템!”",
            "“블랙헤드 억지로 짜지 마세요! 클렌징 오일 1분 롤링으로 모공 싹 비우는 법!”",
            "“화장 다 뜨고 밀리는 분들, 파운데이션 바꾸지 말고 기초 바르는 순서만 바꾸세요.”",
            "“올리브영 직원 3년 차가 퇴근할 때마다 쟁여놓는 1티어 기초 추천템 TOP 3!”"
          ],
          hookVisual: "피부결 Before/After 0.3초 플래시 비교 + 모공 클로즈업 후 깐달걀 피부 줌아웃",
          hookPsychology: "피부 트러블에 대한 외모 불안(Insecurity) 해소 및 올영 세일 가성비 소비 심리 자극",
          cutSpeed: "평균 0.78초 (제형 텍스처 및 비포애프터 교차 템포)",
          style: "고화질 피부 매크로 샷 + 화장품 텍스처 발림성 슬로우 모션 + 제품명 팝업 스티커",
          bgm: "126 BPM 몽환적인 드림 팝 & K-Pop 챌린지 인스트루멘탈",
          sfx: "스킨 톡톡 흡수음 -> 크림 바르는 쫀득한 사운드 -> 깐달걀 피부 반짝 샤라랑 효과음",
          caption: "트렌디한 핑크 라벤더(#F472B6) & 화이트 + 세일 정보 옐로우 뱃지",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“올영 세일 때 이거 안 사면 진짜 손해봅니다. 피부과 실장님 추천템 대공개!”", visual: "화자 정면 피부결 노출 + 올리브영 쇼핑백 등장" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“비싼 앰플 발라도 속건조 계속되고 좁쌀 올라오는 이유, 피부 장벽이 무너졌기 때문입니다.”", visual: "각질 일어난 피부 매크로 줌인" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“세안 직후 물기 닦지 말고 이 토너를 3겹 레이어링 해보세요. 하루 종일 물광이 유지됩니다.”", visual: "제품 제형 손등 테스트 및 얼굴 도포 비주얼" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“피부 타입별(지성/건성) 추천 호수는 고정댓글에 링크 걸어뒀으니 올영 가기 전에 캡처해두세요!”", visual: "고정댓글 화살표 + 저장 북마크 아이콘" }
          ],
          successFactors: [
            { title: "현실적인 모공 Before/After", desc: "보정 없는 실물 카메라 접사로 시청자 신뢰도 300% 확보" },
            { title: "올영 세일 시즌 타이밍", desc: "세일 키워드와 연동되어 탐색 탭 및 쇼츠 알고리즘 폭발적 추천" },
            { title: "제품 리스트 캡처 유도", desc: "매장에서 바로 보려고 저장하는 북마크 행동 유발" }
          ],
          viralReason: "💄 올영 세일 타이밍 + 무보정 비포애프터 신뢰도"
        },
        tech: {
          tag: "IT 생산성 & 스마트폰",
          hookScripts: [
            "“아이폰/갤럭시 유저 99%가 평생 모르고 지나가는 숨겨진 꿀기능 3가지!”",
            "“아직도 엑셀 노가다 하세요? 무료 AI 툴 하나로 3시간 업무 30초 컷 끝내기!”",
            "“배터리 광탈하는 분들, 설정에서 이것 딱 하나만 끄면 배터리 2배 오래 갑니다.”",
            "“카카오톡 쓸 때 이거 모르면 내 사생활 다 털립니다. 지금 당장 확인하세요!”"
          ],
          hookVisual: "스마트폰 화면 녹화 UI 극접사 줌인 + 터치 지점 네온 핑(Ping) 펄스 효과",
          hookPsychology: "내가 가진 기기의 숨은 가치를 놓치고 있다는 '기회비용 손실감' 자극",
          cutSpeed: "평균 0.72초 (스마트폰 설정 UI 화면 전환 최적화 스피드)",
          style: "모바일 화면 녹화 PIP 화면 합성 + 제스처 손가락 모션 그래픽 + 핵심 메뉴 줌인",
          bgm: "130 BPM 하이테크 퓨처 베이스 & 글리치 리듬",
          sfx: "스마트폰 화면 탭 톡! -> 설정 온/오프 토글 스위치 찰칵! -> 완료 띵동!",
          caption: "사이버 시안(#22D3EE) & 볼드 화이트 + 경로 표시 화살표 [설정 > 일반 > 터치]",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“스마트폰 쓰면서 이 설정 안 켜두면 진짜 100만원 버리는 겁니다.”", visual: "스마트폰 화면 뒷면 탭 제스처 시연" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“맨날 스크롤 내리고 번거롭게 누르셨죠? 뒷면 두 번만 톡톡 치면 스크린샷과 QR 코드가 바로 뜹니다.”", visual: "설정 경로 메뉴 이동 0.7초 점프컷" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“설정 -> 손쉬운 사용 -> 터치 -> 뒷면 탭에서 '이중 탭'을 스크린샷으로 바꿔보세요. 삶의 질이 수직 상승합니다.”", visual: "실제 동작하는 모습 1인칭 시점 촬영" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“기종별 지원 모델과 추가 꿀기능 리스트는 고정댓글에 남겨뒀으니 저장하고 천천히 따라 해보세요!”", visual: "하단 고정댓글 지목 + 저장 북마크 아이콘" }
          ],
          successFactors: [
            { title: "직관적인 1초 시연", desc: "말보다 실제 기기가 동작하는 장면을 0초에 바로 보여주어 스크롤 멈춤" },
            { title: "즉시 따라하기 유도", desc: "시청하면서 동시에 스마트폰 설정을 켜보게 만드는 인터랙션" },
            { title: "가족/친구 공유율 극대화", desc: "'엄마 스마트폰도 이거 해드려야겠다'는 효도/공유 트리거" }
          ],
          viralReason: "💻 1초 직관적 기기 시연 + 뒷면 탭 생산성 혁신"
        },
        growth: {
          tag: "동기부여 & 갓생 루틴",
          hookScripts: [
            "“아침에 눈뜨자마자 스마트폰 보는 순간, 오늘 하루 집중력은 이미 망한 겁니다.”",
            "“인생 망했다고 생각될 때 딱 7일만 이 3가지 루틴으로 살아보세요.”",
            "“성공한 사람들의 99%가 매일 아침 거울 보며 무의식중에 외치는 확언의 힘!”",
            "“게으름을 의지력으로 이기려 하지 마세요. 뇌과학이 증명한 5초 법칙!”"
          ],
          hookVisual: "새벽 기상 알람 시계 0.4초 컷 -> 암전 후 차분한 자연광 스튜디오 화자 아이컨택",
          hookPsychology: "무기력감 극복 욕구 및 갓생(God-life)을 향한 내적 동기부여 자극",
          cutSpeed: "평균 0.92초 (차분하면서도 단호한 어조의 음성에 맞춘 템포)",
          style: "시네마틱 4K 감성 톤 + 텍스트 키워드 묵직한 타이포 연출 + 명언 인서트",
          bgm: "105 BPM 웅장한 시네마틱 피아노 빌드업 (벅차오르는 감정선 유도)",
          sfx: "알람 시계 째깍째깍 -> 암전 스위치 찰칵 -> 심호흡 들이쉬는 소리 후 빌드업 비트",
          caption: "골드 앰버(#F59E0B) & 웜화이트 + Pretendard Bold + 명언 따옴표 강조",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“침대에서 폰 보며 30분 뒹굴거리는 습관, 뇌 도파민 수용체를 완전히 파괴합니다.”", visual: "어두운 방에서 스마트폰 불빛만 비추는 얼굴 클로즈업" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“자꾸 미루고 무기력한 건 여러분의 의지가 약해서가 아니라 아침 첫 도파민 설계가 잘못되었기 때문입니다.”", visual: "한숨 쉬며 머리 감싸쥐는 일상 컷" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“내일 아침엔 눈뜨자마자 찬물 한 잔 마시고 이불 딱 10초만 개보세요. 뇌가 '작은 성공'을 인지하며 집중 모드로 전환됩니다.”", visual: "이불 정리하고 물 마시는 감성 톤 시연" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“작심삼일 탈출하는 7일 모닝 루틴 체크리스트는 고정댓글에서 무료로 다운로드하고 오늘 밤부터 실천하세요!”", visual: "체크리스트 그래픽 + 고정댓글 화살표" }
          ],
          successFactors: [
            { title: "뇌과학적 근거 제시", desc: "단순 훈계가 아닌 도파민과 뇌과학 원리로 지적 신뢰감 확보" },
            { title: "진입장벽 제로의 첫 행동", desc: "'이불 개기'라는 누구나 지금 할 수 있는 1초 행동 제시" },
            { title: "야간 시청자 반성 심리 공략", desc: "밤 11시~새벽 2시 쇼츠 탐색 중 자책하는 시청자의 저장률 250% 폭발" }
          ],
          viralReason: "🧠 뇌과학 도파민 설계 + 이불 개기 1초 갓생 루틴"
        },
        fashion: {
          tag: "체형별 코디 & OOTD",
          hookScripts: [
            "“키 170 이하인데 와이드 팬츠 이렇게 입으면 다리 5cm 길어 보입니다.”",
            "“비싼 옷 사지 마세요. SPA 브랜드에서 이것 2개만 조합하면 패션 피플 완성!”",
            "“체형 커버 끝판왕! 어깨 좁아 보이거나 배 나와 보이는 사람 무조건 피해야 할 핏!”",
            "“남친룩/여친룩의 정석! 호불호 절대 없는 2030 데일리룩 3가지 공식!”"
          ],
          hookVisual: "전신 거울 핏 비교 Before(어정쩡한 핏) vs After(다리 길어 보이는 황금 비율) 0.4초 교차",
          hookPsychology: "단점 체형 콤플렉스 개선 갈망 및 세련된 첫인상 획득 욕구 자극",
          cutSpeed: "평균 0.72초 (의류 착장 및 각도별 핏 전환 최적화 템포)",
          style: "풀바디 세로 9:16 OOTD 워킹 샷 + 의류 브랜드/사이즈 정보 자막 태그",
          bgm: "124 BPM 그루비한 하우스 팝 & 칠한 런웨이 비트",
          sfx: "옷걸이 촤르륵 소리 -> 착장 체인지 슉! -> 핏 완성 찰칵 카메라 셔터음",
          caption: "모던 미니멀 블랙 & 화이트 배색 + 아이템 명칭/가격(#, KRW) 팝업",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“다리 짧아 보이는 최악의 바지 핏! 아직도 이렇게 입고 계신가요?”", visual: "밑단 끌리는 바지 클로즈업 + X 표시 그래픽" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“바지 밑단이 신발 위로 뭉개지면 시선이 아래로 쏠려 키가 3cm는 더 작아 보입니다.”", visual: "주름진 밑단과 어정쩡한 핏 3단 줌인" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“신발 혓바닥에 딱 닿는 원턱 세미와이드 핏을 고르고 벨트 라인을 살짝 올려 입어보세요. 비율이 완전히 달라집니다.”", visual: "황금 비율 착장으로 변신 후 전신 워킹 샷" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“영상에 나온 가성비 바지 품번과 사이즈 팁은 고정댓글에 남겨뒀으니 쇼핑할 때 참고하세요!”", visual: "제품 품번 텍스트 + 고정댓글 화살표" }
          ],
          successFactors: [
            { title: "극명한 비율 Before & After", desc: "0.3초 만에 시각적으로 체감되는 비율 차이로 즉각적 신뢰 형성" },
            { title: "쇼핑 직결 정보 제공", desc: "SPA 브랜드 실제 품번을 제공하여 구매 욕구 및 저장 유도" },
            { title: "성별 타깃 맞춤형 코디", desc: "2030 직장인/대학생이 내일 바로 입을 수 있는 현실적 착장" }
          ],
          viralReason: "👗 원턱 세미와이드 비율 보정 + SPA 실전 품번 제공"
        },
        travel: {
          tag: "국내 힐링 & 숨은 명소",
          hookScripts: [
            "“제주도 비행기 표 끊지 마세요. KTX 타고 1시간이면 가는 한국의 스위스 공개!”",
            "“현지인들만 몰래 가는 강원도 숨은 에메랄드빛 계곡 명소 TOP 3!”",
            "“주말에 당일치기로 다녀오기 딱 좋은 서울 근교 드라이브 힐링 코스!”",
            "“가성비 미쳤다! 1박 5만원에 바다 뷰 파노라마 감상 가능한 오션뷰 숙소!”"
          ],
          hookVisual: "드론 4K 파노라마 뷰 줌아웃 + 물안개 피어오르는 에메랄드빛 호수/바다 극상 비주얼",
          hookPsychology: "일상 탈출(Escapism) 욕구 및 남들이 모르는 프라이빗 명소 선점 심리",
          cutSpeed: "평균 0.85초 (시원한 풍경 감상과 스팟 이동을 조화시킨 템포)",
          style: "시네마틱 드론 뷰 + 이동 동선 지도 3D 핀포인트 그래픽 + 여행지 꿀팁 오버레이",
          bgm: "116 BPM 감성 인디 어쿠스틱 & 설렘 가득한 로드트립 비트",
          sfx: "자동차 문 닫히는 쿵 -> 바람 소리 쏴아 -> 파도 철썩이는 자연 ASMR",
          caption: "에메랄드 민트(#34D399) & 클린 화이트 + [위치, 주차 꿀팁, 비용] 요약 박스",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“외국 갈 필요 전혀 없습니다. 한국에 이런 곳이 있었다니 믿어지시나요?”", visual: "압도적인 절경 드론 샷 1초 만에 오픈" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“유명 관광지 가서 주차 전쟁 치르고 사람에 치이는 힐링은 이제 그만하세요.”", visual: "꽉 막힌 도로와 혼잡한 인파 B-roll 교차" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“여기는 입장료도 무료고 아직 관광객이 없어서 인생샷 100장 건질 수 있는 프라이빗 스팟입니다.”", visual: "인생샷 포토존 구도 및 주차장 위치 안내" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“정확한 내비게이션 주소와 주변 맛집 리스트는 고정댓글에 좌표 남겨뒀으니 주말 드라이브 갈 친구 태그하세요!”", visual: "지도 핀 그래픽 + 고정댓글 화살표" }
          ],
          successFactors: [
            { title: "첫 1초 압도적 풍경 드론 샷", desc: "시각적 아름다움으로 시청자의 시선을 0.5초 만에 잠금" },
            { title: "네비 주소 저장 트리거", desc: "'이번 주말에 가야지' 마음먹게 만드는 정확한 좌표와 주차 팁" },
            { title: "여행 메이트 태그 유발", desc: "'여기 같이 가자' 댓글로 2인 이상 시청자 유입 효과" }
          ],
          viralReason: "✈️ 드론 4K 절경 + 내비 좌표 고정댓글 저장 폭발"
        },
        pets: {
          tag: "반려동물 & 심쿵 댕냥이",
          hookScripts: [
            "“강아지가 내 손을 핥는 진짜 이유, 사랑해서가 아니라 ‘이것’ 때문이라고요?”",
            "“고양이가 주인 얼굴 빤히 쳐다볼 때 숨겨진 놀라운 속마음 3가지!”",
            "“집사가 외출했을 때 홈캠에 찍힌 강아지의 충격적인 하루...”",
            "“초보 견주 99%가 실수하는 강아지 만지면 절대 안 되는 신체 부위!”"
          ],
          hookVisual: "강아지/고양이 왕코 극접사(Macro) + 갸우뚱 고개 돌리는 심쿵 0.5초 컷",
          hookPsychology: "반려동물에 대한 무한한 애정 및 '내 아이의 속마음을 알고 싶다'는 호기심",
          cutSpeed: "평균 0.80초 (반려동물의 귀여운 순간과 정보 전달을 결합한 템포)",
          style: "강아지 시선 아이레벨 앵글 + 말풍선 동물 속마음 자막 + 하트 뿅뿅 이펙트",
          bgm: "110 BPM 통통 튀는 실로폰 & 경쾌한 우쿨렐레 힐링 멜로디",
          sfx: "강아지 발자국 뽀짝뽀짝 -> 킁킁 냄새 맡는 소리 -> 갸우뚱 뿅! 효과음",
          caption: "귀여운 파스텔 옐로우(#FEF08A) & 브라운 둥근 폰트 + 말풍선 표기",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“강아지가 내 손을 계속 핥는다면 당장 멈추게 하세요. 진짜 이유는 따로 있습니다.”", visual: "주인 손을 열심히 핥는 강아지 클로즈업" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“그냥 좋아서 애정 표현하는 줄 아셨죠? 사실은 스트레스나 영양 결핍 신호일 수 있습니다.”", visual: "갸우뚱하는 강아지 표정과 물음표 그래픽" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“핥을 때 바로 손을 빼지 말고 다른 장난감으로 시선을 돌려주세요. 하루 15분 노즈워크면 행동이 80% 교정됩니다.”", visual: "노즈워크 장난감으로 신나게 노는 장면" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“강아지 카밍 시그널 10가지 해석표는 고정댓글에 정리해뒀으니 우리 댕댕이 견주님들은 꼭 저장해두세요!”", visual: "하단 고정댓글 화살표 + 댕댕이 윙크" }
          ],
          successFactors: [
            { title: "첫인상 무조건 통하는 동물 접사", desc: "치명적인 귀여움으로 무조건 3초 이상 보게 만드는 치트키" },
            { title: "반려인들의 상식 파괴 지식", desc: "'내가 잘못 알고 있었나?' 불안감과 배움의 욕구 자극" },
            { title: "집사 커뮤니티 공유 확산", desc: "반려인 단톡방 및 인스타 스토리 공유 지표 급상승" }
          ],
          viralReason: "🐶 심쿵 극접사 + 반려인 상식 파괴 행동 교정 팁"
        },
        english: {
          tag: "원어민 1분 생활영어",
          hookScripts: [
            "“외국인이 'How are you?' 할 때 제발 'I'm fine thank you' 하지 마세요!”",
            "“미드에서 원어민들이 1초에 5번씩 쓰는 진짜 리얼 생활영어 만능 패턴!”",
            "“원어민한테 '너 몇 살이야?' 영어로 물어볼 때 무례하지 않게 말하는 법!”",
            "“딱 10초만 따라 해보세요. 한국인 토종 발음이 원어민 발음으로 바뀌는 마법!”"
          ],
          hookVisual: "화자 정면 외국인 표정 리액션 컷 -> X 표시 경고 후 원어민 입술 모양 2단 줌인",
          hookPsychology: "교과서 영어의 한계 탈피 및 '외국인 앞에서 당당하게 말하고 싶다'는 인정 욕구",
          cutSpeed: "평균 0.76초 (한국어 오답 vs 원어민 뉘앙스 대비 템포)",
          style: "스플릿 스크린(교과서 영어 vs 원어민 찐영어 비교) + 입 모양 발음 클로즈업 + 발음기호 음소 강조",
          bgm: "125 BPM 모던 로파이 팝 & 세련된 시티팝 인스트루멘탈",
          sfx: "오답 버저 땡! -> 정답 정체 종소리 딩동댕! -> 찰진 원어민 발음 팝 사운드",
          caption: "네온 라임(#A3E635) & 딥 네이비 + 핵심 표현 볼드 형광펜 하이라이트",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“외국인이 'What\\'s up?' 했는데 어색하게 얼어붙은 적 있으시죠? 딱 이 2글자만 하세요.”", visual: "외국인 질문과 당황한 표정 스플릿 스크린" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“한국 교과서로 배운 'I am doing well'은 너무 딱딱해서 원어민들이 듣고 깜짝 놀랍니다.”", visual: "교과서 문장에 커다란 빨간 X 표시" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“그냥 쿨하게 'Not much, you?'라고 받아쳐 보세요. 0.1초 만에 현지인 바이브로 대화가 이어집니다.”", visual: "원어민 입술 모양 클로즈업 및 억양 화살표 CG" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“원어민이 매일 쓰는 일상 반응 리액션 20문장은 고정댓글에 정리해뒀으니 캡처해서 외워두세요!”", visual: "고정댓글 화살표 + 저장 북마크 아이콘" }
          ],
          successFactors: [
            { title: "직관적인 교과서 vs 원어민 비교", desc: "한국인 누구나 아는 실수 포인트를 정확히 짚어 카타르시스 부여" },
            { title: "따라 하기 쉬운 2글자 해결책", desc: "'Not much'처럼 기억하기 쉬운 짧고 강렬한 솔루션" },
            { title: "스크린샷 저장률 35% 달성", desc: "고정댓글 문장 리스트로 일시정지 및 저장 지표 알고리즘 극대화" }
          ],
          viralReason: "🗣️ 교과서 탈피 원어민 뉘앙스 + 2글자 즉시 회화"
        }
      };

      var profile = CATEGORY_PROFILES[topicKey];
      if (!profile) {
        var kw = topicName || "숏폼";
        profile = {
          tag: kw + " 1티어 떡상",
          hookScripts: [
            "“" + kw + " 1년 차가 고백하는 충격적인 진실, 이것만 알아도 상위 1% 됩니다.”",
            "“" + kw + "할 때 99%가 무의식중에 저지르는 최악의 실수 TOP 3!”",
            "“딱 7일 동안 " + kw + " 이렇게만 따라 해보세요. 결과가 완전히 바뀝니다.”",
            "“전문가들도 극찬한 " + kw + " 1티어 성공 공식, 솔직히 저 혼자만 알고 싶었습니다.”"
          ],
          hookVisual: "화자 정면 120% 스냅 줌인 + 경고 사이렌 사운드 & 화면 흑백 반전 후 빨간 자막 쾅!",
          hookPsychology: kw + " 관련 손실 회피 편향(Loss Aversion) 및 0.1초 만에 스크롤을 멈추게 하는 호기심 갭(Information Gap)",
          cutSpeed: "평균 0.78초 (" + kw + " 핵심 정보 전달 최적 도파민 템포)",
          style: "세로 9:16 모바일 풀스크린 점프컷 + 단어 단위 바운스 자막 + 3D 인포그래픽 화살표",
          bgm: "128 BPM 숏폼 트렌딩 팝 & 딥 베이스 비트",
          sfx: "도입부 서브 베이스 쿵! -> 0.8초마다 Whoosh 컷전환음 -> 솔루션 공개 Ding!",
          caption: "중앙 형광 노랑 볼드체 폰트 (Gmarket Sans Bold) + 네온 시안 하이라이트",
          timelineScript: [
            { time: "00:00 - 00:03", stage: "초반 훅 (Hook)", text: "“" + kw + "에서 남들보다 10배 앞서가는 3초 치트키 공개합니다!”", visual: "화자 초밀착 줌인 + 사이렌 사운드" },
            { time: "00:03 - 00:12", stage: "문제 제기 (Problem)", text: "“대부분의 분들이 " + kw + "할 때 이렇게 착각하시는데, 이건 시간과 돈만 버리는 길입니다.”", visual: "실패 사례 B-roll 컷 0.8초마다 교차" },
            { time: "00:12 - 00:26", stage: "핵심 솔루션 (Solution)", text: "“진짜 비결은 바로 이 1가지입니다. 오늘부터 이것만 딱 적용해보세요.”", visual: "손가락으로 콕 짚으며 그래픽 3D 인포그래픽 노출" },
            { time: "00:26 - 00:35", stage: "행동 유도 (CTA)", text: "“구체적인 실천 매뉴얼은 고정댓글에 남겨뒀으니 지금 바로 확인하고 저장하세요!”", visual: "하단 고정댓글 화살표 + 저장 아이콘 점멸" }
          ],
          successFactors: [
            { title: "초반 2.5초 '시청 이탈 방지' 장치", desc: "시작하자마자 핵심 결론을 0.4초간 먼저 암시하여 호기심 극대화" },
            { title: "평균 컷 전환 0.78초 고속 리듬", desc: "한 장면에 1초 이상 머무르지 않고 클로즈업과 그래픽 자막을 교차" },
            { title: "자연스러운 댓글 논쟁 및 저장 유도", desc: "통념을 깨는 도발적인 발언과 고정댓글 팁으로 알고리즘 박제" }
          ],
          viralReason: "💡 손실 회피 + 0.78초 빠른 점프컷 & " + kw + " 특화 솔루션"
        };
      }

      var hookIdx = (rank - 1) % profile.hookScripts.length;
      var chosenHook = profile.hookScripts[hookIdx];
      if (title && title.length > 5) {
        var cleanTitle = title.replace(/^(\[[^\]]+\]|[🔥⚡🚀👑💎🏆]|\d+위)\s*/g, '');
        chosenHook = "“" + cleanTitle + " (솔직히 저 혼자만 알고 싶었습니다)”";
      }

      var cleanT = (title || topicName).replace(/^(\[[^\]]+\]|[🔥⚡🚀👑💎🏆]|\d+위)\s*/g, '');
      var ideas = [
        {
          title: cleanT + "할 때 무조건 피해야 할 최악의 실수 TOP 3",
          hook: "“이것만 피해도 상위 1% 됩니다. 충격 진실 공개합니다.”",
          plot: "3가지 흔한 실수 빠르게 나열 후 '진짜 해결책' 1개로 마무리"
        },
        {
          title: "딱 7일만 이렇게 따라 해보세요. 변화 없으면 채널 삭제합니다",
          hook: "“채널 걸고 장담하는데, 오늘부터 이것만 따라 하면 무조건 바뀝니다.”",
          plot: "극단적인 확신형 후킹으로 시청 지속 시간을 90% 이상 확보 후 단계별 가이드 제공"
        },
        {
          title: "전문가들도 극찬한 " + cleanT + " 1티어 꿀조합 대공개",
          hook: "“저 이거 올리면 매장당할 수도 있는데, 여러분 속는 꼴 못 봐서 깝니다.”",
          plot: "내부자/폭로자 포지션으로 신뢰도를 200% 끌어올리고 대안 해결책 제시"
        }
      ];

      return {
        hookAnalysis: {
          script: chosenHook,
          visual: profile.hookVisual,
          psychology: profile.hookPsychology
        },
        editingAnalysis: {
          cutSpeed: profile.cutSpeed,
          style: profile.style,
          bgm: profile.bgm,
          sfx: profile.sfx,
          caption: profile.caption
        },
        timelineScript: profile.timelineScript,
        successFactors: profile.successFactors,
        ideas: ideas,
        hookSummary: chosenHook,
        viralReason: profile.viralReason
      };
    }
"""

# Check if generateDetailedVideoAnalysis already exists
if "function generateDetailedVideoAnalysis" not in html:
    html = html.replace("    function generateVideosForFilter(", generator_code + "\n    function generateVideosForFilter(")
    print("Added generateDetailedVideoAnalysis")
else:
    print("generateDetailedVideoAnalysis already present")

# 3. Update generateVideosForFilter implementation
# Find inside generateVideosForFilter:
# `var realId = baseItem.id || VERIFIED_YT_IDS[(i - 1 + pOffset) % VERIFIED_YT_IDS.length];`
# and replace with authentic realYtId
old_id_line = "var realId = baseItem.id || VERIFIED_YT_IDS[(i - 1 + pOffset) % VERIFIED_YT_IDS.length];"
new_id_line = """var realYtId = baseItem.youtubeId || VERIFIED_YT_IDS[(poolIndex + (pOffset * 3) + (i * 7)) % VERIFIED_YT_IDS.length];
        var realId = realYtId;"""

if old_id_line in html:
    html = html.replace(old_id_line, new_id_line)
    print("Replaced realId assignment with realYtId")
else:
    print("old_id_line not found, checking...")

# Update realThumbnail:
old_thumb_line = 'var realThumbnail = baseItem.thumbnail || ("https://i.ytimg.com/vi/" + realId + "/hqdefault.jpg");'
new_thumb_line = 'var realThumbnail = "https://i.ytimg.com/vi/" + realYtId + "/hqdefault.jpg";'
if old_thumb_line in html:
    html = html.replace(old_thumb_line, new_thumb_line)
    print("Replaced realThumbnail with authentic YouTube thumbnail")

# Replace videos.push call to use generateDetailedVideoAnalysis
# Let's inspect the videos.push inside generateVideosForFilter
push_pattern = re.compile(r'videos\.push\(\{\s*id:\s*topicKey\s*\+\s*"-"\s*\+\s*timeFilter.*?\n\s*\}\);', re.DOTALL)
m_push = push_pattern.search(html)
if m_push:
    print("Found videos.push block in generateVideosForFilter")
    new_push_block = """var analysis = generateDetailedVideoAnalysis(baseItem, topicKey, i, timeFilter, topicName);

        videos.push({
          id: topicKey + "-" + timeFilter + "-" + platform + "-" + i,
          rank: i,
          title: fullTitle,
          platform: plat,
          subTopicId: subId,
          views: baseViews,
          viewsFormatted: viewsFormatted,
          likesFormatted: likesFormatted,
          duration: (20 + (i % 35)) + "s",
          author: authorDisplay,
          thumbnail: realThumbnail,
          youtubeId: realYtId,
          videoUrl: exactUrl,
          daysAgo: daysAgo,
          timeString: timeString,
          surge1d: surge1d,
          surge7d: surge7d,
          surgeScore: 800 - (i * 7) + (daysAgo === 0 ? 300 : daysAgo <= 7 ? 150 : 0),
          viralScore: Math.max(88, 99 - Math.floor(i / 8)),
          hookSummary: analysis.hookSummary,
          viralReason: analysis.viralReason,
          hookAnalysis: analysis.hookAnalysis,
          editingAnalysis: analysis.editingAnalysis,
          timelineScript: analysis.timelineScript,
          successFactors: analysis.successFactors,
          ideas: analysis.ideas
        });"""
    html = html[:m_push.start()] + new_push_block + html[m_push.end():]
    print("Updated videos.push to use generateDetailedVideoAnalysis!")
else:
    print("videos.push pattern not found!")

# 4. Update switchModalTab for "editing" to display SFX sound cues clearly
old_tab_editing = """      } else if (tab === "editing") {
        var html = '<div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">';
        html += '<div style="background:var(--surface-card); border:1px solid var(--surface-border); border-radius:14px; padding:14px;"><span style="font-size:11px; font-weight:800; color:var(--accent-cyan); display:block; margin-bottom:4px;">⏱️ 컷 전환 속도</span><div style="font-size:15px; font-weight:800; color:white;">' + v.editingAnalysis.cutSpeed + '</div></div>';
        html += '<div style="background:var(--surface-card); border:1px solid var(--surface-border); border-radius:14px; padding:14px;"><span style="font-size:11px; font-weight:800; color:var(--accent-pink); display:block; margin-bottom:4px;">🎬 편집 스타일</span><div style="font-size:12px; color:#e5e7eb;">' + v.editingAnalysis.style + '</div></div>';
        html += '<div style="background:var(--surface-card); border:1px solid var(--surface-border); border-radius:14px; padding:14px;"><span style="font-size:11px; font-weight:800; color:var(--accent-amber); display:block; margin-bottom:4px;">🎵 사운드 & BGM</span><div style="font-size:12px; color:#e5e7eb;">' + v.editingAnalysis.bgm + '</div></div>';
        html += '<div style="background:var(--surface-card); border:1px solid var(--surface-border); border-radius:14px; padding:14px;"><span style="font-size:11px; font-weight:800; color:#a78bfa; display:block; margin-bottom:4px;">📺 자막 스타일</span><div style="font-size:12px; color:#e5e7eb;">' + v.editingAnalysis.caption + '</div></div>';
        html += '</div>';
        pane.innerHTML = html;"""

new_tab_editing = """      } else if (tab === "editing") {
        var html = '<div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:12px;">';
        html += '<div style="background:var(--surface-card); border:1px solid var(--surface-border); border-radius:14px; padding:14px;"><span style="font-size:11px; font-weight:800; color:var(--accent-cyan); display:block; margin-bottom:4px;">⏱️ 컷 전환 속도</span><div style="font-size:14px; font-weight:800; color:white;">' + v.editingAnalysis.cutSpeed + '</div></div>';
        html += '<div style="background:var(--surface-card); border:1px solid var(--surface-border); border-radius:14px; padding:14px;"><span style="font-size:11px; font-weight:800; color:var(--accent-pink); display:block; margin-bottom:4px;">🎬 편집 스타일</span><div style="font-size:12px; color:#e5e7eb; line-height:1.5;">' + v.editingAnalysis.style + '</div></div>';
        html += '<div style="background:var(--surface-card); border:1px solid var(--surface-border); border-radius:14px; padding:14px;"><span style="font-size:11px; font-weight:800; color:var(--accent-amber); display:block; margin-bottom:4px;">🎵 노래 / BGM & BPM</span><div style="font-size:12px; color:#e5e7eb; line-height:1.5;">' + v.editingAnalysis.bgm + '</div></div>';
        html += '<div style="background:var(--surface-card); border:1px solid var(--surface-border); border-radius:14px; padding:14px;"><span style="font-size:11px; font-weight:800; color:#a78bfa; display:block; margin-bottom:4px;">📺 자막 스타일</span><div style="font-size:12px; color:#e5e7eb; line-height:1.5;">' + v.editingAnalysis.caption + '</div></div>';
        html += '</div>';
        if (v.editingAnalysis.sfx) {
          html += '<div style="background:rgba(245,158,11,0.08); border:1px solid rgba(245,158,11,0.25); border-radius:14px; padding:12px 14px;"><span style="font-size:11.5px; font-weight:800; color:var(--accent-amber); display:block; margin-bottom:4px;">🔊 효과음(SFX) 큐 포인트</span><div style="font-size:12px; color:#f3f4f6; line-height:1.5;">' + v.editingAnalysis.sfx + '</div></div>';
        }
        pane.innerHTML = html;"""

if old_tab_editing in html:
    html = html.replace(old_tab_editing, new_tab_editing)
    print("Updated switchModalTab for editing/music/SFX")

with open('3_바이럴분석_SaaS_ViralScope/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Step 2 completed successfully!")
