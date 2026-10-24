"use client";

import React, { useState } from "react";
import { Search, Sparkles, TrendingUp, ArrowRight } from "lucide-react";

interface SearchBarProps {
  onSearch: (keyword: string) => void;
  isLoading: boolean;
}

const TRENDING_KEYWORDS = [
  "다이어트",
  "주식/재테크",
  "뷰티/메이크업",
  "맛집/레시피",
  "자기계발/동기부여",
  "인간관계/심리",
];

export const SearchBar: React.FC<SearchBarProps> = ({ onSearch, isLoading }) => {
  const [inputVal, setInputVal] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (inputVal.trim() && !isLoading) {
      onSearch(inputVal.trim());
    }
  };

  const handleChipClick = (kw: string) => {
    setInputVal(kw);
    onSearch(kw);
  };

  return (
    <div className="w-full max-w-3xl mx-auto text-center pt-8 pb-4">
      {/* Eye-catching Badge */}
      <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-primary-500/10 border border-primary-500/20 text-primary-300 text-xs font-medium mb-6">
        <Sparkles className="w-3.5 h-3.5 text-accent-cyan animate-spin" style={{ animationDuration: "3s" }} />
        <span>Gemini AI 기반 숏폼 바이럴 해부 & 프리프로덕션 엔진</span>
      </div>

      {/* Main Headline */}
      <h1 className="text-3xl sm:text-5xl font-extrabold text-white tracking-tight leading-[1.2] mb-4">
        3초 만에 스크롤을 멈추는 <br className="hidden sm:block" />
        <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary-500 via-accent-cyan to-accent-pink">
          떡상 숏폼의 성공 공식
        </span>
        을 해부합니다
      </h1>

      <p className="text-sm sm:text-base text-gray-400 max-w-xl mx-auto mb-8 leading-relaxed">
        주제만 입력하세요. 유튜브 쇼츠, 인스타 릴스, 틱톡의 떡상 영상을 전수 분석하여{" "}
        <strong className="text-gray-200">초반 3초 훅 대사, 컷 편집 속도, 타임라인 대본, 내 채널 복제 기획서</strong>까지 낱낱이 제공합니다.
      </p>

      {/* Modern Neon Search Bar Form */}
      <form onSubmit={handleSubmit} className="relative max-w-2xl mx-auto">
        <div className="relative flex items-center rounded-2xl bg-surface/90 border border-surface-border p-2 shadow-2xl shadow-primary-500/10 focus-within:border-primary-500/80 focus-within:ring-2 focus-within:ring-primary-500/20 transition-all">
          <div className="pl-3 text-gray-400">
            <Search className="w-5 h-5 text-primary-400" />
          </div>
          <input
            type="text"
            value={inputVal}
            onChange={(e) => setInputVal(e.target.value)}
            placeholder="분석하고 싶은 숏폼 주제를 입력하세요 (예: 다이어트, 부동산, 영어회화)"
            disabled={isLoading}
            className="w-full bg-transparent px-3 py-2.5 text-sm sm:text-base text-white placeholder-gray-500 focus:outline-none"
          />
          <button
            type="submit"
            disabled={isLoading || !inputVal.trim()}
            className="flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold text-white bg-gradient-to-r from-primary-600 to-accent-pink hover:from-primary-500 hover:to-pink-500 disabled:opacity-40 disabled:cursor-not-allowed transition-all shadow-md shadow-primary-600/30 flex-shrink-0"
          >
            <span>{isLoading ? "분석 중..." : "해부 시작"}</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </form>

      {/* Trending Suggestion Chips */}
      <div className="mt-4 flex flex-wrap items-center justify-center gap-2 text-xs">
        <span className="text-gray-500 flex items-center gap-1 font-medium">
          <TrendingUp className="w-3.5 h-3.5 text-accent-cyan" /> 실시간 추천:
        </span>
        {TRENDING_KEYWORDS.map((kw) => (
          <button
            key={kw}
            onClick={() => handleChipClick(kw)}
            disabled={isLoading}
            className="px-2.5 py-1 rounded-lg bg-surface/60 hover:bg-surface border border-surface-border text-gray-400 hover:text-white transition-all"
          >
            #{kw}
          </button>
        ))}
      </div>
    </div>
  );
};
