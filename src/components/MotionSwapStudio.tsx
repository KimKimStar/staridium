"use client";

import React, { useState, useEffect, useRef } from "react";
import {
  Upload,
  Sparkles,
  Play,
  Download,
  RotateCcw,
  CheckCircle2,
  AlertCircle,
  Film,
  Zap,
  Lock,
  Eye,
  Link as LinkIcon,
  HelpCircle,
  Sliders,
} from "lucide-react";
import { CreditModal } from "./CreditModal";

interface UserStatus {
  userId: string;
  credits: number;
  status: "free" | "pro";
  isPro: boolean;
}

const PRESET_VIDEOS = [
  {
    title: "🔥 240만뷰 댄스/모션 챌린지",
    url: "https://www.youtube.com/shorts/wsXipzlV6wc",
    desc: "경쾌한 전신 움직임과 빠른 컷 전환",
  },
  {
    title: "⚡ 480만뷰 꿀팁 & 후킹 쇼츠",
    url: "https://www.youtube.com/shorts/oTefpEYAc68",
    desc: "제스처와 포인트 강조형 바이럴 모션",
  },
  {
    title: "👑 1200만뷰 표정 & 대화형 숏폼",
    url: "https://www.youtube.com/shorts/U0xCLNMuCZU",
    desc: "상반신 중심의 몰입감 높은 표정 연기",
  },
];

const PRESET_AVATARS = [
  {
    name: "3D 픽사 스타일",
    url: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500&auto=format&fit=crop&q=80",
  },
  {
    name: "20대 여성 크리에이터",
    url: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=500&auto=format&fit=crop&q=80",
  },
  {
    name: "30대 남성 강사",
    url: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500&auto=format&fit=crop&q=80",
  },
  {
    name: "미래 사이버 아바타",
    url: "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=500&auto=format&fit=crop&q=80",
  },
];

const PRESET_HOOKS = [
  "아직도 이거 모르고 계셨나요? 😱",
  "영상 끝까지 보면 인생이 바뀝니다 ⚡",
  "절대 하지 마세요! 99%가 틀리는 습관 ❌",
  "단 3초 만에 100만 조회수 터지는 비결 🔥",
];

