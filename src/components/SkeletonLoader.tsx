"use client";

import React from "react";

export function SkeletonLoader() {
  return (
    <div className="w-full flex flex-col gap-6">
      {/* Skeleton Pulse Banner */}
      <div className="w-full p-4 rounded-2xl bg-surface/50 border border-primary-500/20 flex items-center justify-between animate-pulse">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-primary-600/30" />
          <div className="flex flex-col gap-1.5">
            <div className="w-48 h-4 rounded bg-white/10" />
            <div className="w-32 h-3 rounded bg-white/5" />
          </div>
        </div>
        <div className="w-24 h-6 rounded-full bg-primary-500/20" />
      </div>

      {/* Grid of Skeleton Cards */}
      <div className="w-full grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {Array.from({ length: 8 }).map((_, i) => (
          <div
            key={i}
            className="flex flex-col rounded-2xl bg-surface border border-surface-border overflow-hidden animate-pulse"
          >
            {/* Thumbnail aspect ratio */}
            <div className="w-full aspect-[9/13] bg-white/5 relative">
              <div className="absolute top-3 left-3 w-7 h-7 rounded-lg bg-white/10" />
              <div className="absolute top-3 right-3 w-16 h-6 rounded-lg bg-white/10" />
            </div>

            {/* Meta */}
            <div className="p-4 flex flex-col gap-3">
              <div className="flex justify-between items-center">
                <div className="w-20 h-3 rounded bg-white/10" />
                <div className="w-16 h-3 rounded bg-white/10" />
              </div>
              <div className="w-full h-4 rounded bg-white/10" />
              <div className="w-3/4 h-4 rounded bg-white/10" />
              <div className="w-full h-12 rounded-lg bg-white/5 mt-2" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
