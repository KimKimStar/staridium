import Stripe from "stripe";

const stripeSecretKey = process.env.STRIPE_SECRET_KEY || "sk_test_placeholder_viralscope";

export const stripe = new Stripe(stripeSecretKey, {
  apiVersion: "2023-10-16",
  typescript: true,
});

export const PRO_PLAN_CONFIG = {
  id: "pro_monthly_5000",
  name: "ViralScope AI 모션 스왑 Pro 정기구독",
  priceKrw: 5000, // 월 5,000원 대중적 단일 요금제
  interval: "month" as const,
  description: "타겟 숏폼 모션 뼈대 추출 + 내 캐릭터 스왑 + 3초 훅 자막 오버레이 무제한 렌더링",
  features: [
    "AI 모션 스왑 숏폼 템플릿 렌더링 무제한 이용",
    "타겟 숏폼 모션 뼈대(Pose/Skeleton) 무손실 추출",
    "사용자 셀카/캐릭터/아바타 9:16 실사 애니메이팅",
    "초반 3초 시선강탈 훅(Hook) 자막 FFmpeg 자동 오버레이",
    "1080x1920 세로 풀HD 고화질 워터마크 없는 무제한 다운로드",
    "상업적 이용 100% 가능 (저작권 침해 없는 순수 모션 복제)",
  ],
};
