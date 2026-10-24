import { NextRequest, NextResponse } from "next/server";
import { stripe } from "@/lib/stripe";
import { upgradeUserToPro } from "@/lib/userStore";

export async function POST(req: NextRequest) {
  const body = await req.text();
  const sig = req.headers.get("stripe-signature");
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

  let event: any;
  try {
    if (webhookSecret && sig) {
      event = stripe.webhooks.constructEvent(body, sig, webhookSecret);
    } else {
      event = JSON.parse(body);
    }
  } catch (err: any) {
    console.error("[Stripe Webhook Verification Failed]:", err.message);
    return NextResponse.json({ error: "Webhook Error: " + err.message }, { status: 400 });
  }

  // Handle Event Types
  switch (event.type) {
    case "checkout.session.completed": {
      const session = event.data.object as any;
      const userId = session.metadata?.userId || "demo_user";
      const customerId = session.customer;
      const subscriptionId = session.subscription;

      console.log(`[Stripe Webhook] 5,000 KRW Pro Subscription Success for User: ${userId}`);

      // Upgrade user status to Pro (unlimited credits)
      await upgradeUserToPro(userId, customerId, subscriptionId);
      break;
    }

    case "customer.subscription.updated": {
      const sub = event.data.object as any;
      console.log(`[Stripe Webhook] Subscription Updated: ${sub.id}, Status: ${sub.status}`);
      break;
    }

    case "customer.subscription.deleted": {
      const sub = event.data.object as any;
      console.log(`[Stripe Webhook] Subscription Cancelled: ${sub.id}`);
      // If needed, reset status back to free
      break;
    }

    default:
      console.log(`[Stripe Webhook] Unhandled event type: ${event.type}`);
  }

  return NextResponse.json({ received: true, eventType: event.type });
}
