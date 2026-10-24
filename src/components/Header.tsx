"use client";

import React from "react";
import { Sparkles, Zap, Flame, Crown } from "lucide-react";

interface HeaderProps {
  credits: number;
  isPro: boolean;
  onOpenPricing: () => void;
}

export const Header: React.FC<HeaderProps> = ({ credits, isPro, onOpenPricing }) => {
  return (
    <header className="sticky top-0 z-40 w-full backdrop-blur-xl bg-background/80 border-b border-surface-border">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Brand Logo */}
        <div className="flex items-center gap-3 cursor-pointer">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-primary-600 via-primary-500 to-accent-pink flex items-center justify-center shadow-lg shadow-primary-500/25">
            <Flame className="w-5 h-5 text-white animate-pulse" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-extrabold text-lg sm:text-xl tracking-tight text-white">
                Viral<span className="text-transparent bg-clip-text bg-gradient-to-r from-primary-500 to-accent-cyan">Scope</span>
              </span>
              <span className="text-[10px] font-semibold tracking-wider uppercase px-2 py-0.5 rounded-full bg-primary-500/20 text-primary-300 border border-primary-500/30">
                Pre-production AI
              </span>
            </div>
            <p className="text-[11px] text-gray-400 hidden sm:block">
              숏폼 떡상 알고리즘 해부 & 기획 스튜디오
            </p>
          </div>
        </div>

        {/* Right Nav Actions */}
        <div className="flex items-center gap-3">
          {/* Credit Status Badge */}
          <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-surface border border-surface-border text-xs">
            <Zap className={`w-3.5 h-3.5 ${isPro ? "text-accent-cyan" : credits > 0 ? "text-accent-amber" : "text-red-400"}`} />
            <span className="text-gray-400">잔여 크레딧:</span>
            {isPro ? (
              <span className="font-bold text-accent-cyan flex items-center gap-1">
                <Crown className="w-3 h-3" /> PRO 무제한
              </span>
            ) : (
              <span className={`font-bold ${credits > 0 ? "text-white" : "text-red-400"}`}>
                {credits} / 3회
              </span>
            )}
          </div>

          {/* Upgrade Button */}
          {!isPro && (
            <button
              onClick={onOpenPricing}
              className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-semibold text-white bg-gradient-to-r from-primary-600 to-accent-pink hover:from-primary-500 hover:to-pink-500 shadow-md shadow-primary-500/20 transition-all duration-200 transform hover:scale-[1.02] active:scale-[0.98]"
            >
              <Crown className="w-3.5 h-3.5" />
              <span>Pro 업그레이드</span>
              <span className="text-[10px] opacity-80">(월 5,000원)</span>
            </button>
          )}

          {isPro && (
            <div className="px-3 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-medium flex items-center gap-1.5">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Pro 멤버십 활성</span>
            </div>
          )}
        </div>
      </div>
    </header>
  );
};
