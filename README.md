# 🔥 ViralScope AI - 숏폼 바이럴 분석 & 기획 대시보드 (Pre-production SaaS)

> **"3초 만에 이탈하는 시청자를 사로잡는 AI 바이럴 해부학"**  
> 숏폼(유튜브 쇼츠, 인스타그램 릴스, 틱톡) 크리에이터와 마케터들이 기획/구성/편집의 고통을 덜 수 있도록 도와주는 올인원 Pre-production SaaS입니다.

---

## 🌟 핵심 기능 및 해결 과제

1. **전 플랫폼(쇼츠, 릴스, 틱톡) 떡상 영상 크롤링 & 조회수 순 정렬**
   - 사용자가 주제(예: 다이어트, 주식, 뷰티, 레시피 등)를 입력하면 각 플랫폼에서 수백만 조회수를 기록한 떡상 레퍼런스를 수집/정렬합니다.
2. **AI 자동 하위 주제(서브토픽) 탭 분류**
   - 큰 주제 키워드를 3~4개의 세부 뾰족한 서브토픽으로 자동 분류하여 탭으로 제공합니다. (예: "다이어트" -> "식단/간헐적단식", "홈트 5분 루틴", "멘탈 관리", "영양제/꿀템")
3. **지루하지 않은 프리미엄 스켈레톤 로딩**
   - Gemini AI가 분석을 수행하는 동안 실시간 파이프라인 단계 메시지와 네온 시머(Shimmer) 애니메이션을 노출합니다.
4. **Gemini AI 기반 심층 바이럴 해부 모달**
   - ① **초반 3초 훅(Hook) 대사** & 시각적 화면 연출 & 시청자 심리 트리거 분석
   - ② **알고리즘 시청 지속시간 성공 요인** & 댓글 유도 장치
   - ③ **평균 컷 전환 속도(Pacing)**, 폰트/자막 스타일, 사운드 BGM 템포
   - ④ **전체 타임라인별 대사(스크립트)** (0~3초 훅 -> 문제 제기 -> 해결책 -> CTA)
   - ⑤ **[크리에이터 고민 해결 솔루션] "내 채널 즉시 적용 떡상 기획안 3선"** & 초단위 컷 편집 가이드 & 원클릭 AI 대본 프롬프트
5. **비즈니스 모델 & Stripe 수익화 (월 5,000원)**
   - 신규 접속 시 3회 무료 크레딧 제공
   - 소진 시 월 5,000원 Pro 무제한 플랜 결제 모달 유도 및 Stripe Checkout 연동

---

## 🏗️ 전체 디렉토리 구조 (폴더 아키텍처)

```
3_바이럴분석_SaaS_ViralScope/
│
├── 📂 public/                             # 정적 자산 및 아이콘
├── 📂 src/
│   ├── 📂 app/                            # Next.js 14 App Router
│   │   ├── 📂 api/
│   │   │   ├── 📂 analyze/
│   │   │   │   └── route.ts               # Gemini API 키워드 분석 & 서브토픽/영상 추출 API
│   │   │   ├── 📂 video-detail/
│   │   │   │   └── route.ts               # Gemini 심층 영상 해부 & 기획안 생성 API
│   │   │   └── 📂 stripe/
│   │   │       ├── 📂 checkout/
│   │   │       │   └── route.ts           # Stripe 월 5,000원 Checkout 세션 생성 API
│   │   │       └── 📂 webhook/
│   │   │           └── route.ts           # Stripe 결제 완료 웹훅 처리 API
│   │   ├── globals.css                    # 네온 다크 테마 및 애니메이션 CSS
│   │   ├── layout.tsx                     # 전역 메타데이터 및 HTML 레이아웃
│   │   └── page.tsx                       # 대시보드 메인 페이지 (전체 상태 및 뷰 통합)
│   │
│   ├── 📂 components/                     # 핵심 UI 컴포넌트 모음
│   │   ├── Header.tsx                     # 상단 바, 로고, 크레딧 뱃지, Pro 업그레이드 버튼
│   │   ├── SearchBar.tsx                  # 네온 검색창 & 실시간 인기 검색어 칩
│   │   ├── SubTopicTabs.tsx               # 하위 카테고리 자동 탭 & 플랫폼/정렬 필터 & 인사이트 바
│   │   ├── VideoCard.tsx                  # 9:13 썸네일 카드, 바이럴 스코어, 3초 훅 미리보기
│   │   ├── VideoList.tsx                  # 카드 반응형 그리드 렌더러
│   │   ├── SkeletonLoader.tsx             # 실시간 AI 단계별 로딩 애니메이션
│   │   ├── AnalysisModal.tsx              # [핵심] 3초 훅 / 편집법 / 타임라인 / 기획안 3선 모달
│   │   └── PricingModal.tsx               # 월 5,000원 Pro 구독 유도 및 Stripe 결제 모달
│   │
│   ├── 📂 lib/                            # 유틸리티 & SDK 인스턴스
│   │   ├── gemini.ts                      # Gemini 1.5/2.0 API 호출 & 스마트 Fallback 엔진
│   │   └── stripe.ts                      # Stripe SDK 인스턴스 및 Pro 요금제 설정
│   │
│   └── 📂 types/
│       └── index.ts                       # ViralVideo, SubTopic, VideoDetailAnalysis 타입 정의
│
├── .env.example                           # 환경변수 템플릿
├── package.json                           # 프로젝트 의존성 설정
├── tsconfig.json                          # TypeScript 컴파일러 설정
├── tailwind.config.ts                     # Tailwind CSS 커스텀 테마 설정
├── postcss.config.js                      # PostCSS 설정
├── preview.html                           # 브라우저 즉시 체험용 단독형 인터랙티브 웹 앱
├── run_saas_preview.bat                   # 더블클릭 프리뷰 실행기
└── run_nextjs.bat                         # Next.js 로컬 서버 구동기
```

---

## 🚀 빠른 실행 및 사용 방법

### 방법 1. 즉시 브라우저에서 대시보드 체험하기 (권장)
- `run_saas_preview.bat` 파일을 더블클릭하거나 루트의 `⚡ [실행] 3_바이럴분석_SaaS.bat`을 더블클릭합니다.
- 설치 과정 없이 브라우저에서 환상적인 비주얼의 대시보드가 즉시 열립니다.
- 키워드("다이어트", "주식", "뷰티" 등) 검색, 하위 탭 전환, 틱톡/릴스/쇼츠 필터, 영상 클릭 후 기획안 복사, 3회 크레딧 차감 후 Pro 결제 모달까지 모든 기능이 즉시 인터랙티브하게 동작합니다.

### 방법 2. Next.js 풀스택 개발 서버 구동 (Node.js 환경)
1. **Node.js 설치**: [nodejs.org](https://nodejs.org/)에서 LTS 버전을 설치합니다.
2. **API 키 설정 (선택사항)**:
   - `.env.example` 파일을 복사하여 `.env.local`로 이름을 변경합니다.
   - 보유하신 Google Gemini API 키 및 Stripe 키를 입력합니다. (키가 없어도 지능형 엔진으로 완벽 작동)
3. **서버 시작**:
   - `run_nextjs.bat`을 더블클릭합니다. 자동으로 패키지 설치(`npm install`) 후 `http://localhost:3000`이 실행됩니다.
