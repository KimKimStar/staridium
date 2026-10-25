"use client";

import React from "react";
import { ExternalLink, Sparkles } from "lucide-react";

interface AdBannerProps {
  type?: "in-feed" | "banner";
  className?: string;
}

export function AdBanner({ type = "banner", className = "" }: AdBannerProps) {
  if (type === "in-feed") {
    return (
      <div
        className={`relative flex flex-col rounded-2xl bg-slate-900/60 border border-dashed border-slate-700/80 hover:border-slate-600 transition-all duration-300 p-4 justify-between backdrop-blur-sm group ${className}`}
      >
        {/* Subtle Advertisement Label */}
        <div className="flex items-center justify-between pb-3 border-b border-slate-800">
          <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 bg-slate-800/80 px-2 py-0.5 rounded-md border border-slate-700/50">
            Advertisement
          </span>
          <span className="text-[10px] text-slate-500 font-medium">스폰서</span>
        </div>

        {/* Ad Body (In-feed Native Card) */}
        <div className="flex flex-col items-center justify-center text-center my-6 gap-3">
          <div className="w-14 h-14 rounded-2xl bg-gradient-to-tr from-blue-600/30 to-violet-600/30 border border-blue-500/30 flex items-center justify-center text-blue-400 group-hover:scale-105 transition-transform">
            <Sparkles className="w-7 h-7 text-blue-400" />
          </div>
          <div className="flex flex-col gap-1">
            <h4 className="text-sm font-bold text-slate-200">
              AI 숏폼 원클릭 캡션 자동 생성기
            </h4>
            <p className="text-xs text-slate-400 line-clamp-3 max-w-[220px]">
              9:16 모바일 화면에 최적화된 애니메이션 자막과 효과음을 10초 만에 생성하세요.
            </p>
          </div>
        </div>

        {/* Ad Action Link */}
        <a
          href="https://google.com"
          target="_blank"
          rel="noopener noreferrer"
          className="w-full py-2 px-3 rounded-xl bg-slate-800/90 hover:bg-slate-750 text-slate-300 hover:text-white text-xs font-semibold flex items-center justify-center gap-1.5 border border-slate-700 transition-colors"
        >
          <span>스폰서 링크 바로가기</span>
          <ExternalLink className="w-3.5 h-3.5 text-slate-400" />
        </a>
      </div>
    );
  }

  // Horizontal Banner (For above/below text hook in detail modal)
  return (
    <div
      className={`w-full rounded-xl bg-slate-900/60 border border-slate-700/60 p-3.5 flex flex-col sm:flex-row items-center justify-between gap-3 ${className}`}
    >
      <div className="flex items-center gap-3 w-full sm:w-auto">
        <span className="text-[9px] font-bold uppercase tracking-wider text-slate-500 bg-slate-800 px-1.5 py-0.5 rounded border border-slate-700/60 flex-shrink-0">
          Advertisement
        </span>
        <div className="flex flex-col">
          <div className="text-xs font-bold text-slate-200">
            [스폰서] 크리에이터 전용 고수익 AI 영상 편집 툴킷 14일 무료 체험
          </div>
          <div className="text-[11px] text-slate-400">
            알고리즘 추천 확률을 극대화하는 0~3초 후킹 프리셋 50종 즉시 다운로드
          </div>
        </div>
      </div>
      <a
        href="https://google.com"
        target="_blank"
        rel="noopener noreferrer"
        className="px-3 py-1.5 rounded-lg bg-blue-600/20 hover:bg-blue-600/30 text-blue-400 border border-blue-500/30 text-xs font-bold flex items-center gap-1 flex-shrink-0 transition-colors"
      >
        <span>자세히 보기</span>
        <ExternalLink className="w-3 h-3" />
      </a>
    </div>
  );
}
