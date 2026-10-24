import { NextRequest, NextResponse } from "next/server";
import { stripe, PRO_PLAN_CONFIG } from "@/lib/stripe";

export async function POST(req: NextRequest) {
  try {
    const origin = req.headers.get("origin") || process.env.NEXT_PUBLIC_APP_URL || "http://localhost:3000";
    const body = await req.json().catch(() => ({}));
    const { userId, email } = body;

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ["card"],
      line_items: [
        {
          price_data: {
            currency: "krw",
            product_data: {
              name: PRO_PLAN_CONFIG.name,
              description: PRO_PLAN_CONFIG.description,
              images: ["https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80"]
            },
            unit_amount: PRO_PLAN_CONFIG.priceKrw, // 19,000 KRW
            recurring: {
              interval: "month"
            }
          },
          quantity: 1
        }
      ],
      mode: "subscription",
      customer_email: email,
      metadata: {
        userId: userId || "guest_creator"
      },
      success_url: `${origin}/?payment=success&session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${origin}/?payment=cancel`
    });

    return NextResponse.json({ url: session.url });
  } catch (error: any) {
    console.error("[Stripe Checkout Error]:", error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
