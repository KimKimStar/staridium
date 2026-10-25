"use client";

import React from "react";
import { ViralVideo } from "@/types";
import { VideoCard } from "./VideoCard";
import { AdBanner } from "./AdBanner";

interface VideoListProps {
  videos: ViralVideo[];
  onOpenAnalysis?: (video: ViralVideo) => void;
  onSelectVideo?: (video: ViralVideo) => void;
}

export function VideoList({ videos, onOpenAnalysis, onSelectVideo }: VideoListProps) {
  const handleOpen = onOpenAnalysis || onSelectVideo || (() => {});

  if (!videos || videos.length === 0) {
    return (
      <div className="w-full py-20 flex flex-col items-center justify-center text-center">
        <div className="w-16 h-16 rounded-2xl bg-slate-800/80 border border-slate-700/60 flex items-center justify-center text-3xl mb-4 shadow-lg">
          🔍
        </div>
        <h3 className="text-lg font-bold text-white mb-1">검색된 떡상 영상이 없습니다</h3>
        <p className="text-sm text-slate-400">다른 키워드나 하위 주제를 선택해 보세요.</p>
      </div>
    );
  }

  return (
    <div className="w-full grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      {videos.map((video, idx) => {
        const elements = [
          <VideoCard
            key={video.id || `v-${idx}`}
            video={video}
            rank={idx + 1}
            onOpenAnalysis={handleOpen}
          />,
        ];

        // Insert native In-Feed Ad card naturally every 6 items (AdSense monetization)
        if ((idx + 1) % 6 === 0 && idx < videos.length - 1) {
          elements.push(
            <AdBanner
              key={`ad-${idx}`}
              type="in-feed"
              className="h-full"
            />
          );
        }

        return elements;
      })}
    </div>
  );
}
