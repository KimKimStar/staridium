"use client";

import React from "react";
import { SubTopic, PlatformType } from "@/types";
import { Sparkles, Layers, PlayCircle, Instagram, Video, ArrowDownUp } from "lucide-react";

interface SubTopicTabsProps {
  keyword: string;
  subTopics: SubTopic[];
  activeSubTopic: string;
  onSelectSubTopic: (id: string) => void;
  platformFilter: PlatformType;
  onSelectPlatform: (platform: PlatformType) => void;
  sortBy: "views" | "score";
  onSelectSort: (sort: "views" | "score") => void;
  insights?: {
    avgViewCount: string;
    topPlatform: string;
    hookPattern: string;
  };
}

export const SubTopicTabs: React.FC<SubTopicTabsProps> = ({
  keyword,
  subTopics,
  activeSubTopic,
  onSelectSubTopic,
  platformFilter,
  onSelectPlatform,
  sortBy,
  onSelectSort,
  insights,
}) => {
  return (
    <div className="w-full space-y-4 my-6">
      {/* AI Key Insights Bar */}
      {insights && (
        <div className="p-3.5 sm:p-4 rounded-2xl bg-gradient-to-r from-primary-950/40 via-surface to-surface border border-primary-500/20 backdrop-blur-md flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-primary-500/20 flex items-center justify-center text-primary-300">
              <Sparkles className="w-4 h-4" />
            </div>
            <div>
              <div className="text-xs text-gray-400">AI 바이럴 통계 분석</div>
              <div className="text-xs sm:text-sm font-semibold text-white">
                “{keyword}” 숏폼 평균 조회수: <span className="text-accent-cyan">{insights.avgViewCount}</span>
              </div>
            </div>
          </div>
          <div className="flex items-center gap-2 text-xs bg-surface/80 px-3 py-1.5 rounded-xl border border-surface-border">
            <span className="text-gray-400 font-medium">핵심 떡상 공식:</span>
            <span className="text-accent-pink font-semibold">{insights.hookPattern}</span>
          </div>
        </div>
      )}

      {/* SubTopic Auto-Categorization Tabs */}
      <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none">
        <button
          onClick={() => onSelectSubTopic("all")}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold whitespace-nowrap transition-all ${
            activeSubTopic === "all"
              ? "bg-gradient-to-r from-primary-600 to-primary-700 text-white shadow-lg shadow-primary-600/30 border border-primary-400/40"
              : "bg-surface hover:bg-surface/80 text-gray-400 hover:text-white border border-surface-border"
          }`}
        >
          <Layers className="w-4 h-4" />
          <span>전체 카테고리</span>
        </button>

        {subTopics.map((sub) => (
          <button
            key={sub.id}
            onClick={() => onSelectSubTopic(sub.id)}
            className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold whitespace-nowrap transition-all ${
              activeSubTopic === sub.id
                ? "bg-gradient-to-r from-primary-600 to-accent-pink text-white shadow-lg shadow-primary-600/30 border border-pink-400/40"
                : "bg-surface hover:bg-surface/80 text-gray-300 hover:text-white border border-surface-border"
            }`}
          >
            <span>{sub.name}</span>
            <span
              className={`text-[10px] px-1.5 py-0.5 rounded-md ${
                activeSubTopic === sub.id ? "bg-black/30 text-white" : "bg-white/10 text-gray-400"
              }`}
            >
              {sub.count}개
            </span>
          </button>
        ))}
      </div>

      {/* Secondary Controls: Platform Filter & Sort By */}
      <div className="flex flex-wrap items-center justify-between gap-3 pt-1">
        {/* Platform Buttons */}
        <div className="flex items-center gap-1.5 bg-surface/70 p-1 rounded-xl border border-surface-border text-xs">
          <button
            onClick={() => onSelectPlatform("all")}
            className={`px-3 py-1 rounded-lg font-medium transition-all ${
              platformFilter === "all" ? "bg-white/15 text-white" : "text-gray-400 hover:text-white"
            }`}
          >
            전체 플랫폼
          </button>
          <button
            onClick={() => onSelectPlatform("shorts")}
            className={`flex items-center gap-1 px-3 py-1 rounded-lg font-medium transition-all ${
              platformFilter === "shorts" ? "bg-red-500/20 text-red-400 border border-red-500/30" : "text-gray-400 hover:text-white"
            }`}
          >
            <PlayCircle className="w-3.5 h-3.5" />
            <span>유튜브 쇼츠</span>
          </button>
          <button
            onClick={() => onSelectPlatform("reels")}
            className={`flex items-center gap-1 px-3 py-1 rounded-lg font-medium transition-all ${
              platformFilter === "reels" ? "bg-pink-500/20 text-pink-400 border border-pink-500/30" : "text-gray-400 hover:text-white"
            }`}
          >
            <Instagram className="w-3.5 h-3.5" />
            <span>인스타 릴스</span>
          </button>
          <button
            onClick={() => onSelectPlatform("tiktok")}
            className={`flex items-center gap-1 px-3 py-1 rounded-lg font-medium transition-all ${
              platformFilter === "tiktok" ? "bg-cyan-500/20 text-cyan-400 border border-cyan-500/30" : "text-gray-400 hover:text-white"
            }`}
          >
            <Video className="w-3.5 h-3.5" />
            <span>틱톡</span>
          </button>
        </div>

        {/* Sort Controls */}
        <div className="flex items-center gap-2 text-xs">
          <span className="text-gray-500 flex items-center gap-1">
            <ArrowDownUp className="w-3 h-3" /> 정렬:
          </span>
          <select
            value={sortBy}
            onChange={(e) => onSelectSort(e.target.value as "views" | "score")}
            className="bg-surface border border-surface-border text-gray-300 rounded-lg px-2.5 py-1 focus:outline-none focus:border-primary-500"
          >
            <option value="views">조회수 높은 순 (기본)</option>
            <option value="score">AI 바이럴 스코어 순</option>
          </select>
        </div>
      </div>
    </div>
  );
};
