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
    <header className="sticky top-0 z-40 border-b border-slate-800 bg-slate-950/80 backdrop-blur-xl px-6 py-4">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        {/* Brand */}
        <div className="flex items-center gap-3">
          <Link href="/" className="flex items-center gap-3 group">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 to-violet-600 flex items-center justify-center shadow-lg shadow-blue-500/25 group-hover:scale-105 transition-transform">
              <Sparkles className="w-5 h-5 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-extrabold text-xl tracking-tight bg-gradient-to-r from-white via-slate-100 to-blue-400 bg-clip-text text-transparent">
                  ViralScope AI
                </span>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/30">
                  SaaS Pro
                </span>
              </div>
              <p className="text-xs text-slate-400">숏폼 바이럴 해부학 & AI 모션 스왑 엔진</p>
            </div>
          </Link>
        </div>

        {/* Center Navigation: Motion Swap Killer Feature */}
        <div className="hidden md:flex items-center gap-2">
          <Link
            href="/motion-swap"
            className="flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-black text-amber-200 bg-gradient-to-r from-violet-950/60 via-purple-900/60 to-slate-900/80 border border-amber-500/40 shadow-lg shadow-violet-600/20 hover:border-amber-400 hover:scale-[1.02] transition-all"
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
          <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-700/60 shadow-sm">
            <Zap className="w-4 h-4 text-amber-400 fill-amber-400" />
            <span className="text-xs text-slate-400 font-medium hidden sm:inline">잔여 크레딧:</span>
            <span className="text-sm font-bold text-amber-300">
              {isPro ? "무제한 PRO" : `${credits}회`}
            </span>
          </div>

          <button
            onClick={onOpenPricing}
            className={`flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-bold transition-all ${
              isPro
                ? "bg-slate-800 text-slate-300 border border-slate-700/80 cursor-default"
                : "bg-gradient-to-r from-blue-600 to-violet-600 hover:from-blue-500 hover:to-violet-500 text-white shadow-lg shadow-blue-500/25 active:scale-95"
            }`}
          >
            <Crown className="w-4 h-4 text-amber-300" />
            <span>{isPro ? "PRO 구독 중" : "PRO 구독 (월 5,000원)"}</span>
          </button>
        </div>
      </div>
    </header>
  );
}
