import { NextRequest, NextResponse } from "next/server";
import { analyzeTopicWithGemini } from "@/lib/gemini";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { keyword } = body;

    if (!keyword || typeof keyword !== "string" || !keyword.trim()) {
      return NextResponse.json(
        { error: "검색할 주제 키워드를 올바르게 입력해주세요." },
        { status: 400 }
      );
    }

    const result = await analyzeTopicWithGemini(keyword.trim());
    return NextResponse.json(result);
  } catch (error: any) {
    console.error("API Analyze Error:", error);
    return NextResponse.json(
      { error: "영상 바이럴 분석 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요." },
      { status: 500 }
    );
  }
}
