"use client";

import React from "react";
import { SubTopic, PlatformType } from "@/types";
import { LayoutGrid, Youtube, Instagram, Film } from "lucide-react";

interface SubTopicTabsProps {
  subTopics: SubTopic[];
  selectedSubTopic: string;
  onSelectSubTopic: (id: string) => void;
  selectedPlatform: PlatformType;
  onSelectPlatform: (plat: PlatformType) => void;
  totalVideosCount: number;
}

export function SubTopicTabs({
  subTopics,
  selectedSubTopic,
  onSelectSubTopic,
  selectedPlatform,
  onSelectPlatform,
  totalVideosCount,
}: SubTopicTabsProps) {
  return (
    <div className="w-full flex flex-col gap-4 border-b border-surface-border pb-4">
      {/* Platform & Official Verification Badge */}
      <div className="flex items-center justify-between flex-wrap gap-3">
        <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-red-500/10 border border-red-500/30 text-red-300 text-xs font-bold">
          <Youtube className="w-4 h-4 text-red-500" />
          <span>YouTube Data API v3 공식 실시간 조회수 100% 반영</span>
        </div>

        <div className="text-xs text-gray-400 font-medium">
          총 <strong className="text-red-400 font-bold">{totalVideosCount}개</strong>의 떡상 유튜브 쇼츠 레퍼런스
        </div>
      </div>

      {/* SubTopic Chips */}
      <div className="flex items-center gap-2 overflow-x-auto pb-1">
        <button
          onClick={() => onSelectSubTopic("all")}
          className={`px-4 py-2 rounded-xl text-xs font-bold transition-all whitespace-nowrap ${
            selectedSubTopic === "all"
              ? "bg-gradient-to-r from-primary-600 to-primary-500 text-white shadow-lg shadow-primary-600/25"
              : "bg-surface border border-surface-border text-gray-400 hover:text-white hover:bg-white/5"
          }`}
        >
          전체 하위 주제 ({totalVideosCount})
        </button>
        {subTopics.map((sub) => {
          const isActive = selectedSubTopic === sub.id;
          return (
            <button
              key={sub.id}
              onClick={() => onSelectSubTopic(sub.id)}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all whitespace-nowrap ${
                isActive
                  ? "bg-gradient-to-r from-primary-600 to-primary-500 text-white shadow-lg shadow-primary-600/25"
                  : "bg-surface border border-surface-border text-gray-400 hover:text-white hover:bg-white/5"
              }`}
            >
              {sub.name}
            </button>
          );
        })}
      </div>
    </div>
  );
}
