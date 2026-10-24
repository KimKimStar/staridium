"use client";

import React, { useState } from "react";
import { Search, Flame } from "lucide-react";

interface SearchBarProps {
  onSearch: (keyword: string) => void;
  isLoading?: boolean;
}

const POPULAR_KEYWORDS = [
  "인간관계", "다이어트", "재테크", "K-뷰티", "초간단요리", 
  "자기계발", "스마트폰꿀팁", "데일리룩", "국내여행", "생활영어"
];

export function SearchBar({ onSearch, isLoading }: SearchBarProps) {
  const [inputVal, setInputVal] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (inputVal.trim()) {
      onSearch(inputVal.trim());
    }
  };

  return (
    <div className="w-full max-w-3xl mx-auto flex flex-col items-center gap-3">
      <form onSubmit={handleSubmit} className="w-full relative">
        <div className="relative flex items-center">
          <input
            type="text"
            value={inputVal}
            onChange={(e) => setInputVal(e.target.value)}
            placeholder="어떤 숏폼 주제의 떡상 공식을 파헤칠까요? (예: 인간관계, 다이어트, 주식)"
            className="w-full pl-12 pr-28 py-4 rounded-2xl bg-surface-card border border-surface-border text-white placeholder-gray-500 text-sm md:text-base focus:outline-none focus:border-primary-500 focus:ring-2 focus:ring-primary-500/20 shadow-2xl transition-all"
          />
          <Search className="w-5 h-5 text-gray-400 absolute left-4" />
          <button
            type="submit"
            disabled={isLoading}
            className="absolute right-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-primary-600 to-primary-500 hover:from-primary-500 hover:to-primary-600 text-white font-bold text-xs md:text-sm shadow-lg shadow-primary-600/30 transition-all disabled:opacity-50"
          >
            {isLoading ? "분석 중..." : "AI 분석"}
          </button>
        </div>
      </form>

      {/* Popular Keyword Chips */}
      <div className="flex items-center gap-2 overflow-x-auto w-full justify-start md:justify-center py-1">
        <div className="flex items-center gap-1 text-[11px] font-bold text-amber-400 flex-shrink-0">
          <Flame className="w-3.5 h-3.5 fill-amber-400" />
          <span>실시간 인기:</span>
        </div>
        {POPULAR_KEYWORDS.map((kw) => (
          <button
            key={kw}
            type="button"
            onClick={() => {
              setInputVal(kw);
              onSearch(kw);
            }}
            className="px-2.5 py-1 rounded-full text-xs bg-white/5 border border-white/10 text-gray-300 hover:text-white hover:border-primary-500/50 hover:bg-primary-500/10 transition-all flex-shrink-0"
          >
            {kw}
          </button>
        ))}
      </div>
    </div>
  );
}
