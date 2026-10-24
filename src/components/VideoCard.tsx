"use client";

import React from "react";
import { ViralVideo } from "@/types";
import { Eye, Heart, Flame, Sparkles, Play, ArrowUpRight } from "lucide-react";

interface VideoCardProps {
  video: ViralVideo;
  onSelect: (video: ViralVideo) => void;
}

export const VideoCard: React.FC<VideoCardProps> = ({ video, onSelect }) => {
  const getPlatformBadge = (platform: "shorts" | "reels" | "tiktok") => {
    switch (platform) {
      case "shorts":
        return {
          label: "YouTube Shorts",
          color: "bg-red-500/10 text-red-400 border-red-500/30",
          dotColor: "bg-red-500",
        };
      case "reels":
        return {
          label: "Instagram Reels",
          color: "bg-pink-500/10 text-pink-400 border-pink-500/30",
          dotColor: "bg-pink-500",
        };
      case "tiktok":
        return {
          label: "TikTok Viral",
          color: "bg-cyan-500/10 text-cyan-400 border-cyan-500/30",
          dotColor: "bg-cyan-400",
        };
    }
  };

  const badge = getPlatformBadge(video.platform);

  return (
    <div
      onClick={() => onSelect(video)}
      className="group relative flex flex-col rounded-2xl bg-surface/80 hover:bg-surface border border-surface-border hover:border-primary-500/50 p-4 transition-all duration-300 hover:shadow-2xl hover:shadow-primary-500/20 cursor-pointer overflow-hidden transform hover:-translate-y-1"
    >
      {/* Glow Hover Effect */}
      <div className="absolute inset-0 bg-gradient-to-t from-primary-600/10 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none" />

      {/* Thumbnail Container (Short-form 9:14 aspect ratio) */}
      <div className="relative w-full aspect-[9/13] rounded-xl overflow-hidden bg-slate-900 mb-3.5">
        <img
          src={video.thumbnail}
          alt={video.title}
          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
          loading="lazy"
        />

        {/* Top Badges Overlay */}
        <div className="absolute top-2.5 left-2.5 right-2.5 flex items-center justify-between">
          <span
            className={`flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[11px] font-semibold border backdrop-blur-md ${badge.color}`}
          >
            <span className={`w-1.5 h-1.5 rounded-full ${badge.dotColor}`} />
            {badge.label}
          </span>
          <span className="px-2 py-0.5 rounded-md bg-black/60 backdrop-blur-md text-white text-[11px] font-mono">
            {video.duration}
          </span>
        </div>

        {/* Play Overlay Icon on hover */}
        <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-black/40 backdrop-blur-[2px]">
          <div className="w-12 h-12 rounded-full bg-primary-600/90 text-white flex items-center justify-center shadow-lg transform group-hover:scale-110 transition-transform">
            <Play className="w-5 h-5 fill-current ml-0.5" />
          </div>
        </div>

        {/* Viral Score Badge */}
        <div className="absolute bottom-2.5 left-2.5 flex items-center gap-1 px-2.5 py-1 rounded-lg bg-black/75 backdrop-blur-md border border-white/10 text-xs font-bold text-accent-amber">
          <Flame className="w-3.5 h-3.5 text-accent-amber" />
          <span>바이럴 지수 {video.viralScore}점</span>
        </div>
      </div>

      {/* Author and View Stats */}
      <div className="flex items-center justify-between text-xs text-gray-400 mb-2">
        <span className="font-medium text-gray-300 truncate max-w-[140px]">
          {video.author}
        </span>
        <div className="flex items-center gap-3">
          <span className="flex items-center gap-1 text-accent-cyan font-semibold">
            <Eye className="w-3.5 h-3.5" />
            {video.viewsFormatted}
          </span>
          <span className="flex items-center gap-1">
            <Heart className="w-3.5 h-3.5 text-accent-pink" />
            {video.likesFormatted}
          </span>
        </div>
      </div>

      {/* Video Title */}
      <h3 className="font-bold text-sm text-white line-clamp-2 mb-3 leading-snug group-hover:text-primary-300 transition-colors">
        {video.title}
      </h3>

      {/* 3-Second Hook Preview Quote */}
      <div className="p-2.5 rounded-xl bg-surface-card border border-surface-border text-xs mb-3 space-y-1">
        <div className="flex items-center gap-1 text-[11px] font-semibold text-accent-amber">
          <Sparkles className="w-3 h-3" />
          <span>초반 3초 훅 대사:</span>
        </div>
        <p className="text-gray-300 italic line-clamp-2 leading-relaxed">
          {video.hookSummary}
        </p>
      </div>

      {/* Viral Reason Tag */}
      <div className="mt-auto pt-2 border-t border-surface-border/60 flex items-center justify-between text-[11px]">
        <span className="text-gray-400 truncate max-w-[200px]">
          💡 {video.viralReason}
        </span>
        <span className="text-primary-400 font-semibold flex items-center gap-0.5 group-hover:translate-x-0.5 transition-transform">
          해부하기 <ArrowUpRight className="w-3 h-3" />
        </span>
      </div>
    </div>
  );
};
