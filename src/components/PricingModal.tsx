"use client";

import React, { useState } from "react";
import { X, Check, Crown, Sparkles, Zap, ShieldCheck } from "lucide-react";

interface PricingModalProps {
  isOpen: boolean;
  onClose: () => void;
  onPaymentSuccess: () => void;
}

export const PricingModal: React.FC<PricingModalProps> = ({
  isOpen,
  onClose,
  onPaymentSuccess,
}) => {
  const [isLoading, setIsLoading] = useState(false);

  if (!isOpen) return null;

  const handleCheckout = async () => {
    setIsLoading(true);
    try {
      const res = await fetch("/api/stripe/checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
      });

      const data = await res.json();
      if (data.url) {
        if (data.mock) {
          // Mock 테스트 환경일 경우 즉시 로컬 Pro 활성화
          alert("🎉 Stripe 시뮬레이션 결제가 완료되었습니다! Pro 멤버십이 즉시 활성화됩니다.");
          onPaymentSuccess();
          onClose();
        } else {
          // 실제 Stripe 결제창으로 리다이렉트
          window.location.href = data.url;
        }
      }
    } catch (err) {
      console.error("결제 요청 실패:", err);
      alert("결제 요청 중 문제가 발생했습니다.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md">
      <div className="relative w-full max-w-lg rounded-3xl bg-surface border border-primary-500/40 p-6 sm:p-8 shadow-2xl shadow-primary-500/30 overflow-hidden">
        {/* Glow Ambient */}
        <div className="absolute -top-20 -right-20 w-48 h-48 bg-primary-600/30 rounded-full blur-3xl pointer-events-none" />
        <div className="absolute -bottom-20 -left-20 w-48 h-48 bg-accent-pink/20 rounded-full blur-3xl pointer-events-none" />

        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-5 right-5 w-8 h-8 rounded-full bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white flex items-center justify-center transition-all"
        >
          <X className="w-4 h-4" />
        </button>

        {/* Header Badge */}
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-accent-pink/10 border border-accent-pink/30 text-accent-pink text-xs font-bold mb-4">
          <Crown className="w-3.5 h-3.5" />
          <span>무료 크레딧 소진 · Pro 멤버십</span>
        </div>

        {/* Title */}
        <h3 className="text-2xl font-black text-white tracking-tight mb-2">
          숏폼 기획 시간을 90% 단축하고, <br />
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary-400 to-accent-pink">
            알고리즘 떡상 확률을 3배
          </span>
          로 높이세요
        </h3>
        <p className="text-xs text-gray-400 mb-6 leading-relaxed">
          무료 3회 크레딧이 모두 사용되었습니다. Pro 플랜으로 업그레이드하고 매일 쏟아지는 트렌드 영상과 AI 대본 기획안을 무제한으로 열람하세요.
        </p>

        {/* Pricing Card */}
        <div className="p-5 rounded-2xl bg-surface-card border border-primary-500/30 mb-6">
          <div className="flex items-baseline justify-between mb-4">
            <div>
              <span className="text-3xl font-extrabold text-white">₩5,000</span>
              <span className="text-xs text-gray-400"> / 월 (커피 한 잔 가격)</span>
            </div>
            <span className="text-[11px] font-bold px-2 py-0.5 rounded bg-accent-cyan/10 text-accent-cyan border border-cyan-500/30">
              언제든 해지 가능
            </span>
          </div>

          {/* Benefits list */}
          <ul className="space-y-2.5 text-xs text-gray-200">
            <li className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-400 flex-shrink-0" />
              <span>
                <strong>무제한 주제 검색</strong> & 하위 카테고리 자동 추출
              </span>
            </li>
            <li className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-400 flex-shrink-0" />
              <span>
                쇼츠 · 릴스 · 틱톡 <strong>조회수 순 랭킹 전수 분석</strong>
              </span>
            </li>
            <li className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-400 flex-shrink-0" />
              <span>
                <strong>초반 3초 훅 대사 & 시각 연출</strong> AI 정밀 해부
              </span>
            </li>
            <li className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-400 flex-shrink-0" />
              <span>
                내 채널 맞춤형 <strong>신규 기획안 3선 & 컷 편집 템플릿</strong>
              </span>
            </li>
            <li className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-400 flex-shrink-0" />
              <span>원클릭 숏폼 대본 생성 프롬프트 무제한 복사</span>
            </li>
          </ul>
        </div>

        {/* Checkout Button */}
        <button
          onClick={handleCheckout}
          disabled={isLoading}
          className="w-full py-3.5 px-4 rounded-xl text-sm font-bold text-white bg-gradient-to-r from-primary-600 via-primary-500 to-accent-pink hover:from-primary-500 hover:to-pink-500 shadow-xl shadow-primary-500/30 transition-all flex items-center justify-center gap-2 disabled:opacity-50"
        >
          {isLoading ? (
            <>
              <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
              <span>Stripe 안전 결제창 연결 중...</span>
            </>
          ) : (
            <>
              <Zap className="w-4 h-4 fill-current" />
              <span>월 5,000원으로 Pro 무제한 시작하기</span>
            </>
          )}
        </button>

        <div className="mt-3 flex items-center justify-center gap-2 text-[11px] text-gray-500">
          <ShieldCheck className="w-3.5 h-3.5 text-gray-400" />
          <span>Stripe 공식 암호화 보안 결제 시스템 적용</span>
        </div>
      </div>
    </div>
  );
};
