import { supabaseAdmin, isSupabaseConfigured } from "./supabase";

export interface UserAccount {
  id: string;
  email: string;
  name: string;
  credits: number; // 신규 가입 시 1 크레딧 무료
  status: "free" | "pro"; // 'pro'는 무제한 이용
  stripeCustomerId?: string;
  stripeSubscriptionId?: string;
  createdAt: string;
  updatedAt: string;
}

// In-Memory fallback store for seamless local execution
const localUserMemory: Record<string, UserAccount> = {
  demo_user: {
    id: "demo_user",
    email: "creator@viralscope.ai",
    name: "도전하는 크리에이터",
    credits: 1, // 1회 무료 체험
    status: "free",
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  },
};

export async function getUserAccount(userId: string = "demo_user", email?: string): Promise<UserAccount> {
  // 1. Try Supabase if configured
  if (isSupabaseConfigured()) {
    try {
      const { data, error } = await supabaseAdmin
        .from("profiles")
        .select("*")
        .eq("id", userId)
        .maybeSingle();

      if (data && !error) {
        return {
          id: data.id,
          email: data.email || email || "creator@viralscope.ai",
          name: data.full_name || "크리에이터",
          credits: data.credits ?? 1,
          status: data.subscription_status === "pro" ? "pro" : "free",
          stripeCustomerId: data.stripe_customer_id,
          stripeSubscriptionId: data.stripe_subscription_id,
          createdAt: data.created_at,
          updatedAt: data.updated_at,
        };
      }
    } catch (e) {
      console.warn("[UserStore] Supabase query fallback to local store:", e);
    }
  }

  // 2. Local fallback
  if (!localUserMemory[userId]) {
    localUserMemory[userId] = {
      id: userId,
      email: email || `${userId}@viralscope.ai`,
      name: "신규 크리에이터",
      credits: 1, // 신규 유저 1회 무료 제공
      status: "free",
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
    };
  }

  return localUserMemory[userId];
}

export async function deductUserCredit(userId: string = "demo_user"): Promise<{ success: boolean; remainingCredits: number; status: "free" | "pro" }> {
  const account = await getUserAccount(userId);

  // Pro users have unlimited access
  if (account.status === "pro") {
    return { success: true, remainingCredits: 999999, status: "pro" };
  }

  // Check free credits
  if (account.credits <= 0) {
    return { success: false, remainingCredits: 0, status: "free" };
  }

  const newCredits = account.credits - 1;

  // Update Supabase if configured
  if (isSupabaseConfigured()) {
    try {
      await supabaseAdmin
        .from("profiles")
        .update({ credits: newCredits, updated_at: new Date().toISOString() })
        .eq("id", userId);

      await supabaseAdmin.from("credit_transactions").insert({
        user_id: userId,
        amount: -1,
        balance_after: newCredits,
        reason: "MOTION_SWAP_RENDER",
      });
    } catch (e) {
      console.warn("[UserStore] Supabase credit deduction error:", e);
    }
  }

  // Update local memory
  if (localUserMemory[userId]) {
    localUserMemory[userId].credits = newCredits;
    localUserMemory[userId].updatedAt = new Date().toISOString();
  }

  return { success: true, remainingCredits: newCredits, status: "free" };
}

export async function upgradeUserToPro(userId: string, customerId?: string, subscriptionId?: string): Promise<UserAccount> {
  const account = await getUserAccount(userId);
  account.status = "pro";
  account.credits = 999999;
  account.stripeCustomerId = customerId;
  account.stripeSubscriptionId = subscriptionId;
  account.updatedAt = new Date().toISOString();

  if (isSupabaseConfigured()) {
    try {
      await supabaseAdmin
        .from("profiles")
        .update({
          subscription_status: "pro",
          credits: 999999,
          stripe_customer_id: customerId,
          stripe_subscription_id: subscriptionId,
          updated_at: new Date().toISOString(),
        })
        .eq("id", userId);

      await supabaseAdmin.from("credit_transactions").insert({
        user_id: userId,
        amount: 999999,
        balance_after: 999999,
        reason: "STRIPE_PRO_UPGRADE_5000",
      });
    } catch (e) {
      console.warn("[UserStore] Supabase upgrade error:", e);
    }
  }

  localUserMemory[userId] = account;
  return account;
}
