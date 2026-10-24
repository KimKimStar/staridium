"use client";

import React from "react";
import { Header } from "@/components/Header";
import { MotionSwapStudio } from "@/components/MotionSwapStudio";
import Link from "next/link";
import { ArrowLeft, BarChart3, Film } from "lucide-react";

export default function MotionSwapPage() {
  return (
    <div className="min-h-screen bg-[#070b14] text-white flex flex-col">
      {/* Top Global Navigation */}
      <header className="sticky top-0 z-40 w-full border-b border-white/10 bg-slate-950/80 backdrop-blur-md px-6 py-4">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-4">
            <Link
              href="/"
              className="flex items-center gap-2 text-sm text-gray-400 hover:text-white px-3 py-1.5 rounded-xl bg-white/5 hover:bg-white/10 transition-colors"
            >
              <ArrowLeft className="w-4 h-4" />
              <span>대시보드로 돌아가기</span>
            </Link>
            <div className="h-4 w-px bg-white/20" />
            <div className="flex items-center gap-2">
              <span className="p-2 rounded-xl bg-gradient-to-tr from-purple-600 to-pink-600 text-white shadow-md shadow-purple-500/20">
                <Film className="w-5 h-5" />
              </span>
              <span className="font-extrabold text-lg tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-white via-purple-200 to-pink-300">
                ViralScope AI MotionSwap Studio
              </span>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <Link
              href="/"
              className="text-xs font-semibold px-3 py-2 rounded-xl text-gray-400 hover:text-white hover:bg-white/5 transition-colors flex items-center gap-1.5"
            >
              <BarChart3 className="w-4 h-4" />
              바이럴 분석 대시보드
            </Link>
            <span className="text-xs font-bold px-3 py-1.5 rounded-xl bg-purple-500/20 text-purple-300 border border-purple-500/30">
              킬러 기능 MVP
            </span>
          </div>
        </div>
      </header>

      {/* Main Studio Body */}
      <main className="flex-1">
        <MotionSwapStudio />
      </main>
    </div>
  );
}
