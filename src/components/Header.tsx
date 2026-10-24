"use client";

import React from "react";
import Link from "next/link";
import { Sparkles, Crown, Zap, Film } from "lucide-react";

interface HeaderProps {
  credits: number;
  isPro: boolean;
  onOpenPricing: () => void;
}

export function Header({ credits, isPro, onOpenPricing }: HeaderProps) {
  return (
    <header className="sticky top-0 z-40 border-b border-surface-border bg-background/80 backdrop-blur-md px-6 py-4">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        {/* Brand */}
        <div className="flex items-center gap-3">
          <Link href="/" className="flex items-center gap-3 group">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-primary-600 to-accent-cyan flex items-center justify-center shadow-lg shadow-primary-600/30 group-hover:scale-105 transition-transform">
              <Sparkles className="w-5 h-5 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-extrabold text-xl tracking-tight bg-gradient-to-r from-white via-primary-100 to-accent-cyan bg-clip-text text-transparent">
                  ViralScope AI
                </span>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-primary-500/20 text-primary-400 border border-primary-500/30">
                  MVP v2.0
                </span>
              </div>
              <p className="text-xs text-gray-400">숏폼 바이럴 해부학 & AI 모션 스왑 SaaS</p>
            </div>
          </Link>
        </div>

        {/* Center / Navigation: Motion Swap Killer Feature */}
        <div className="hidden md:flex items-center gap-2">
          <Link
            href="/motion-swap"
            className="flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-black text-amber-200 bg-gradient-to-r from-purple-900/60 via-pink-900/60 to-amber-900/40 border border-amber-500/40 shadow-lg shadow-purple-600/20 hover:border-amber-400 hover:scale-[1.02] transition-all"
          >
            <Film className="w-4 h-4 text-pink-400 animate-pulse" />
            <span>AI 모션 스왑 스튜디오</span>
            <span className="px-1.5 py-0.5 text-[9px] font-black bg-pink-500 text-white rounded-full">
              HOT
            </span>
          </Link>
        </div>

        {/* Right Actions: Credit & Pro Button */}
        <div className="flex items-center gap-3 sm:gap-4">
          <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-surface border border-surface-border">
            <Zap className="w-4 h-4 text-amber-400 fill-amber-400" />
            <span className="text-xs text-gray-400 font-medium hidden sm:inline">잔여 크레딧:</span>
            <span className="text-sm font-bold text-amber-300">
              {isPro ? "무제한 PRO" : `${credits}회`}
            </span>
          </div>

          <button
            onClick={onOpenPricing}
            className="flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold text-white bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 shadow-lg shadow-purple-600/25 transition-all transform hover:-translate-y-0.5"
          >
            <Crown className="w-4 h-4 text-amber-300" />
            <span>{isPro ? "PRO 구독 중" : "월 5,000원 무제한"}</span>
          </button>
        </div>
      </div>
    </header>
  );
}
