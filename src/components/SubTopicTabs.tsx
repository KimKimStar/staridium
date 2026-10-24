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
      {/* Platform Filter Tabs */}
      <div className="flex items-center justify-between flex-wrap gap-3">
        <div className="flex items-center gap-1.5 p-1 bg-surface border border-surface-border rounded-xl">
          <button
            onClick={() => onSelectPlatform("all")}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
              selectedPlatform === "all"
                ? "bg-primary-600 text-white shadow-md shadow-primary-600/30"
                : "text-gray-400 hover:text-white"
            }`}
          >
            <LayoutGrid className="w-3.5 h-3.5" />
            <span>전체 플랫폼</span>
          </button>
          <button
            onClick={() => onSelectPlatform("shorts")}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
              selectedPlatform === "shorts"
                ? "bg-red-600 text-white shadow-md shadow-red-600/30"
                : "text-gray-400 hover:text-white"
            }`}
          >
            <Youtube className="w-3.5 h-3.5" />
            <span>유튜브 쇼츠</span>
          </button>
          <button
            onClick={() => onSelectPlatform("reels")}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
              selectedPlatform === "reels"
                ? "bg-gradient-to-r from-purple-600 to-pink-600 text-white shadow-md shadow-pink-600/30"
                : "text-gray-400 hover:text-white"
            }`}
          >
            <Instagram className="w-3.5 h-3.5" />
            <span>인스타 릴스</span>
          </button>
          <button
            onClick={() => onSelectPlatform("tiktok")}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
              selectedPlatform === "tiktok"
                ? "bg-cyan-600 text-white shadow-md shadow-cyan-600/30"
                : "text-gray-400 hover:text-white"
            }`}
          >
            <Film className="w-3.5 h-3.5" />
            <span>틱톡 코리아</span>
          </button>
        </div>

        <div className="text-xs text-gray-400 font-medium">
          총 <strong className="text-primary-400 font-bold">{totalVideosCount}개</strong>의 떡상 숏폼 레퍼런스
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
