"use client";

import React, { useState, useEffect, useMemo } from "react";
import { Header } from "@/components/Header";
import { SearchBar } from "@/components/SearchBar";
import { SubTopicTabs } from "@/components/SubTopicTabs";
import { VideoList } from "@/components/VideoList";
import { SkeletonLoader } from "@/components/SkeletonLoader";
import { AnalysisModal } from "@/components/AnalysisModal";
import { PricingModal } from "@/components/PricingModal";
import {
  PlatformType,
  SearchAnalysisResult,
  VideoDetailAnalysis,
  ViralVideo,
} from "@/types";
import { Sparkles, Trophy, HelpCircle, Layers } from "lucide-react";

export default function HomePage() {
  // 1. 크레딧 및 Pro 구독 상태 관리
  const [credits, setCredits] = useState<number>(3);
  const [isPro, setIsPro] = useState<boolean>(false);
  const [isPricingOpen, setIsPricingOpen] = useState<boolean>(false);

  // 2. 검색 및 데이터 상태 관리
  const [keyword, setKeyword] = useState<string>("");
  const [analysisResult, setAnalysisResult] = useState<SearchAnalysisResult | null>(null);
  const [activeSubTopic, setActiveSubTopic] = useState<string>("all");
  const [platformFilter, setPlatformFilter] = useState<PlatformType>("all");
  const [sortBy, setSortBy] = useState<"views" | "score">("views");

  // 3. 로딩 상태
  const [isSearching, setIsSearching] = useState<boolean>(false);
  const [selectedVideo, setSelectedVideo] = useState<ViralVideo | null>(null);
  const [detailAnalysis, setDetailAnalysis] = useState<VideoDetailAnalysis | null>(null);
  const [isAnalyzingDetail, setIsAnalyzingDetail] = useState<boolean>(false);

  // 초기 로드: 로컬스토리지에서 크레딧 & 결제 파라미터 확인
  useEffect(() => {
    // URL 결제 성공 체크
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

  // 크레딧 상태 업데이트 헬퍼
  const deductCredit = () => {
    if (isPro) return true;
    if (credits <= 0) {
      setIsPricingOpen(true);
      return false;
    }
    const newCredit = credits - 1;
    setCredits(newCredit);
    localStorage.setItem("viralscope_credits", newCredit.toString());
    return true;
  };

  // 키워드 검색 핸들러
  const handleSearch = async (kw: string) => {
    if (!isPro && credits <= 0) {
      setIsPricingOpen(true);
      return;
    }

    if (!deductCredit()) return;

    setKeyword(kw);
    setIsSearching(true);
    setActiveSubTopic("all");
    setPlatformFilter("all");

    try {
      const res = await fetch("/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ keyword: kw }),
      });

      if (!res.ok) {
        throw new Error("분석 실패");
      }

      const data: SearchAnalysisResult = await res.json();
      setAnalysisResult(data);
    } catch (err) {
      console.error("검색 에러:", err);
      alert("데이터 분석 중 문제가 발생했습니다. 잠시 후 다시 시도해주세요.");
    } finally {
      setIsSearching(false);
    }
  };

  // 영상 카드 클릭 시 상세 해부 모달 호출
  const handleSelectVideo = async (video: ViralVideo) => {
    setSelectedVideo(video);
    setIsAnalyzingDetail(true);
    setDetailAnalysis(null);

    try {
      const res = await fetch("/api/video-detail", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ video }),
      });

      if (!res.ok) throw new Error("상세 분석 실패");

      const data: VideoDetailAnalysis = await res.json();
      setDetailAnalysis(data);
    } catch (err) {
      console.error("상세 분석 에러:", err);
    } finally {
      setIsAnalyzingDetail(false);
    }
  };

  // 결제 완료 콜백
  const handlePaymentSuccess = () => {
    setIsPro(true);
    localStorage.setItem("viralscope_is_pro", "true");
  };

  // 필터링 및 정렬된 비디오 목록 계산
  const filteredVideos = useMemo(() => {
    if (!analysisResult) return [];

    let list = [...analysisResult.videos];

    // 1. 하위 주제 탭 필터링
    if (activeSubTopic !== "all") {
      list = list.filter((v) => v.subTopicId === activeSubTopic);
    }

    // 2. 플랫폼 필터링
    if (platformFilter !== "all") {
      list = list.filter((v) => v.platform === platformFilter);
    }

    // 3. 정렬 (조회수 순 vs 바이럴 스코어 순)
    if (sortBy === "views") {
      list.sort((a, b) => b.views - a.views);
    } else {
      list.sort((a, b) => b.viralScore - a.viralScore);
    }

    return list;
  }, [analysisResult, activeSubTopic, platformFilter, sortBy]);

  return (
    <div className="min-h-screen flex flex-col bg-background text-gray-100 relative selection:bg-primary-500 selection:text-white">
      {/* Background Decorative Ambient Glow */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-7xl h-96 bg-hero-glow pointer-events-none" />

      {/* 1. Global Navigation Header */}
      <Header
        credits={credits}
        isPro={isPro}
        onOpenPricing={() => setIsPricingOpen(true)}
      />

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 pb-16 z-10">
        {/* 2. Hero & Search Bar */}
        <SearchBar onSearch={handleSearch} isLoading={isSearching} />

        {/* 3. Skeleton Loading State */}
        {isSearching && <SkeletonLoader />}

        {/* 4. Results Section */}
        {!isSearching && analysisResult && (
          <div className="space-y-6 animate-fadeIn">
            {/* SubTopics Tabs & Filters */}
            <SubTopicTabs
              keyword={analysisResult.keyword}
              subTopics={analysisResult.subTopics}
              activeSubTopic={activeSubTopic}
              onSelectSubTopic={setActiveSubTopic}
              platformFilter={platformFilter}
              onSelectPlatform={setPlatformFilter}
              sortBy={sortBy}
              onSelectSort={setSortBy}
              insights={analysisResult.insights}
            />

            {/* Video Cards Grid */}
            <VideoList
              videos={filteredVideos}
              onSelectVideo={handleSelectVideo}
            />
          </div>
        )}

        {/* 5. Initial Empty/Welcome State */}
        {!isSearching && !analysisResult && (
          <div className="mt-12 max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="p-6 rounded-2xl bg-surface/70 border border-surface-border space-y-3">
              <div className="w-10 h-10 rounded-xl bg-primary-500/20 text-primary-400 flex items-center justify-center font-bold">
                01
              </div>
              <h3 className="font-bold text-white text-base">
                전 플랫폼 떡상 영상 크롤링
              </h3>
              <p className="text-xs text-gray-400 leading-relaxed">
                쇼츠, 릴스, 틱톡에서 폭발적인 조회수를 기록한 최신 레퍼런스를 조회수 순으로 한눈에 파악합니다.
              </p>
            </div>

            <div className="p-6 rounded-2xl bg-surface/70 border border-surface-border space-y-3">
              <div className="w-10 h-10 rounded-xl bg-accent-pink/20 text-accent-pink flex items-center justify-center font-bold">
                02
              </div>
              <h3 className="font-bold text-white text-base">
                초반 3초 훅 & 컷 편집 해부
              </h3>
              <p className="text-xs text-gray-400 leading-relaxed">
                왜 시청자가 스크롤을 멈췄는지 첫마디 대사, 시각 연출, 평균 컷 전환 속도까지 Gemini AI가 정밀 분석합니다.
              </p>
            </div>

            <div className="p-6 rounded-2xl bg-surface/70 border border-surface-border space-y-3">
              <div className="w-10 h-10 rounded-xl bg-accent-cyan/20 text-accent-cyan flex items-center justify-center font-bold">
                03
              </div>
              <h3 className="font-bold text-white text-base">
                내 채널 복제 기획안 & 프롬프트
              </h3>
              <p className="text-xs text-gray-400 leading-relaxed">
                고민 끝! 떡상 공식을 그대로 적용한 3가지 신규 기획안과 즉시 복사 가능한 숏폼 대본 프롬프트를 받으세요.
              </p>
            </div>
          </div>
        )}
      </main>

      {/* 6. Deep Analysis Modal */}
      <AnalysisModal
        video={selectedVideo}
        analysis={detailAnalysis}
        isLoading={isAnalyzingDetail}
        onClose={() => setSelectedVideo(null)}
      />

      {/* 7. Stripe Pricing Modal */}
      <PricingModal
        isOpen={isPricingOpen}
        onClose={() => setIsPricingOpen(false)}
        onPaymentSuccess={handlePaymentSuccess}
      />

      {/* Footer */}
      <footer className="w-full border-t border-surface-border py-6 bg-surface/40 text-center text-xs text-gray-500">
        <p>© 2026 ViralScope AI. Built for next-generation short-form creators & marketers.</p>
      </footer>
    </div>
  );
}
