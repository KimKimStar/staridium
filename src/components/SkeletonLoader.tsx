"use client";

import React, { useEffect, useState } from "react";
import { Sparkles, Bot, Film } from "lucide-react";

export const SkeletonLoader: React.FC = () => {
  const steps = [
    "유튜브 쇼츠 · 인스타 릴스 · 틱톡 알고리즘 전수 스캔 중...",
    "초반 3초 후킹 공식 및 시청 지속시간 이탈 방지 장치 분석 중...",
    "컷 전환 속도, 폰트 스타일, 배경음악(BGM) 템포 해부 중...",
    "크리에이터 맞춤형 떡상 기획안 및 AI 대본 프롬프트 구성 중...",
  ];

  const [currentStep, setCurrentStep] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentStep((prev) => (prev + 1) % steps.length);
    }, 1200);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="w-full space-y-8 my-8">
      {/* Real-time AI Progress Bar */}
      <div className="max-w-xl mx-auto p-4 rounded-2xl bg-surface/90 border border-primary-500/30 shadow-xl shadow-primary-500/10 text-center">
        <div className="flex items-center justify-center gap-2 mb-2">
          <Bot className="w-5 h-5 text-accent-cyan animate-bounce" />
          <span className="text-sm font-semibold text-white">Gemini AI가 떡상 영상을 해부하고 있습니다</span>
        </div>
        <p className="text-xs text-primary-300 font-mono transition-all duration-300">
          {steps[currentStep]}
        </p>

        {/* Progress line */}
        <div className="w-full bg-surface-border rounded-full h-1.5 mt-3 overflow-hidden">
          <div className="bg-gradient-to-r from-primary-600 via-accent-cyan to-accent-pink h-1.5 rounded-full animate-shimmer" />
        </div>
      </div>

      {/* Grid of Skeleton Video Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {[1, 2, 3, 4, 5, 6].map((i) => (
          <div
            key={i}
            className="rounded-2xl bg-surface/60 border border-surface-border p-4 space-y-4 animate-pulse relative overflow-hidden"
          >
            {/* Thumbnail skeleton */}
            <div className="w-full aspect-[9/14] bg-white/5 rounded-xl flex items-center justify-center">
              <Film className="w-10 h-10 text-white/10" />
            </div>

            {/* Badges skeleton */}
            <div className="flex items-center gap-2">
              <div className="w-16 h-5 bg-white/10 rounded-md" />
              <div className="w-20 h-5 bg-white/10 rounded-md" />
            </div>

            {/* Title skeleton */}
            <div className="space-y-2">
              <div className="w-full h-4 bg-white/10 rounded" />
              <div className="w-3/4 h-4 bg-white/10 rounded" />
            </div>

            {/* Hook text preview skeleton */}
            <div className="w-full h-12 bg-white/5 rounded-lg border border-white/5 p-2" />

            {/* Button skeleton */}
            <div className="w-full h-9 bg-primary-600/20 rounded-xl" />
          </div>
        ))}
      </div>
    </div>
  );
};
