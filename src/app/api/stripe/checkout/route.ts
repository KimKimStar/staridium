import { NextRequest, NextResponse } from "next/server";
import { stripe } from "@/lib/stripe";

export async function POST(req: NextRequest) {
  try {
    const origin = req.headers.get("origin") || process.env.NEXT_PUBLIC_APP_URL || "http://localhost:3000";
    const apiKey = process.env.STRIPE_SECRET_KEY;

    // 실제 Stripe 키가 구성되어 있지 않은 경우의 스마트 시뮬레이션 처리
    if (!apiKey || apiKey.startsWith("sk_test_placeholder")) {
      return NextResponse.json({
        mock: true,
        url: `${origin}/?payment=success&credits=unlimited`,
        message: "Stripe 테스트 모드로 결제 완료가 시뮬레이션되었습니다.",
      });
    }

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ["card"],
      line_items: [
        {
          price_data: {
            currency: "krw",
            product_data: {
              name: "ViralScope Pro (월간 구독)",
              description: "AI 숏폼 떡상 바이럴 분석 및 기획/대본 무제한 생성",
              images: ["https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400&q=80"],
            },
            unit_amount: 5000,
            recurring: {
              interval: "month",
            },
          },
          quantity: 1,
        },
      ],
      mode: "subscription",
      success_url: `${origin}/?payment=success&credits=unlimited`,
      cancel_url: `${origin}/?payment=cancelled`,
      metadata: {
        plan: "pro_5000_krw",
      },
    });

    return NextResponse.json({ url: session.url });
  } catch (error: any) {
    console.error("Stripe Checkout Error:", error);
    return NextResponse.json(
      { error: error.message || "결제 세션 생성 중 오류가 발생했습니다." },
      { status: 500 }
    );
  }
}
