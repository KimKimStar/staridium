import { NextRequest, NextResponse } from "next/server";
import { stripe } from "@/lib/stripe";
import { supabaseAdmin, isSupabaseConfigured } from "@/lib/supabase";

export async function POST(req: NextRequest) {
  const body = await req.text();
  const sig = req.headers.get("stripe-signature");
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

  let event;
  try {
    if (webhookSecret && sig) {
      event = stripe.webhooks.constructEvent(body, sig, webhookSecret);
    } else {
      event = JSON.parse(body);
    }
  } catch (err: any) {
    console.error("[Stripe Webhook Verification Failed]:", err.message);
    return NextResponse.json({ error: "Webhook Error" }, { status: 400 });
  }

  // Handle Successful Subscription Checkout
  if (event.type === "checkout.session.completed") {
    const session = event.data.object as any;
    const userId = session.metadata?.userId;
    const customerId = session.customer;
    const subscriptionId = session.subscription;

    console.log(`[Stripe Webhook] Payment Successful for User: ${userId}`);

    if (userId && isSupabaseConfigured()) {
      await supabaseAdmin.from("profiles").update({
        subscription_status: "pro",
        stripe_customer_id: customerId,
        stripe_subscription_id: subscriptionId,
        updated_at: new Date().toISOString()
      }).eq("id", userId);

      await supabaseAdmin.from("credit_transactions").insert({
        user_id: userId,
        amount: 999999,
        balance_after: 999999,
        reason: "STRIPE_PRO_UPGRADE"
      });
    }
  }

  return NextResponse.json({ received: true });
}
