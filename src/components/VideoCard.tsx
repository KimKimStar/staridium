"use client";

import React, { useState } from "react";
import { ViralVideo } from "@/types";
import { Eye, Heart, Play, Sparkles, Youtube, ArrowUpRight } from "lucide-react";

interface VideoCardProps {
  video: ViralVideo;
  rank: number;
  onOpenAnalysis: (video: ViralVideo) => void;
}

export function VideoCard({ video, rank, onOpenAnalysis }: VideoCardProps) {
  const [imgError, setImgError] = useState(false);

  // Safe fallback thumbnail if image fails
  const fallbackThumb = `https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=800&auto=format&fit=crop&q=80`;
  const displayThumb = imgError ? fallbackThumb : (video.thumbnail || fallbackThumb);

  return (
    <div
      onClick={() => onOpenAnalysis(video)}
      className="group relative flex flex-col rounded-2xl bg-slate-800/90 border border-slate-700/70 overflow-hidden hover:border-blue-500/60 hover:shadow-xl hover:shadow-blue-500/10 transition-all duration-300 cursor-pointer transform hover:-translate-y-1.5 backdrop-blur-sm"
    >
      {/* Top Badges */}
      <div className="absolute top-3 left-3 z-20 flex items-center justify-center min-w-[28px] h-7 px-2 rounded-lg bg-slate-950/80 backdrop-blur-md border border-slate-700/80 text-xs font-black text-amber-400 shadow-md">
        #{rank}
      </div>

      <div className="absolute top-3 right-3 z-20 flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-slate-950/80 backdrop-blur-md border border-slate-700/80 text-[11px] font-bold text-white shadow-md">
        <Youtube className="w-3.5 h-3.5 text-red-500 fill-red-500" />
        <span className="text-gray-200">Shorts</span>
        <span className="text-emerald-400 font-extrabold ml-1">🔥 {video.viralScore}점</span>
      </div>

      {/* 9:13 Vertical Aspect Ratio Thumbnail with hover zoom */}
      <div className="relative w-full aspect-[9/13] bg-slate-900 overflow-hidden">
        <img
          src={displayThumb}
          alt={video.title}
          referrerPolicy="no-referrer"
          onError={() => setImgError(true)}
          className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
        />

        {/* Play Overlay with Glassmorphic Button */}
        <div className="absolute inset-0 bg-gradient-to-t from-slate-950/95 via-slate-950/25 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
          <div className="w-13 h-13 px-4 py-2.5 rounded-full bg-blue-600/90 hover:bg-blue-500 text-white flex items-center gap-2 shadow-lg shadow-blue-500/40 transform group-hover:scale-105 transition-all text-xs font-bold border border-blue-400/30">
            <Play className="w-4 h-4 fill-white" />
            <span>분석 보기</span>
          </div>
        </div>

        {/* Duration Badge */}
        <div className="absolute bottom-2.5 right-2.5 px-2 py-0.5 rounded-md bg-slate-950/85 backdrop-blur-sm border border-slate-700/60 text-[10px] font-mono font-bold text-slate-300">
          {video.duration || "45s"}
        </div>
      </div>

      {/* Card Info (Shadcn UI inspired layout) */}
      <div className="flex flex-col flex-1 p-4 gap-2.5 bg-slate-800/80">
        {/* Author & Stats */}
        <div className="flex items-center justify-between text-xs text-slate-400 font-medium">
          <span className="truncate max-w-[130px] font-semibold text-slate-200">
            {video.author}
          </span>
          <div className="flex items-center gap-3 font-semibold">
            <span className="flex items-center gap-1 text-emerald-400">
              <Eye className="w-3.5 h-3.5" />
              {video.viewsFormatted}
            </span>
            <span className="flex items-center gap-1 text-pink-400">
              <Heart className="w-3.5 h-3.5 fill-pink-500/20" />
              {video.likesFormatted}
            </span>
          </div>
        </div>

        {/* Video Title */}
        <h3 className="font-bold text-sm text-white line-clamp-2 leading-snug group-hover:text-blue-300 transition-colors">
          {video.title}
        </h3>

        {/* Hook Preview Box */}
        <div className="mt-auto pt-2.5 border-t border-slate-700/60">
          <div className="text-[11px] font-extrabold text-blue-400 mb-1 flex items-center gap-1">
            <Sparkles className="w-3 h-3 text-blue-400" />
            <span>초반 3초 훅 대사</span>
          </div>
          <p className="text-xs text-slate-300 line-clamp-2 italic bg-slate-900/60 p-2 rounded-lg border border-slate-700/50">
            "{video.hookSummary || "시작하자마자 시청자의 시선을 강탈하는 후킹 대사..."}"
          </p>
        </div>

        {/* Primary Action Button (Neon Blue) */}
        <button
          onClick={(e) => {
            e.stopPropagation();
            onOpenAnalysis(video);
          }}
          className="w-full mt-2 py-2 px-3 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-extrabold text-xs flex items-center justify-center gap-1.5 shadow-md shadow-blue-500/20 active:scale-[0.98] transition-all border border-blue-400/20"
        >
          <span>3초 후킹 대사 보기</span>
          <ArrowUpRight className="w-3.5 h-3.5" />
        </button>
      </div>
    </div>
  );
}
