"use client";

import React, { useState } from "react";
import { ViralVideo } from "@/types";
import { Eye, Heart, Play, Sparkles, Youtube, Instagram, Film } from "lucide-react";

interface VideoCardProps {
  video: ViralVideo;
  rank: number;
  onOpenAnalysis: (video: ViralVideo) => void;
}

export function VideoCard({ video, rank, onOpenAnalysis }: VideoCardProps) {
  const [imgError, setImgError] = useState(false);

  const getPlatformIcon = (plat: string) => {
    if (plat === "shorts") return <Youtube className="w-3.5 h-3.5 text-red-400" />;
    if (plat === "reels") return <Instagram className="w-3.5 h-3.5 text-pink-400" />;
    return <Film className="w-3.5 h-3.5 text-cyan-400" />;
  };

  const getPlatformLabel = (plat: string) => {
    if (plat === "shorts") return "Shorts";
    if (plat === "reels") return "Reels";
    return "TikTok";
  };

  // Safe fallback thumbnail if image fails
  const fallbackThumb = `https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=800&auto=format&fit=crop&q=80`;
  const displayThumb = imgError ? fallbackThumb : (video.thumbnail || fallbackThumb);

  return (
    <div
      onClick={() => onOpenAnalysis(video)}
      className="group relative flex flex-col rounded-2xl bg-surface-card border border-surface-border overflow-hidden hover:border-primary-500/50 hover:shadow-2xl hover:shadow-primary-600/20 transition-all duration-300 cursor-pointer transform hover:-translate-y-1"
    >
      {/* Rank Badge */}
      <div className="absolute top-3 left-3 z-20 flex items-center justify-center w-7 h-7 rounded-xl bg-black/70 backdrop-blur-md border border-white/20 text-xs font-black text-amber-400">
        #{rank}
      </div>

      {/* Platform & Viral Score Badge */}
      <div className="absolute top-3 right-3 z-20 flex items-center gap-1.5 px-2.5 py-1 rounded-xl bg-black/70 backdrop-blur-md border border-white/10 text-[11px] font-bold text-white">
        <Youtube className="w-3.5 h-3.5 text-red-500 fill-red-500" />
        <span>YouTube Shorts</span>
        <span className="text-emerald-400 ml-1">🔥 {video.viralScore}점</span>
      </div>

      {/* 9:14 Aspect Ratio Real Thumbnail */}
      <div className="relative w-full aspect-[9/13] bg-surface overflow-hidden">
        <img
          src={displayThumb}
          alt={video.title}
          referrerPolicy="no-referrer"
          onError={() => setImgError(true)}
          className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
        />

        {/* Play Overlay */}
        <div className="absolute inset-0 bg-gradient-to-t from-background/90 via-background/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
          <div className="w-12 h-12 rounded-full bg-primary-600/90 text-white flex items-center justify-center shadow-lg shadow-primary-600/50 transform group-hover:scale-110 transition-transform">
            <Play className="w-6 h-6 fill-white ml-0.5" />
          </div>
        </div>

        {/* Duration */}
        <div className="absolute bottom-2.5 right-2.5 px-2 py-0.5 rounded-md bg-black/80 text-[10px] font-bold text-gray-300">
          {video.duration || "45s"}
        </div>
      </div>

      {/* Card Info */}
      <div className="flex flex-col flex-1 p-4 gap-2.5">
        {/* Author & Stats */}
        <div className="flex items-center justify-between text-xs text-gray-400 font-medium">
          <span className="truncate max-w-[130px] font-semibold text-gray-300">
            {video.author}
          </span>
          <div className="flex items-center gap-3">
            <span className="flex items-center gap-1 text-emerald-400 font-bold">
              <Eye className="w-3.5 h-3.5" />
              {video.viewsFormatted}
            </span>
            <span className="flex items-center gap-1 text-gray-400">
              <Heart className="w-3.5 h-3.5 text-pink-400" />
              {video.likesFormatted}
            </span>
          </div>
        </div>

        {/* Title */}
        <h3 className="font-bold text-sm text-white line-clamp-2 leading-snug group-hover:text-primary-300 transition-colors">
          {video.title}
        </h3>

        {/* Hook Preview */}
        <div className="mt-auto pt-2 border-t border-white/5">
          <div className="text-[11px] font-bold text-primary-400 mb-0.5 flex items-center gap-1">
            <Sparkles className="w-3 h-3" />
            <span>초반 3초 훅 대사:</span>
          </div>
          <p className="text-xs text-gray-300 line-clamp-2 italic bg-white/5 p-2 rounded-lg">
            {video.hookSummary || "“아직도 그렇게 하세요? 당장 멈추세요! 99%가 인생 낭비하고 있습니다.”"}
          </p>
        </div>

        {/* CTA Button */}
        <button className="w-full mt-2 py-2 rounded-xl bg-white/5 hover:bg-primary-600/20 border border-white/10 hover:border-primary-500/30 text-xs font-bold text-primary-300 flex items-center justify-center gap-1.5 transition-all">
          <Sparkles className="w-3.5 h-3.5" />
          <span>AI 성공 요인 & 대본 해부</span>
        </button>
      </div>
    </div>
  );
}
