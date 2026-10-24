"use client";

import React, { useState, useEffect, useMemo, useCallback } from "react";
import { Header } from "@/components/Header";
import { SearchBar } from "@/components/SearchBar";
import { PeriodFilter } from "@/components/PeriodFilter";
import { SubTopicTabs } from "@/components/SubTopicTabs";
import { VideoList } from "@/components/VideoList";
import { SkeletonLoader } from "@/components/SkeletonLoader";
import { AnalysisModal } from "@/components/AnalysisModal";
import { PricingModal } from "@/components/PricingModal";
import {
  PlatformType,
  PeriodFilterType,
  SearchAnalysisResult,
  VideoDetailAnalysis,
  ViralVideo,
  SubTopic,
} from "@/types";
import { Sparkles, TrendingUp, Filter } from "lucide-react";

export default function HomePage() {
  // 1. 크레딧 및 Pro 구독 상태 관리 (신규 사용자 3 크레딧 기본 제공)
  const [credits, setCredits] = useState<number>(3);
  const [isPro, setIsPro] = useState<boolean>(false);
  const [isPricingOpen, setIsPricingOpen] = useState<boolean>(false);

  // 2. 검색, 기간 필터 및 데이터 상태 관리
  const [keyword, setKeyword] = useState<string>("인간관계");
  const [period, setPeriod] = useState<PeriodFilterType>("1m");
  const [platformFilter, setPlatformFilter] = useState<PlatformType>("all");
  const [activeSubTopic, setActiveSubTopic] = useState<string>("all");
  const [subTopics, setSubTopics] = useState<SubTopic[]>([]);
  const [videos, setVideos] = useState<ViralVideo[]>([]);

  // 3. 비동기 로딩 및 모달 상태
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [selectedVideo, setSelectedVideo] = useState<ViralVideo | null>(null);
  const [detailAnalysis, setDetailAnalysis] = useState<VideoDetailAnalysis | null>(null);
  const [isAnalyzingDetail, setIsAnalyzingDetail] = useState<boolean>(false);

  // 초기화: 로컬스토리지에서 크레딧 및 구독 정보 복원
  useEffect(() => {
    if (typeof window !== "undefined") {
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.get("payment") === "success") {
        setIsPro(true);
        localStorage.setItem("viralscope_is_pro", "true");
      } else {
        const savedPro = localStorage.getItem("viralscope_is_pro");
        if (savedPro === "true") setIsPro(true);
      }

      const savedCredits = localStorage.getItem("viralscope_credits");
      if (savedCredits !== null) {
        setCredits(parseInt(savedCredits, 10));
      } else {
        localStorage.setItem("viralscope_credits", "3");
      }
    }
  }, []);

  // 랭킹 및 하위 주제 데이터 가져오기 (기간 필터 + 검색어)
  const fetchRankingData = useCallback(async (kw: string, p: PeriodFilterType, plat: PlatformType) => {
    setIsLoading(true);
    try {
      // 1. 기간별 조회수 랭킹 API 호출
      const res = await fetch(`/api/ranking?keyword=${encodeURIComponent(kw)}&period=${p}&platform=${plat}`);
      if (res.ok) {
        const data = await res.json();
        if (data.videos && data.videos.length > 0) {
          setVideos(data.videos);
        }
      }

      // 2. 하위 주제 분류 API 호출 (분류가 없는 경우 Gemini 자동 클러스터링)
      const analyzeRes = await fetch("/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ keyword: kw }),
      });
      if (analyzeRes.ok) {
        const analyzeData: SearchAnalysisResult = await analyzeRes.json();
        if (analyzeData.subTopics && analyzeData.subTopics.length > 0) {
          setSubTopics(analyzeData.subTopics);
        }
      }
    } catch (err) {
      console.error("[Fetch Error]:", err);
    } finally {
      setIsLoading(false);
    }
  }, []);

  // 최초 로드 시 기본 랭킹 조회
  useEffect(() => {
    fetchRankingData(keyword, period, platformFilter);
  }, []);

  // 기간 필터 변경 핸들러
  const handlePeriodChange = (newPeriod: PeriodFilterType) => {
    setPeriod(newPeriod);
    fetchRankingData(keyword, newPeriod, platformFilter);
  };

  // 플랫폼 필터 변경 핸들러
  const handlePlatformChange = (newPlat: PlatformType) => {
    setPlatformFilter(newPlat);
    fetchRankingData(keyword, period, newPlat);
  };

  // 검색창 입력 핸들러
  const handleSearch = (kw: string) => {
    setKeyword(kw);
    setActiveSubTopic("all");
    fetchRankingData(kw, period, platformFilter);
  };

  // 영상 카드 클릭 시 AI 딥다이브 분석 실행 (크레딧 체크 및 Gemini API 연동)
  const handleOpenAnalysis = async (video: ViralVideo) => {
    // 1. 크레딧 소진 체크 (Pro 미구독자)
    if (!isPro && credits <= 0) {
      setIsPricingOpen(true);
      return;
    }

    setSelectedVideo(video);
    setIsAnalyzingDetail(true);
    setDetailAnalysis(null);

    // 2. 무료 크레딧 차감 (Pro가 아닐 때 1회 차감)
    if (!isPro) {
      const nextCredits = Math.max(0, credits - 1);
      setCredits(nextCredits);
      localStorage.setItem("viralscope_credits", nextCredits.toString());
    }

    try {
      // 3. Gemini API 딥다이브 분석 라우트 호출 (4대 요소 정밀 해부)
      const res = await fetch("/api/deep-dive", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ video }),
      });

      if (!res.ok) {
        const errorData = await res.json();
        if (res.status === 402 || errorData.requireSubscription) {
          setIsPricingOpen(true);
          setSelectedVideo(null);
          return;
        }
        throw new Error(errorData.error || "분석 실패");
      }

      const data = await res.json();
      setDetailAnalysis(data.analysis);
    } catch (err) {
      console.error("[Deep Dive Error]:", err);
      // Fallback detail analysis call
      try {
        const fallbackRes = await fetch("/api/video-detail", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ video }),
        });
        if (fallbackRes.ok) {
          const fbData = await fallbackRes.json();
          setDetailAnalysis(fbData);
        }
      } catch (fbErr) {
        console.error("[Fallback Error]:", fbErr);
      }
    } finally {
      setIsAnalyzingDetail(false);
    }
  };

  // 필터링된 영상 목록 (하위 주제별 필터)
  const filteredVideos = useMemo(() => {
    if (activeSubTopic === "all") return videos;
    return videos.filter((v) => v.subTopicId === activeSubTopic || v.subCategory === activeSubTopic);
  }, [videos, activeSubTopic]);

  return (
    <div className="min-h-screen flex flex-col bg-background text-gray-100 relative selection:bg-primary-500 selection:text-white">
      {/* Background Decorative Ambient Glow */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-7xl h-96 bg-hero-glow pointer-events-none" />

      {/* 1. Global Navigation Header (크레딧 & Pro 버튼) */}
      <Header
        credits={credits}
        isPro={isPro}
        onOpenPricing={() => setIsPricingOpen(true)}
      />

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 z-10 flex flex-col gap-8">
        {/* 상단 검색 영역 & 우측 상단 기간 필터 */}
        <section className="flex flex-col gap-6">
          <div className="text-center max-w-2xl mx-auto space-y-2">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-primary-500/10 border border-primary-500/20 text-primary-400 text-xs font-bold">
              <Sparkles className="w-3.5 h-3.5" />
              <span>크리에이터를 위한 AI 숏폼 바이럴 해부학 엔진</span>
            </div>
            <h1 className="text-3xl sm:text-4xl font-black text-white tracking-tight">
              터지는 숏폼의 <span className="bg-gradient-to-r from-primary-400 to-accent-pink bg-clip-text text-transparent">성공 공식</span>을 즉시 복제하세요
            </h1>
            <p className="text-xs sm:text-sm text-gray-400">
              유튜브 쇼츠(YouTube Shorts)의 폭발적 실시간 조회수 원인을 Gemini AI로 1초 만에 해부합니다.
            </p>
          </div>

          {/* 중앙 메인 검색창 */}
          <SearchBar onSearch={handleSearch} isLoading={isLoading} />

          {/* 필터 컨트롤 바: 하위 주제 안내 및 우측 상단 '기간 필터' */}
          <div className="flex items-center justify-between flex-wrap gap-4 pt-2">
            <div className="flex items-center gap-2">
              <TrendingUp className="w-4 h-4 text-primary-400" />
              <span className="text-sm font-bold text-white">
                ‘{keyword}’ 키워드 떡상 랭킹
              </span>
              <span className="text-xs text-gray-400">
                (조회수 역순 정렬)
              </span>
            </div>

            {/* 우측 상단 기간 필터 드롭다운/버튼 (1일, 1주일, 1개월, 3개월, 6개월, 1년, 역대) */}
            <PeriodFilter
              selectedPeriod={period}
              onChange={handlePeriodChange}
            />
          </div>

          {/* 하위 주제 탭 (Tab) 및 플랫폼 필터 */}
          <SubTopicTabs
            subTopics={subTopics}
            selectedSubTopic={activeSubTopic}
            onSelectSubTopic={setActiveSubTopic}
            selectedPlatform={platformFilter}
            onSelectPlatform={handlePlatformChange}
            totalVideosCount={filteredVideos.length}
          />
        </section>

        {/* 랭킹 대시보드: API 통신 중 스켈레톤, 완료 후 조회수 순 썸네일 그리드 */}
        <section className="flex-1">
          {isLoading ? (
            <SkeletonLoader />
          ) : (
            <VideoList
              videos={filteredVideos}
              onSelectVideo={handleOpenAnalysis}
            />
          )}
        </section>
      </main>

      {/* 4대 핵심 AI 딥다이브 분석 모달 */}
      <AnalysisModal
        analysis={detailAnalysis}
        isOpen={!!selectedVideo}
        isLoading={isAnalyzingDetail}
        onClose={() => setSelectedVideo(null)}
      />

      {/* 월 19,000원 Stripe 무제한 정기구독 결제 모달 */}
      <PricingModal
        isOpen={isPricingOpen}
        onClose={() => setIsPricingOpen(false)}
        onPaymentSuccess={() => {
          setIsPro(true);
          localStorage.setItem("viralscope_is_pro", "true");
        }}
      />

      {/* Footer */}
      <footer className="w-full border-t border-surface-border py-6 bg-surface/40 text-center text-xs text-gray-500">
        <p>© 2026 ViralScope AI. All rights reserved. Powered by Google Gemini AI & Supabase.</p>
      </footer>
    </div>
  );
}
