import { NextRequest, NextResponse } from "next/server";
import { stripe } from "@/lib/stripe";

export async function POST(req: NextRequest) {
  const payload = await req.text();
  const sig = req.headers.get("stripe-signature");
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

  let event;

  try {
    if (webhookSecret && sig) {
      event = stripe.webhooks.constructEvent(payload, sig, webhookSecret);
    } else {
      event = JSON.parse(payload);
    }
  } catch (err: any) {
    console.error(`Webhook signature verification failed:`, err.message);
    return NextResponse.json({ error: "Webhook Error" }, { status: 400 });
  }

  // 결제 완료 이벤트 핸들링
  switch (event.type) {
    case "checkout.session.completed": {
      const session = event.data.object;
      console.log("💳 결제 완료 세션:", session.id, "고객 이메일:", session.customer_email);
      // DB가 연결되어 있다면 사용자 계정에 Pro 구독 플래그 및 무제한 크레딧 업데이트
      break;
    }
    case "invoice.payment_succeeded": {
      const invoice = event.data.object;
      console.log("✅ 정기 구독 결제 성공:", invoice.id);
      break;
    }
    case "customer.subscription.deleted": {
      console.log("⚠️ 구독 취소됨:", event.data.object.id);
      break;
    }
    default:
      console.log(`기타 Stripe 이벤트 수신: ${event.type}`);
  }

  return NextResponse.json({ received: true });
}
