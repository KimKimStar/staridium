import Stripe from "stripe";

const stripeSecretKey = process.env.STRIPE_SECRET_KEY || "sk_test_placeholder";

export const stripe = new Stripe(stripeSecretKey, {
  apiVersion: "2023-10-16",
  typescript: true,
});

export const PRO_PLAN_CONFIG = {
  name: "ViralScope Pro",
  priceKrw: 5000,
  interval: "month",
  description: "무제한 숏폼 바이럴 분석 & AI 떡상 기획/대본 생성기",
  features: [
    "무제한 키워드 검색 및 떡상 영상 크롤링",
    "쇼츠 / 릴스 / 틱톡 플랫폼별 조회수 순 랭킹 분석",
    "초반 3초 훅 & 시각 연출 AI 심층 해부",
    "타임라인별 대본 스크립트 & 컷 편집 템플릿",
    "내 채널 맞춤형 떡상 기획안 3선 & AI 프롬프트 생성",
    "원클릭 대본 복사 및 기획안 PDF 내보내기",
  ],
};
