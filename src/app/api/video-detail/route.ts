import { NextRequest, NextResponse } from "next/server";
import { generateDeepVideoAnalysis } from "@/lib/gemini";
import { ViralVideo } from "@/types";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { video }: { video: ViralVideo } = body;

    if (!video || !video.id) {
      return NextResponse.json(
        { error: "분석할 영상 데이터가 유효하지 않습니다." },
        { status: 400 }
      );
    }

    const detailAnalysis = await generateDeepVideoAnalysis(video);
    return NextResponse.json(detailAnalysis);
  } catch (error: any) {
    console.error("API Video-Detail Error:", error);
    return NextResponse.json(
      { error: "영상 상세 해부 중 오류가 발생했습니다." },
      { status: 500 }
    );
  }
}
