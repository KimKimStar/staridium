"use client";

import React from "react";
import { ViralVideo } from "@/types";
import { VideoCard } from "./VideoCard";
import { AlertCircle } from "lucide-react";

interface VideoListProps {
  videos: ViralVideo[];
  onSelectVideo: (video: ViralVideo) => void;
}

export const VideoList: React.FC<VideoListProps> = ({ videos, onSelectVideo }) => {
  if (videos.length === 0) {
    return (
      <div className="w-full py-16 text-center rounded-2xl bg-surface/40 border border-surface-border">
        <AlertCircle className="w-10 h-10 text-gray-500 mx-auto mb-3" />
        <h4 className="text-base font-semibold text-white mb-1">
          해당 조건의 떡상 영상이 없습니다
        </h4>
        <p className="text-xs text-gray-400">
          다른 하위 주제 탭이나 플랫폼 필터를 선택해보세요.
        </p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      {videos.map((video) => (
        <VideoCard key={video.id} video={video} onSelect={onSelectVideo} />
      ))}
    </div>
  );
};
