import { NextRequest, NextResponse } from "next/server";
import { generateDeepVideoAnalysis } from "@/lib/gemini";
import { supabaseAdmin, isSupabaseConfigured } from "@/lib/supabase";
import { ViralVideo } from "@/types";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { video, userId } = body as { video: ViralVideo; userId?: string };

    if (!video || !video.id) {
      return NextResponse.json({ error: "분석할 영상 정보가 누락되었습니다." }, { status: 400 });
    }

    // 1. Credit Check & Deduction (if user is authenticated)
    if (userId && isSupabaseConfigured()) {
      const { data: profile, error: profileErr } = await supabaseAdmin
        .from("profiles")
        .select("credits, subscription_status")
        .eq("id", userId)
        .single();

      if (profile && profile.subscription_status !== "pro") {
        if (profile.credits <= 0) {
          return NextResponse.json(
            {
              error: "무료 크레딧(3회)을 모두 소진하셨습니다.",
              requireSubscription: true,
              checkoutUrl: "/api/stripe/checkout"
            },
            { status: 402 }
          );
        }

        // Deduct 1 credit
        await supabaseAdmin
          .from("profiles")
          .update({ credits: profile.credits - 1 })
          .eq("id", userId);

        // Record credit transaction
        await supabaseAdmin.from("credit_transactions").insert({
          user_id: userId,
          amount: -1,
          balance_after: profile.credits - 1,
          reason: "DEEP_DIVE_ANALYSIS"
        });
      }
    }

    // 2. Execute Gemini Deep Dive Analysis
    const analysis = await generateDeepVideoAnalysis(video);

    // 3. Cache analysis in Supabase if configured
    if (isSupabaseConfigured()) {
      await supabaseAdmin.from("video_analyses").upsert({
        video_id: video.id,
        hook_text: analysis.hookAnalysis.hookScript,
        hook_visual_action: analysis.hookAnalysis.visualAction,
        hook_psychology: analysis.hookAnalysis.psychologicalTrigger,
        success_factors: analysis.successFactors,
        editing_tempo: analysis.editingAnalysis.cutSpeed,
        editing_style: analysis.editingAnalysis,
        timeline_script: analysis.timelineScript,
        creator_action_plan: analysis.actionPlan
      }, { onConflict: "video_id" });
    }

    return NextResponse.json({
      success: true,
      analysis
    });
  } catch (err: any) {
    console.error("[API Deep Dive Error]:", err);
    return NextResponse.json({ error: "AI 심층 분석 생성 중 오류가 발생했습니다." }, { status: 500 });
  }
}
