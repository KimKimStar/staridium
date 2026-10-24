"use client";

import React from "react";
import { ViralVideo } from "@/types";
import { VideoCard } from "./VideoCard";

interface VideoListProps {
  videos: ViralVideo[];
  onOpenAnalysis: (video: ViralVideo) => void;
}

export function VideoList({ videos, onOpenAnalysis }: VideoListProps) {
  if (!videos || videos.length === 0) {
    return (
      <div className="w-full py-20 flex flex-col items-center justify-center text-center">
        <div className="w-16 h-16 rounded-2xl bg-surface border border-surface-border flex items-center justify-center text-3xl mb-4">
          🔍
        </div>
        <h3 className="text-lg font-bold text-white mb-1">검색된 떡상 영상이 없습니다</h3>
        <p className="text-sm text-gray-400">다른 키워드나 하위 주제를 선택해 보세요.</p>
      </div>
    );
  }

  return (
    <div className="w-full grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      {videos.map((video, idx) => (
        <VideoCard
          key={video.id || `v-${idx}`}
          video={video}
          rank={idx + 1}
          onOpenAnalysis={onOpenAnalysis}
        />
      ))}
    </div>
  );
}
