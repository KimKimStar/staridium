import Stripe from "stripe";

const stripeSecretKey = process.env.STRIPE_SECRET_KEY || "sk_test_placeholder_viralscope";

export const stripe = new Stripe(stripeSecretKey, {
  apiVersion: "2023-10-16",
  typescript: true,
});

export const PRO_PLAN_CONFIG = {
  name: "ViralScope Pro 무제한 플랜",
  priceKrw: 19000,
  interval: "month",
  description: "무제한 숏폼 바이럴 해부학 & AI 떡상 기획/대본 생성기",
  features: [
    "무제한 키워드 검색 및 전 플랫폼 떡상 영상 크롤링",
    "쇼츠 / 릴스 / 틱톡 플랫폼별 조회수 순 정렬 (1일~역대)",
    "초반 3초 훅(Hook) & 시청 이탈 방지 AI 심층 해부",
    "타임라인별 대본 스크립트 & 컷 편집 템플릿 제공",
    "내 채널 맞춤형 떡상 기획안 3선 & 전용 AI 프롬프트 생성",
    "원클릭 대본 복사 및 기획안 내보내기",
  ],
};