export const MotionSwapStudio: React.FC = () => {
  // Input states
  const [targetUrl, setTargetUrl] = useState<string>("https://www.youtube.com/shorts/wsXipzlV6wc");
  const [userImage, setUserImage] = useState<string | null>(PRESET_AVATARS[0].url);
  const [hookText, setHookText] = useState<string>("아직도 이거 모르고 계셨나요? 😱");
  const [isDragging, setIsDragging] = useState<boolean>(false);

  // User & Credit states
  const [userStatus, setUserStatus] = useState<UserStatus>({
    userId: "demo_user",
    credits: 1,
    status: "free",
    isPro: false,
  });
  const [isCreditModalOpen, setIsCreditModalOpen] = useState<boolean>(false);

  // Processing & Output states
  const [isProcessing, setIsProcessing] = useState<boolean>(false);
  const [progressStep, setProgressStep] = useState<number>(0);
  const [progressPercent, setProgressPercent] = useState<number>(0);
  const [resultVideoUrl, setResultVideoUrl] = useState<string | null>(null);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [showSafeZone, setShowSafeZone] = useState<boolean>(true);

  const fileInputRef = useRef<HTMLInputElement>(null);

  // 1. Fetch User Status on Mount
  useEffect(() => {
    fetchUserStatus();

    // Check payment query param
    if (typeof window !== "undefined") {
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.get("payment") === "success") {
        setUserStatus((prev) => ({ ...prev, credits: 999999, status: "pro", isPro: true }));
        alert("🎉 월 5,000원 Pro 무제한 구독이 성공적으로 완료되었습니다! 이제 무제한으로 렌더링하세요.");
      }
    }
  }, []);

  const fetchUserStatus = async () => {
    try {
      const res = await fetch("/api/user/status?userId=demo_user");
      if (res.ok) {
        const data = await res.json();
        setUserStatus(data);
      }
    } catch (e) {
      console.warn("Failed to fetch user status", e);
    }
  };

  // Image Drag & Drop Handlers
  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    const files = e.dataTransfer.files;
    if (files && files[0]) {
      processImageFile(files[0]);
    }
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (files && files[0]) {
      processImageFile(files[0]);
    }
  };

  const processImageFile = (file: File) => {
    if (!file.type.startsWith("image/")) {
      alert("이미지 파일(JPG, PNG, WEBP)만 업로드 가능합니다.");
      return;
    }
    const reader = new FileReader();
    reader.onload = (event) => {
      if (event.target?.result) {
        setUserImage(event.target.result as string);
      }
    };
    reader.readAsDataURL(file);
  };

  // Main Render Action
  const handleStartMotionSwap = async () => {
    setErrorMessage(null);

    // Validation
    if (!targetUrl.trim()) {
      alert("타겟 숏폼 URL을 입력해주세요.");
      return;
    }
    if (!userImage) {
      alert("스왑할 본인 셀카 또는 캐릭터 이미지를 업로드해주세요.");
      return;
    }

    // Check Credit before starting
    if (!userStatus.isPro && userStatus.credits <= 0) {
      setIsCreditModalOpen(true);
      return;
    }

    // Start Simulation of 4-phase progress bar while backend processes
    setIsProcessing(true);
    setProgressPercent(10);
    setProgressStep(1);
    setResultVideoUrl(null);

    // Simulated progress steps for smooth UX
    const timer1 = setTimeout(() => {
      setProgressStep(1);
      setProgressPercent(28);
    }, 1200);

    const timer2 = setTimeout(() => {
      setProgressStep(2);
      setProgressPercent(62);
    }, 3800);

    const timer3 = setTimeout(() => {
      setProgressStep(3);
      setProgressPercent(88);
    }, 6500);

    try {
      const response = await fetch("/api/motion-swap", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          targetUrl,
          userImage,
          hookText,
          userId: userStatus.userId,
        }),
      });

      clearTimeout(timer1);
      clearTimeout(timer2);
      clearTimeout(timer3);

      if (response.status === 402) {
        // Free credits exhausted
        setIsProcessing(false);
        setIsCreditModalOpen(true);
        return;
      }

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "영상 렌더링에 실패했습니다.");
      }

      // Finish progress
      setProgressStep(4);
      setProgressPercent(100);

      setTimeout(() => {
        setIsProcessing(false);
        setResultVideoUrl(data.resultVideoUrl);
        setUserStatus((prev) => ({
          ...prev,
          credits: data.remainingCredits,
          isPro: data.isPro,
        }));
      }, 800);
    } catch (err: any) {
      setIsProcessing(false);
      setErrorMessage(err.message || "영상 처리 중 오류가 발생했습니다.");
    }
  };

  return (
    <div className="w-full max-w-7xl mx-auto px-4 py-8 text-white">
      {/* Top Banner & Header */}
      <div className="mb-8 flex flex-col md:flex-row md:items-center justify-between gap-4 p-6 rounded-3xl bg-gradient-to-r from-purple-950/60 via-slate-900 to-indigo-950/60 border border-purple-500/30 backdrop-blur-xl shadow-2xl">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 mb-2 text-xs font-bold text-purple-300 bg-purple-500/20 border border-purple-500/30 rounded-full">
            <Sparkles className="w-3.5 h-3.5 text-amber-300" />
            저작권 침해 제로 · 순수 모션 & 템플릿 복제 엔진
          </div>
          <h1 className="text-2xl sm:text-3xl font-black tracking-tight">
            AI 모션 스왑 기반 숏폼 템플릿 렌더링 스튜디오
          </h1>
          <p className="text-sm text-gray-400 mt-1">
            타인의 떡상 영상에서 <strong className="text-purple-300">‘모션 뼈대’</strong>와 <strong className="text-pink-300">‘3초 후킹 타이밍’</strong>만 추출하고, 내 캐릭터로 완벽 탈바꿈합니다.
          </p>
        </div>

        {/* User Credit Status Card */}
        <div className="flex items-center gap-3 bg-black/40 border border-white/10 p-3.5 rounded-2xl">
          <div className="text-right">
            <span className="text-xs text-gray-400 block">내 계정 상태</span>
            {userStatus.isPro ? (
              <span className="text-sm font-extrabold text-amber-300 flex items-center gap-1 justify-end">
                <Sparkles className="w-4 h-4 fill-amber-300 text-amber-300" />
                PRO 무제한 멤버십
              </span>
            ) : (
              <span className="text-sm font-extrabold text-purple-300">
                무료 체험: <strong className="text-white text-base">{userStatus.credits}</strong>회 남음
              </span>
            )}
          </div>
          {!userStatus.isPro && (
            <button
              onClick={() => setIsCreditModalOpen(true)}
              className="py-2 px-3.5 rounded-xl font-bold text-xs bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 text-white shadow-md shadow-purple-600/30 transition-all flex items-center gap-1"
            >
              <Zap className="w-3.5 h-3.5 fill-current text-amber-300" />
              월 5,000원 무제한
            </button>
          )}
        </div>
      </div>

      {/* Main Split Grid (Left: Inputs, Right: Processing & Results) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        {/* ================= LEFT COLUMN: INPUTS (7 Cols) ================= */}
        <div className="lg:col-span-7 space-y-6">
          {/* Section 1: Target Video URL Input */}
          <div className="p-6 rounded-3xl bg-slate-900/90 border border-white/10 shadow-xl backdrop-blur-md">
            <div className="flex items-center justify-between mb-3">
              <label className="text-sm font-bold text-gray-200 flex items-center gap-2">
                <span className="w-6 h-6 rounded-full bg-purple-600/30 text-purple-300 text-xs flex items-center justify-center font-black">1</span>
                벤치마킹 타겟 숏폼 URL
              </label>
              <span className="text-xs text-purple-400">유튜브 쇼츠 / 릴스 / 틱톡 지원</span>
            </div>

            <div className="relative mb-3">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-gray-500">
                <LinkIcon className="w-4 h-4" />
              </div>
              <input
                type="url"
                value={targetUrl}
                onChange={(e) => setTargetUrl(e.target.value)}
                placeholder="https://www.youtube.com/shorts/..."
                className="w-full pl-10 pr-4 py-3 rounded-xl bg-black/60 border border-white/15 text-sm text-white placeholder-gray-500 focus:outline-none focus:border-purple-500 transition-colors"
              />
            </div>

            {/* Quick Benchmark Preset Buttons */}
            <div className="space-y-1.5">
              <span className="text-[11px] font-semibold text-gray-400 uppercase tracking-wider block">
                검증된 바이럴 모션 템플릿 빠른 선택:
              </span>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
                {PRESET_VIDEOS.map((pv, idx) => (
                  <button
                    key={idx}
                    type="button"
                    onClick={() => setTargetUrl(pv.url)}
                    className={`p-2.5 rounded-xl border text-left text-xs transition-all ${
                      targetUrl === pv.url
                        ? "bg-purple-600/20 border-purple-500 text-white shadow-md shadow-purple-600/20"
                        : "bg-white/[0.03] border-white/10 text-gray-300 hover:bg-white/[0.08]"
                    }`}
                  >
                    <div className="font-bold truncate">{pv.title}</div>
                    <div className="text-[10px] text-gray-400 truncate mt-0.5">{pv.desc}</div>
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Section 2: Drag & Drop Character/Selfie Image Upload */}
          <div className="p-6 rounded-3xl bg-slate-900/90 border border-white/10 shadow-xl backdrop-blur-md">
            <div className="flex items-center justify-between mb-3">
              <label className="text-sm font-bold text-gray-200 flex items-center gap-2">
                <span className="w-6 h-6 rounded-full bg-pink-600/30 text-pink-300 text-xs flex items-center justify-center font-black">2</span>
                내 셀카 / 캐릭터 이미지 (모션 스왑 대상)
              </label>
              <span className="text-xs text-pink-400">Drag & Drop 또는 파일 업로드</span>
            </div>

            {/* Drag & Drop Box */}
            <div
              onDragOver={handleDragOver}
              onDragLeave={handleDragLeave}
              onDrop={handleDrop}
              onClick={() => fileInputRef.current?.click()}
              className={`relative border-2 border-dashed rounded-2xl p-6 text-center cursor-pointer transition-all ${
                isDragging
                  ? "border-pink-500 bg-pink-500/10 scale-[1.01]"
                  : "border-white/15 bg-black/40 hover:border-pink-500/50 hover:bg-white/[0.02]"
              }`}
            >
              <input
                ref={fileInputRef}
                type="file"
                accept="image/*"
                onChange={handleFileChange}
                className="hidden"
              />

              {userImage ? (
                <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
                  <div className="relative w-24 h-32 rounded-xl overflow-hidden border-2 border-pink-500 shadow-lg shadow-pink-500/20 flex-shrink-0">
                    <img
                      src={userImage}
                      alt="Uploaded character"
                      className="w-full h-full object-cover"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end justify-center p-1">
                      <span className="text-[10px] font-bold text-pink-200">선택 완료</span>
                    </div>
                  </div>
                  <div className="text-left">
                    <div className="inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-bold text-emerald-400 bg-emerald-500/10 rounded-full mb-1">
                      <CheckCircle2 className="w-3.5 h-3.5" />
                      스왑 이미지 준비됨
                    </div>
                    <p className="text-xs text-gray-300">
                      클릭하거나 새 이미지를 끌어다 놓으면 다른 사진으로 교체됩니다.
                    </p>
                    <span className="text-[11px] text-pink-400 underline mt-1 inline-block">
                      다른 사진으로 변경하기
                    </span>
                  </div>
                </div>
              ) : (
                <div className="py-4">
                  <div className="w-12 h-12 mx-auto mb-3 rounded-2xl bg-pink-500/10 border border-pink-500/20 text-pink-400 flex items-center justify-center">
                    <Upload className="w-6 h-6" />
                  </div>
                  <p className="text-sm font-bold text-white mb-1">
                    본인 셀카 또는 캐릭터 사진을 여기에 끌어다 놓으세요
                  </p>
                  <p className="text-xs text-gray-400">
                    JPG, PNG, WEBP 권장 (얼굴과 전신이 또렷할수록 애니메이팅 품질 극대화)
                  </p>
                </div>
              )}
            </div>

            {/* Quick Avatar Presets */}
            <div className="mt-4">
              <span className="text-[11px] font-semibold text-gray-400 uppercase tracking-wider block mb-2">
                또는 준비된 AI 캐릭터 아바타 프리셋 선택:
              </span>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                {PRESET_AVATARS.map((avatar, idx) => (
                  <button
                    key={idx}
                    type="button"
                    onClick={() => setUserImage(avatar.url)}
                    className={`flex items-center gap-2 p-1.5 pr-2.5 rounded-xl border transition-all text-left ${
                      userImage === avatar.url
                        ? "bg-pink-600/20 border-pink-500 text-white"
                        : "bg-white/[0.02] border-white/10 text-gray-300 hover:bg-white/[0.06]"
                    }`}
                  >
                    <img
                      src={avatar.url}
                      alt={avatar.name}
                      className="w-8 h-8 rounded-lg object-cover"
                    />
                    <span className="text-xs font-semibold truncate">{avatar.name}</span>
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Section 3: 3-Second Hook Subtitle Text */}
          <div className="p-6 rounded-3xl bg-slate-900/90 border border-white/10 shadow-xl backdrop-blur-md">
            <div className="flex items-center justify-between mb-3">
              <label className="text-sm font-bold text-gray-200 flex items-center gap-2">
                <span className="w-6 h-6 rounded-full bg-amber-600/30 text-amber-300 text-xs flex items-center justify-center font-black">3</span>
                초반 0~3초 시선강탈 훅 자막 (FFmpeg 자동 오버레이)
              </label>
              <span className="text-xs text-amber-400">노란색 하이라이트 박스</span>
            </div>

            <input
              type="text"
              value={hookText}
              onChange={(e) => setHookText(e.target.value)}
              placeholder="예: 아직도 이거 모르고 계셨나요? 😱"
              className="w-full px-4 py-3 rounded-xl bg-black/60 border border-white/15 text-sm text-white placeholder-gray-500 focus:outline-none focus:border-amber-500 transition-colors mb-3"
            />

            {/* Quick Hook Presets */}
            <div className="flex flex-wrap gap-1.5">
              {PRESET_HOOKS.map((hook, idx) => (
                <button
                  key={idx}
                  type="button"
                  onClick={() => setHookText(hook)}
                  className="px-2.5 py-1 rounded-lg bg-white/[0.04] hover:bg-amber-500/20 hover:text-amber-300 text-xs text-gray-300 border border-white/10 transition-colors"
                >
                  {hook}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* ================= RIGHT COLUMN: ACTION & RESULT (5 Cols) ================= */}
        <div className="lg:col-span-5 space-y-6">
          {/* Main Action Trigger Card */}
          <div className="p-6 rounded-3xl bg-gradient-to-b from-slate-900 to-black border border-purple-500/30 shadow-2xl">
            <h3 className="text-lg font-bold text-white mb-2 flex items-center gap-2">
              <Film className="w-5 h-5 text-purple-400" />
              원클릭 렌더링 엔진 가동
            </h3>
            <p className="text-xs text-gray-400 mb-5 leading-relaxed">
              입력하신 타겟 영상의 포즈/모션 뼈대와 사용자 이미지를 Replicate AnimateAnyone으로 결합하고, FFmpeg 3초 훅 자막을 9:16 황금 비율로 오버레이합니다.
            </p>

            {/* Render Button */}
            <button
              onClick={handleStartMotionSwap}
              disabled={isProcessing}
              className="w-full py-4 px-6 rounded-2xl font-black text-base bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 hover:from-purple-500 hover:to-amber-400 text-white shadow-xl shadow-purple-600/30 hover:shadow-purple-600/50 transition-all flex items-center justify-center gap-2.5 disabled:opacity-50 disabled:cursor-not-allowed group"
            >
              {isProcessing ? (
                <>
                  <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                  <span>AI 모션 스왑 및 렌더링 진행 중...</span>
                </>
              ) : (
                <>
                  <Zap className="w-5 h-5 fill-current text-amber-200 group-hover:scale-110 transition-transform" />
                  <span>영상 템플릿화 및 모션 스왑 시작</span>
                </>
              )}
            </button>

            {/* Credit Notice below button */}
            <div className="mt-3 flex items-center justify-between text-xs text-gray-400">
              <span>필요 크레딧: 1회 (또는 Pro 무제한)</span>
              {!userStatus.isPro && (
                <button
                  onClick={() => setIsCreditModalOpen(true)}
                  className="text-purple-400 hover:text-purple-300 underline font-semibold"
                >
                  월 5,000원에 무제한 구독
                </button>
              )}
            </div>
          </div>

          {/* Progress Window (Active when processing) */}
          {isProcessing && (
            <div className="p-6 rounded-3xl bg-slate-900 border border-purple-500/40 shadow-2xl animate-pulse-subtle">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-bold text-purple-300 uppercase tracking-wider">
                  렌더링 파이프라인 가동 중
                </span>
                <span className="text-sm font-black text-amber-400">{progressPercent}%</span>
              </div>

              {/* Progress Bar Track */}
              <div className="w-full h-3 bg-black/60 rounded-full overflow-hidden p-0.5 border border-white/10 mb-4">
                <div
                  className="h-full bg-gradient-to-r from-purple-500 via-pink-500 to-amber-400 rounded-full transition-all duration-500 ease-out"
                  style={{ width: `${progressPercent}%` }}
                />
              </div>

              {/* Multi-step Status Indicator */}
              <div className="space-y-2.5 text-xs">
                <div className={`flex items-center gap-2.5 ${progressStep >= 1 ? "text-purple-300 font-bold" : "text-gray-500"}`}>
                  <div className={`w-4 h-4 rounded-full flex items-center justify-center text-[10px] ${progressStep >= 1 ? "bg-purple-500 text-white" : "bg-white/10"}`}>
                    1
                  </div>
                  <span>타겟 영상 모션 뼈대(Pose Skeleton) 및 타이밍 분석</span>
                </div>

                <div className={`flex items-center gap-2.5 ${progressStep >= 2 ? "text-pink-300 font-bold" : "text-gray-500"}`}>
                  <div className={`w-4 h-4 rounded-full flex items-center justify-center text-[10px] ${progressStep >= 2 ? "bg-pink-500 text-white" : "bg-white/10"}`}>
                    2
                  </div>
                  <span>Replicate AnimateAnyone 이미지 스왑 & 애니메이팅</span>
                </div>

                <div className={`flex items-center gap-2.5 ${progressStep >= 3 ? "text-amber-300 font-bold" : "text-gray-500"}`}>
                  <div className={`w-4 h-4 rounded-full flex items-center justify-center text-[10px] ${progressStep >= 3 ? "bg-amber-500 text-black font-black" : "bg-white/10"}`}>
                    3
                  </div>
                  <span>FFmpeg 9:16 인코딩 & 3초 훅 자막 하이라이트 오버레이</span>
                </div>

                <div className={`flex items-center gap-2.5 ${progressStep >= 4 ? "text-emerald-400 font-bold" : "text-gray-500"}`}>
                  <div className={`w-4 h-4 rounded-full flex items-center justify-center text-[10px] ${progressStep >= 4 ? "bg-emerald-500 text-white" : "bg-white/10"}`}>
                    4
                  </div>
                  <span>세로 풀HD MP4 최종 완성</span>
                </div>
              </div>
            </div>
          )}

          {/* Error Message Box */}
          {errorMessage && (
            <div className="p-4 rounded-2xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs flex items-start gap-2.5">
              <AlertCircle className="w-4 h-4 flex-shrink-0 mt-0.5" />
              <span>{errorMessage}</span>
            </div>
          )}

          {/* Result Player Card (Appears after completion) */}
          {resultVideoUrl && (
            <div className="p-6 rounded-3xl bg-slate-900 border border-emerald-500/40 shadow-2xl animate-fade-in">
              <div className="flex items-center justify-between mb-3">
                <span className="inline-flex items-center gap-1.5 text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-full border border-emerald-500/20">
                  <CheckCircle2 className="w-3.5 h-3.5" />
                  9:16 쇼츠 렌더링 완료!
                </span>
                <button
                  type="button"
                  onClick={() => setShowSafeZone(!showSafeZone)}
                  className={`text-[11px] px-2.5 py-1 rounded-lg border transition-colors flex items-center gap-1 ${
                    showSafeZone
                      ? "bg-purple-600/20 border-purple-500 text-purple-300"
                      : "bg-white/5 border-white/10 text-gray-400"
                  }`}
                >
                  <Eye className="w-3 h-3" />
                  Safe Zone 가이드 {showSafeZone ? "ON" : "OFF"}
                </button>
              </div>

              {/* 9:16 Vertical Player Frame */}
              <div className="relative mx-auto w-full max-w-[280px] aspect-[9/16] bg-black rounded-2xl overflow-hidden border-2 border-white/10 shadow-inner group">
                <video
                  src={resultVideoUrl}
                  controls
                  autoPlay
                  loop
                  playsInline
                  className="w-full h-full object-cover"
                />

                {/* Safe Zone Overlay Guide (Shows Instagram Reels & YouTube Shorts safe bounds) */}
                {showSafeZone && (
                  <div className="absolute inset-0 pointer-events-none border border-cyan-400/30 flex flex-col justify-between p-3">
                    <div className="p-1 rounded bg-black/50 text-[9px] text-cyan-300 self-start">
                      ▲ 프로필/채널명 영역 (Safe Zone)
                    </div>
                    <div className="p-1 rounded bg-black/50 text-[9px] text-yellow-300 self-center">
                      ★ 3초 훅 자막 황금 배치존 (Y: 68%)
                    </div>
                    <div className="p-1 rounded bg-black/50 text-[9px] text-cyan-300 self-start">
                      ▼ 제목 & 사운드 바 영역 (Safe Zone)
                    </div>
                  </div>
                )}
              </div>

              {/* Action Buttons */}
              <div className="mt-5 space-y-2.5">
                <a
                  href={resultVideoUrl}
                  download="ViralScope_Motion_Swap.mp4"
                  className="w-full py-3.5 px-4 rounded-xl font-bold text-sm bg-emerald-500 hover:bg-emerald-400 text-black flex items-center justify-center gap-2 shadow-lg shadow-emerald-500/20 transition-all"
                >
                  <Download className="w-4 h-4 stroke-[2.5]" />
                  <span>완성 쇼츠 다운로드 (1080x1920 MP4)</span>
                </a>

                <button
                  type="button"
                  onClick={() => {
                    setResultVideoUrl(null);
                    setProgressPercent(0);
                    setProgressStep(0);
                  }}
                  className="w-full py-3 px-4 rounded-xl font-bold text-xs bg-white/5 hover:bg-white/10 text-gray-300 border border-white/10 flex items-center justify-center gap-1.5 transition-colors"
                >
                  <RotateCcw className="w-3.5 h-3.5" />
                  <span>다른 이미지 / 문구로 새 영상 만들기</span>
                </button>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Stripe 5,000 KRW Checkout Modal */}
      <CreditModal
        isOpen={isCreditModalOpen}
        onClose={() => setIsCreditModalOpen(false)}
        userId={userStatus.userId}
      />
    </div>
  );
};
