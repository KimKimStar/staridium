import { NextRequest, NextResponse } from "next/server";
import { getUserAccount, deductUserCredit } from "@/lib/userStore";
import { runMotionSwapReplicate } from "@/lib/replicate";
import { overlay3SecondHookSubtitle } from "@/lib/ffmpeg";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const {
      targetUrl,
      userImage,
      hookText,
      userId = "demo_user",
    } = body;

    // 1. 유효성 검사
    if (!targetUrl || !targetUrl.trim()) {
      return NextResponse.json(
        { error: "벤치마킹할 타겟 숏폼 URL을 입력해주세요." },
        { status: 400 }
      );
    }

    if (!userImage) {
      return NextResponse.json(
        { error: "스왑할 사용자 셀카 또는 캐릭터 이미지를 업로드해주세요." },
        { status: 400 }
      );
    }

    // 2. 비즈니스 모델 및 사용자 크레딧 검증
    const user = await getUserAccount(userId);

    // 무료 크레딧을 모두 소진한 비구독(free) 유저 차단 -> Stripe 결제 유도
    if (user.status !== "pro" && user.credits <= 0) {
      return NextResponse.json(
        {
          requiresUpgrade: true,
          error: "무료 체험 크레딧(1회)을 모두 사용하셨습니다. 월 5,000원에 무제한 모션 스왑 기능을 이용해보세요!",
          userStatus: user.status,
          remainingCredits: 0,
        },
        { status: 402 } // Payment Required
      );
    }

    console.log(`[MotionSwap API] 유저(${userId}) 렌더링 요청: 크레딧=${user.credits}, 상태=${user.status}`);

    // 3. Replicate API 연동: 모션 뼈대 추출 및 이미지 애니메이팅
    const replicatedVideoUrl = await runMotionSwapReplicate({
      targetVideoUrl: targetUrl,
      userImageUrl: userImage,
      prompt: "Full-body vertical 9:16 motion animated character, perfect motion sync, hyperrealistic shorts",
    });

    // 4. FFmpeg 연동: 3초 훅 텍스트 자막 오버레이 및 9:16 인코딩
    const finalRenderedVideo = await overlay3SecondHookSubtitle({
      inputVideoUrl: replicatedVideoUrl,
      hookText: hookText || "🔥 3초 만에 시선 끄는 바이럴 숏폼!",
    });

    // 5. 렌더링 성공 후 크레딧 차감 (Pro 유저는 무제한 유지)
    const deductionResult = await deductUserCredit(userId);

    return NextResponse.json({
      success: true,
      resultVideoUrl: finalRenderedVideo,
      remainingCredits: deductionResult.remainingCredits,
      isPro: deductionResult.status === "pro",
      message: "AI 모션 스왑 및 3초 훅 자막 합성이 성공적으로 완료되었습니다!",
    });
  } catch (error: any) {
    console.error("[MotionSwap API Error]:", error);
    return NextResponse.json(
      { error: error.message || "영상 처리 중 오류가 발생했습니다." },
      { status: 500 }
    );
  }
}
