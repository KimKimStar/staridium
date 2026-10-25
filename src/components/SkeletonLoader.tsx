"use client";

import React from "react";

export function SkeletonLoader() {
  return (
    <div className="w-full flex flex-col gap-6">
      {/* Top Banner Skeleton */}
      <div className="w-full p-4 rounded-2xl bg-slate-800/60 border border-slate-700/60 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-slate-700/70 animate-pulse" />
          <div className="flex flex-col gap-2">
            <div className="w-52 h-4 rounded-md bg-slate-700/70 animate-pulse" />
            <div className="w-36 h-3 rounded-md bg-slate-700/50 animate-pulse" />
          </div>
        </div>
        <div className="w-28 h-7 rounded-lg bg-slate-700/60 animate-pulse" />
      </div>

      {/* Grid of 8 9:13 Shorts Skeleton Cards */}
      <div className="w-full grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {Array.from({ length: 8 }).map((_, i) => (
          <div
            key={i}
            className="flex flex-col rounded-2xl bg-slate-800/80 border border-slate-700/60 overflow-hidden shadow-lg"
          >
            {/* Shimmering Thumbnail (9:13 Aspect Ratio) */}
            <div className="w-full aspect-[9/13] bg-slate-900/90 relative overflow-hidden">
              <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-700/20 to-transparent -translate-x-full animate-[shimmer_1.8s_infinite]" />
              {/* Fake rank badge */}
              <div className="absolute top-3 left-3 w-7 h-7 rounded-lg bg-slate-700/80 animate-pulse" />
              {/* Fake platform badge */}
              <div className="absolute top-3 right-3 w-20 h-6 rounded-lg bg-slate-700/80 animate-pulse" />
              {/* Fake duration */}
              <div className="absolute bottom-2.5 right-2.5 w-10 h-4 rounded bg-slate-800/90 animate-pulse" />
            </div>

            {/* Meta & Content Skeletons */}
            <div className="p-4 flex flex-col gap-3 bg-slate-800/90">
              <div className="flex justify-between items-center">
                <div className="w-24 h-3.5 rounded bg-slate-700/70 animate-pulse" />
                <div className="w-20 h-3.5 rounded bg-slate-700/70 animate-pulse" />
              </div>
              <div className="w-full h-4 rounded bg-slate-700/80 animate-pulse" />
              <div className="w-3/4 h-4 rounded bg-slate-700/70 animate-pulse" />
              
              {/* Hook preview skeleton box */}
              <div className="w-full p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/50 mt-1 flex flex-col gap-1.5">
                <div className="w-28 h-3 rounded bg-blue-500/30 animate-pulse" />
                <div className="w-full h-3 rounded bg-slate-700/60 animate-pulse" />
              </div>

              {/* Action Button Skeleton */}
              <div className="w-full h-8 rounded-xl bg-slate-700/70 animate-pulse mt-1" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
