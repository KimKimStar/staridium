import { NextRequest, NextResponse } from "next/server";
import { stripe, PRO_PLAN_CONFIG } from "@/lib/stripe";

export async function POST(req: NextRequest) {
  try {
    const origin = req.headers.get("origin") || process.env.NEXT_PUBLIC_APP_URL || "http://localhost:3000";
    const body = await req.json().catch(() => ({}));
    const { userId = "demo_user", email = "creator@viralscope.ai" } = body;

    // Check if Stripe Secret Key is live or placeholder
    const isMockStripe = !process.env.STRIPE_SECRET_KEY || process.env.STRIPE_SECRET_KEY.includes("placeholder");

    if (isMockStripe) {
      // Local dev simulation mode: redirect to success with session mock
      return NextResponse.json({
        url: `${origin}/?payment=success&mock=true&session_id=mock_sub_${Date.now()}&userId=${userId}`,
        isMock: true,
      });
    }

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ["card"],
      line_items: [
        {
          price_data: {
            currency: "krw",
            product_data: {
              name: PRO_PLAN_CONFIG.name,
              description: PRO_PLAN_CONFIG.description,
              images: [
                "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80",
              ],
            },
            unit_amount: PRO_PLAN_CONFIG.priceKrw, // 5,000 KRW
            recurring: {
              interval: PRO_PLAN_CONFIG.interval, // 'month'
            },
          },
          quantity: 1,
        },
      ],
      mode: "subscription",
      customer_email: email,
      metadata: {
        userId: userId,
        planId: PRO_PLAN_CONFIG.id,
      },
      success_url: `${origin}/?payment=success&session_id={CHECKOUT_SESSION_ID}&userId=${userId}`,
      cancel_url: `${origin}/?payment=cancel`,
    });

    return NextResponse.json({ url: session.url });
  } catch (error: any) {
    console.error("[Stripe Checkout Error]:", error);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
