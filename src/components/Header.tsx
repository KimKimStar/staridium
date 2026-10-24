"use client";

import React from "react";
import { Sparkles, Crown, Zap } from "lucide-react";

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
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-primary-600 to-accent-cyan flex items-center justify-center shadow-lg shadow-primary-600/30">
            <Sparkles className="w-5 h-5 text-white" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-extrabold text-xl tracking-tight bg-gradient-to-r from-white via-primary-100 to-accent-cyan bg-clip-text text-transparent">
                ViralScope AI
              </span>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-primary-500/20 text-primary-400 border border-primary-500/30">
                PROD v2.0
              </span>
            </div>
            <p className="text-xs text-gray-400">숏폼 바이럴 해부학 & 사전 기획 자동화 SaaS</p>
          </div>
        </div>

        {/* Right Actions: Credit & Pro Button */}
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-surface border border-surface-border">
            <Zap className="w-4 h-4 text-amber-400 fill-amber-400" />
            <span className="text-xs text-gray-400 font-medium">잔여 크레딧:</span>
            <span className="text-sm font-bold text-amber-300">
              {isPro ? "무제한 PRO" : `${credits}회`}
            </span>
          </div>

          <button
            onClick={onOpenPricing}
            className="flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold text-white bg-gradient-to-r from-primary-600 to-accent-pink hover:opacity-90 shadow-lg shadow-primary-600/25 transition-all transform hover:-translate-y-0.5"
          >
            <Crown className="w-4 h-4" />
            <span>{isPro ? "구독 관리" : "PRO 업그레이드 (월 19,000원)"}</span>
          </button>
        </div>
      </div>
    </header>
  );
}
