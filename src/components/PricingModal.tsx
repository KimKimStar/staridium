"use client";

import React, { useState } from "react";
import { X, Check, Crown, Zap, Sparkles } from "lucide-react";
import { PRO_PLAN_CONFIG } from "@/lib/stripe";

interface PricingModalProps {
  isOpen: boolean;
  onClose: () => void;
  userEmail?: string;
  userId?: string;
}

export function PricingModal({ isOpen, onClose, userEmail, userId }: PricingModalProps) {
  const [loading, setLoading] = useState(false);

  if (!isOpen) return null;

  const handleSubscribe = async () => {
    setLoading(true);
    try {
      const res = await fetch("/api/stripe/checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          userId: userId || "demo_user",
          email: userEmail || "creator@viralscope.ai",
        }),
      });
      const data = await res.json();
      if (data.url) {
        window.location.href = data.url;
      } else {
        alert("결제 창을 생성하지 못했습니다. 잠시 후 다시 시도해 주세요.");
      }
    } catch (err) {
      console.error(err);
      alert("결제 통신 중 오류가 발생했습니다.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md animate-fadeIn">
      <div className="relative w-full max-w-lg bg-surface border border-primary-500/40 rounded-3xl p-8 shadow-2xl overflow-hidden">
        {/* Glow BG */}
        <div className="absolute top-0 right-0 w-64 h-64 bg-primary-600/20 rounded-full blur-3xl pointer-events-none" />

        <button
          onClick={onClose}
          className="absolute top-5 right-5 w-8 h-8 rounded-full bg-white/5 hover:bg-white/10 flex items-center justify-center text-gray-400 hover:text-white transition-all"
        >
          <X className="w-4 h-4" />
        </button>

        {/* Modal Content */}
        <div className="flex flex-col items-center text-center">
          <div className="w-14 h-14 rounded-2xl bg-gradient-to-tr from-primary-600 to-accent-pink flex items-center justify-center shadow-lg shadow-primary-600/40 mb-4">
            <Crown className="w-7 h-7 text-white" />
          </div>

          <span className="text-xs font-black uppercase tracking-wider text-accent-pink mb-1">
            VIP Creator Membership
          </span>
          <h2 className="text-2xl font-black text-white mb-2">
            ViralScope Pro 무제한 플랜
          </h2>
          <p className="text-xs text-gray-400 max-w-sm mb-6">
            타겟 숏폼 모션 뼈대 추출 + 내 캐릭터 스왑 + 3초 훅 자막 오버레이를 월 5,000원에 무제한으로 누리세요.
          </p>

          {/* Pricing Box */}
          <div className="w-full p-6 rounded-2xl bg-gradient-to-b from-primary-950/40 to-surface-card border border-primary-500/30 mb-6 flex flex-col items-center">
            <div className="flex items-baseline gap-1 text-white">
              <span className="text-4xl font-black tracking-tight">₩{PRO_PLAN_CONFIG.priceKrw.toLocaleString()}</span>
              <span className="text-xs text-gray-400 font-bold">/ 월 (정기 구독)</span>
            </div>
            <span className="text-[11px] text-emerald-400 font-bold mt-1">
              ✓ 대중적 단일 요금제 · 언제든 1초 만에 원클릭 해지 가능
            </span>
          </div>

          {/* Features List */}
          <div className="w-full space-y-2.5 mb-8 text-left">
            {PRO_PLAN_CONFIG.features.map((feat, idx) => (
              <div key={idx} className="flex items-center gap-2.5 text-xs text-gray-300">
                <div className="w-4 h-4 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center flex-shrink-0">
                  <Check className="w-2.5 h-2.5 stroke-[3]" />
                </div>
                <span>{feat}</span>
              </div>
            ))}
          </div>

          {/* Checkout Button */}
          <button
            onClick={handleSubscribe}
            disabled={loading}
            className="w-full py-4 rounded-2xl bg-gradient-to-r from-primary-600 via-primary-500 to-accent-pink hover:opacity-95 text-white font-extrabold text-sm shadow-xl shadow-primary-600/30 transition-all flex items-center justify-center gap-2 disabled:opacity-50 transform hover:-translate-y-0.5"
          >
            {loading ? (
              <span>Stripe 결제창 이동 중...</span>
            ) : (
              <>
                <Sparkles className="w-4 h-4 fill-white" />
                <span>지금 {PRO_PLAN_CONFIG.priceKrw.toLocaleString()}원에 무제한 시작하기</span>
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}
