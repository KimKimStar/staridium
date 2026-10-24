"use client";

import React, { useState } from "react";
import { PRO_PLAN_CONFIG } from "@/lib/stripe";
import { Sparkles, Check, X, ShieldCheck, Zap } from "lucide-react";

interface CreditModalProps {
  isOpen: boolean;
  onClose: () => void;
  userId?: string;
  email?: string;
}

export const CreditModal: React.FC<CreditModalProps> = ({
  isOpen,
  onClose,
  userId = "demo_user",
  email = "creator@viralscope.ai",
}) => {
  const [loading, setLoading] = useState(false);

  if (!isOpen) return null;

  const handleCheckout = async () => {
    setLoading(true);
    try {
      const res = await fetch("/api/stripe/checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ userId, email }),
      });

      const data = await res.json();
      if (data.url) {
        window.location.href = data.url;
      } else {
        alert(data.error || "결제 페이지로 이동하는 중 문제가 발생했습니다.");
        setLoading(false);
      }
    } catch (e: any) {
      alert("결제 요청 실패: " + e.message);
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md animate-fade-in">
      <div className="relative w-full max-w-lg p-6 sm:p-8 bg-gradient-to-b from-gray-900 via-gray-900 to-black border border-purple-500/40 rounded-3xl shadow-2xl shadow-purple-500/20 text-white">
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-5 right-5 p-2 text-gray-400 hover:text-white rounded-full bg-white/5 hover:bg-white/10 transition-colors"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Badge */}
        <div className="inline-flex items-center gap-1.5 px-3 py-1 mb-4 text-xs font-bold text-amber-400 bg-amber-500/10 border border-amber-500/30 rounded-full">
          <Sparkles className="w-3.5 h-3.5" />
          무료 체험 크레딧(1회) 소진 완료
        </div>

        {/* Title */}
        <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight mb-2">
          월 <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 via-pink-400 to-amber-300">5,000원</span>으로<br />
          AI 모션 스왑을 무제한 이용하세요!
        </h2>
        <p className="text-sm text-gray-400 mb-6 leading-relaxed">
          타인의 떡상 숏폼에서 '모션 뼈대'만 따오고 내 캐릭터를 덧씌워 저작권 걱정 없이 하루 수십 개의 바이럴 쇼츠를 무제한 렌더링하세요.
        </p>

        {/* Plan Feature Box */}
        <div className="p-5 mb-6 rounded-2xl bg-white/[0.04] border border-white/10">
          <div className="flex items-baseline justify-between mb-4">
            <div>
              <span className="text-lg font-bold text-white">Pro 무제한 구독</span>
              <p className="text-xs text-purple-400">대중적 단일 요금제 (언제든 해지 가능)</p>
            </div>
            <div className="text-right">
              <span className="text-3xl font-black text-amber-300">₩5,000</span>
              <span className="text-xs text-gray-400"> / 월</span>
            </div>
          </div>

          <div className="space-y-2.5 text-xs sm:text-sm text-gray-300">
            {PRO_PLAN_CONFIG.features.map((feature, idx) => (
              <div key={idx} className="flex items-center gap-2.5">
                <div className="flex-shrink-0 w-4 h-4 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center">
                  <Check className="w-3 h-3 stroke-[3]" />
                </div>
                <span>{feature}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Checkout Button */}
        <button
          onClick={handleCheckout}
          disabled={loading}
          className="w-full py-4 px-6 rounded-xl font-extrabold text-base bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 hover:from-purple-500 hover:to-amber-400 text-white shadow-lg shadow-purple-600/30 hover:shadow-purple-600/50 transition-all flex items-center justify-center gap-2 group disabled:opacity-60"
        >
          {loading ? (
            <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
          ) : (
            <>
              <Zap className="w-5 h-5 fill-current text-amber-200" />
              <span>지금 월 5,000원에 무제한 시작하기 (Stripe 결제)</span>
            </>
          )}
        </button>

        {/* Security Assurance */}
        <div className="mt-4 flex items-center justify-center gap-1.5 text-xs text-gray-500">
          <ShieldCheck className="w-4 h-4 text-emerald-500" />
          <span>Stripe 공식 글로벌 보안 결제 · 언제든 원클릭 구독 해지 가능</span>
        </div>
      </div>
    </div>
  );
};
