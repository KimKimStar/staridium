import { NextRequest, NextResponse } from "next/server";
import { getUserAccount } from "@/lib/userStore";

export async function GET(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url);
    const userId = searchParams.get("userId") || "demo_user";

    const user = await getUserAccount(userId);

    return NextResponse.json({
      userId: user.id,
      email: user.email,
      credits: user.credits,
      status: user.status,
      isPro: user.status === "pro",
    });
  } catch (err: any) {
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
