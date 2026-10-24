"use client";

import React, { useState } from "react";
import { VideoDetailAnalysis } from "@/types";
import { X, Copy, Check, Sparkles, Zap, Flame, Clock, Film, MessageSquare, Lightbulb } from "lucide-react";

interface AnalysisModalProps {
  analysis: VideoDetailAnalysis | null;
  isOpen: boolean;
  onClose: () => void;
  isLoading?: boolean;
}

type TabType = "hook" | "success" | "editing" | "timeline" | "action";

export function AnalysisModal({ analysis, isOpen, onClose, isLoading }: AnalysisModalProps) {
  const [activeTab, setActiveTab] = useState<TabType>("hook");
  const [copiedScript, setCopiedScript] = useState(false);
  const [copiedPrompt, setCopiedPrompt] = useState(false);

  if (!isOpen) return null;

  const handleCopyScript = () => {
    if (!analysis) return;
    const fullText = analysis.timelineScript
      .map((item) => `[${item.timestamp}] ${item.stage}\n대사: ${item.narration}\n연출: ${item.visualDirection}`)
      .join("\n\n");
    navigator.clipboard.writeText(fullText);
    setCopiedScript(true);
    setTimeout(() => setCopiedScript(false), 2000);
  };

  const handleCopyPrompt = () => {
    if (!analysis) return;
    navigator.clipboard.writeText(analysis.actionPlan.aiPromptSnippet);
    setCopiedPrompt(true);
    setTimeout(() => setCopiedPrompt(false), 2000);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md animate-fadeIn">
      <div className="relative w-full max-w-4xl max-h-[90vh] bg-surface border border-surface-border rounded-3xl shadow-2xl flex flex-col overflow-hidden">
        {/* Modal Header */}
        <div className="flex items-center justify-between p-6 border-b border-surface-border bg-surface-card">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-primary-600 to-accent-pink flex items-center justify-center shadow-lg shadow-primary-600/30">
              <Sparkles className="w-5 h-5 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs font-bold px-2 py-0.5 rounded-full bg-primary-500/20 text-primary-300 border border-primary-500/30">
                  Gemini AI Deep Dive
                </span>
                <span className="text-xs text-gray-400">숏폼 떡상 성공 공식 정밀 해부</span>
              </div>
              <h2 className="text-base md:text-lg font-bold text-white line-clamp-1 mt-0.5">
                {isLoading ? "영상 알고리즘 요인을 분석 중입니다..." : analysis?.videoTitle}
              </h2>
            </div>
          </div>
          <button
            onClick={onClose}
            className="w-9 h-9 rounded-xl bg-white/5 hover:bg-white/10 flex items-center justify-center text-gray-400 hover:text-white transition-all"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        {isLoading ? (
          <div className="flex-1 p-12 flex flex-col items-center justify-center text-center gap-4">
            <div className="w-16 h-16 rounded-full border-4 border-primary-500/20 border-t-primary-500 animate-spin" />
            <h3 className="text-base font-bold text-white">Gemini AI가 숏폼 성공 공식을 해부하고 있습니다...</h3>
            <p className="text-xs text-gray-400 max-w-sm">
              초반 3초 훅 대사, 시청 이탈 방지 연출법, 평균 컷 전환 템포, 타임라인별 대본을 생성 중입니다.
            </p>
          </div>
        ) : analysis ? (
          <div className="flex-1 flex flex-col overflow-hidden">
            {/* Tabs */}
            <div className="flex items-center gap-2 p-3 bg-background border-b border-surface-border overflow-x-auto">
              <button
                onClick={() => setActiveTab("hook")}
                className={`flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-bold transition-all whitespace-nowrap ${
                  activeTab === "hook"
                    ? "bg-primary-600 text-white shadow-md shadow-primary-600/30"
                    : "text-gray-400 hover:text-white hover:bg-white/5"
                }`}
              >
                <Zap className="w-3.5 h-3.5" />
                <span>① 초반 3초 훅 (Hook)</span>
              </button>

              <button
                onClick={() => setActiveTab("success")}
                className={`flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-bold transition-all whitespace-nowrap ${
                  activeTab === "success"
                    ? "bg-primary-600 text-white shadow-md shadow-primary-600/30"
                    : "text-gray-400 hover:text-white hover:bg-white/5"
                }`}
              >
                <Flame className="w-3.5 h-3.5" />
                <span>② 떡상 성공 요인 (조회수 비밀)</span>
              </button>

              <button
                onClick={() => setActiveTab("editing")}
                className={`flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-bold transition-all whitespace-nowrap ${
                  activeTab === "editing"
                    ? "bg-primary-600 text-white shadow-md shadow-primary-600/30"
                    : "text-gray-400 hover:text-white hover:bg-white/5"
                }`}
              >
                <Film className="w-3.5 h-3.5" />
                <span>③ 컷 편집 템포 & 스타일</span>
              </button>

              <button
                onClick={() => setActiveTab("timeline")}
                className={`flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-bold transition-all whitespace-nowrap ${
                  activeTab === "timeline"
                    ? "bg-primary-600 text-white shadow-md shadow-primary-600/30"
                    : "text-gray-400 hover:text-white hover:bg-white/5"
                }`}
              >
                <MessageSquare className="w-3.5 h-3.5" />
                <span>④ 타임라인 대본 스크립트</span>
              </button>

              <button
                onClick={() => setActiveTab("action")}
                className={`flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-bold transition-all whitespace-nowrap ${
                  activeTab === "action"
                    ? "bg-accent-pink text-white shadow-md shadow-accent-pink/30"
                    : "text-gray-400 hover:text-white hover:bg-white/5"
                }`}
              >
                <Lightbulb className="w-3.5 h-3.5" />
                <span>🚀 내 채널 떡상 기획안 3선</span>
              </button>
            </div>

            {/* Tab Contents */}
            <div className="flex-1 overflow-y-auto p-6 space-y-6">
              {/* Tab 1: Hook Analysis */}
              {activeTab === "hook" && (
                <div className="space-y-4">
                  <div className="p-5 rounded-2xl bg-surface-card border border-primary-500/30 shadow-lg">
                    <span className="text-xs font-bold text-primary-400 uppercase tracking-wider block mb-2">
                      🎙️ 초반 3초 실제 대사 (Hook Script)
                    </span>
                    <blockquote className="text-base md:text-lg font-bold text-white italic border-l-4 border-primary-500 pl-4 py-1">
                      {analysis.hookAnalysis.hookScript}
                    </blockquote>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="p-4 rounded-2xl bg-surface-card border border-surface-border">
                      <span className="text-xs font-bold text-accent-cyan block mb-1">
                        🎬 시각적 화면 연출 장치
                      </span>
                      <p className="text-xs text-gray-300 leading-relaxed">
                        {analysis.hookAnalysis.visualAction}
                      </p>
                    </div>

                    <div className="p-4 rounded-2xl bg-surface-card border border-surface-border">
                      <span className="text-xs font-bold text-amber-400 block mb-1">
                        🧠 시청자 심리 트리거 분석
                      </span>
                      <p className="text-xs text-gray-300 leading-relaxed">
                        {analysis.hookAnalysis.psychologicalTrigger}
                      </p>
                    </div>
                  </div>
                </div>
              )}

              {/* Tab 2: Why Viral & Success Factors */}
              {activeTab === "success" && (
                <div className="space-y-4">
                  <div className="text-xs font-bold text-gray-400">
                    💡 이 영상이 수백만 조회수를 돌파한 3대 핵심 알고리즘 트리거:
                  </div>
                  {analysis.successFactors.map((factor, idx) => (
                    <div
                      key={idx}
                      className="p-4 rounded-2xl bg-surface-card border border-surface-border flex items-start gap-3"
                    >
                      <div className="w-7 h-7 rounded-lg bg-primary-600/30 text-primary-300 flex items-center justify-center font-bold text-xs flex-shrink-0 mt-0.5">
                        #{idx + 1}
                      </div>
                      <div>
                        <h4 className="text-sm font-bold text-white mb-1">{factor.title}</h4>
                        <p className="text-xs text-gray-300 leading-relaxed">{factor.description}</p>
                      </div>
                    </div>
                  ))}
                </div>
              )}

              {/* Tab 3: Editing Analysis */}
              {activeTab === "editing" && (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="p-4 rounded-2xl bg-surface-card border border-surface-border">
                    <span className="text-xs font-bold text-primary-400 block mb-1">
                      ⚡ 평균 컷 전환 속도 (Pacing)
                    </span>
                    <p className="text-sm font-bold text-white">{analysis.editingAnalysis.cutSpeed}</p>
                  </div>

                  <div className="p-4 rounded-2xl bg-surface-card border border-surface-border">
                    <span className="text-xs font-bold text-accent-cyan block mb-1">
                      🎨 화면 구도 및 편집 스타일
                    </span>
                    <p className="text-sm font-bold text-white">{analysis.editingAnalysis.editingStyle}</p>
                  </div>

                  <div className="p-4 rounded-2xl bg-surface-card border border-surface-border">
                    <span className="text-xs font-bold text-pink-400 block mb-1">
                      🎵 배경음악(BGM) 템포 & 사운드 디자인
                    </span>
                    <p className="text-sm font-bold text-white">{analysis.editingAnalysis.soundMood}</p>
                  </div>

                  <div className="p-4 rounded-2xl bg-surface-card border border-surface-border">
                    <span className="text-xs font-bold text-amber-400 block mb-1">
                      🔤 자막 폰트 및 애니메이션 프리셋
                    </span>
                    <p className="text-sm font-bold text-white">{analysis.editingAnalysis.captionStyle}</p>
                  </div>
                </div>
              )}

              {/* Tab 4: Timeline Script */}
              {activeTab === "timeline" && (
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <span className="text-xs text-gray-400 font-bold">
                      전체 타임라인별 대본 스크립트 (총 4단계):
                    </span>
                    <button
                      onClick={handleCopyScript}
                      className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-primary-600 hover:bg-primary-500 text-xs font-bold text-white transition-all"
                    >
                      {copiedScript ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
                      <span>{copiedScript ? "복사 완료!" : "전체 대본 복사"}</span>
                    </button>
                  </div>

                  <div className="space-y-3">
                    {analysis.timelineScript.map((item, idx) => (
                      <div
                        key={idx}
                        className="p-4 rounded-2xl bg-surface-card border border-surface-border flex flex-col gap-2"
                      >
                        <div className="flex items-center justify-between text-xs">
                          <span className="font-extrabold text-primary-400">{item.timestamp}</span>
                          <span className="px-2 py-0.5 rounded-full bg-white/10 text-gray-300 font-bold text-[11px]">
                            {item.stage}
                          </span>
                        </div>
                        <div className="text-sm text-white font-medium bg-black/30 p-2.5 rounded-xl border border-white/5">
                          💬 {item.narration}
                        </div>
                        <div className="text-xs text-gray-400 flex items-center gap-1.5">
                          <span>🎬 연출:</span>
                          <span className="text-gray-300">{item.visualDirection}</span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Tab 5: Action Plan */}
              {activeTab === "action" && (
                <div className="space-y-6">
                  <div className="space-y-3">
                    <h4 className="text-xs font-bold text-accent-pink uppercase tracking-wider">
                      🔥 내 채널 즉시 적용 떡상 기획안 3선:
                    </h4>
                    {analysis.actionPlan.reproducibleIdeas.map((idea, idx) => (
                      <div
                        key={idx}
                        className="p-4 rounded-2xl bg-surface-card border border-surface-border flex flex-col gap-2"
                      >
                        <div className="flex items-center gap-2">
                          <span className="px-2 py-0.5 rounded bg-accent-pink/20 text-accent-pink font-bold text-xs">
                            추천 #{idx + 1}
                          </span>
                          <span className="text-sm font-bold text-white">{idea.suggestedTitle}</span>
                        </div>
                        <p className="text-xs text-gray-300 italic bg-white/5 p-2 rounded-lg">
                          훅: {idea.hookScript}
                        </p>
                        <p className="text-xs text-gray-400">플롯: {idea.keyPlot}</p>
                      </div>
                    ))}
                  </div>

                  {/* AI Prompt Snippet */}
                  <div className="p-4 rounded-2xl bg-black/40 border border-primary-500/30 flex flex-col gap-2">
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-bold text-primary-300">
                        ⚡ ChatGPT/Claude 원클릭 대본 생성 프롬프트:
                      </span>
                      <button
                        onClick={handleCopyPrompt}
                        className="flex items-center gap-1 px-2.5 py-1 rounded bg-white/10 hover:bg-white/20 text-[11px] font-bold text-white transition-all"
                      >
                        {copiedPrompt ? <Check className="w-3 h-3" /> : <Copy className="w-3 h-3" />}
                        <span>{copiedPrompt ? "복사됨!" : "프롬프트 복사"}</span>
                      </button>
                    </div>
                    <pre className="text-xs text-gray-300 whitespace-pre-wrap font-mono bg-white/5 p-3 rounded-xl overflow-x-auto">
                      {analysis.actionPlan.aiPromptSnippet}
                    </pre>
                  </div>
                </div>
              )}
            </div>
          </div>
        ) : null}
      </div>
    </div>
  );
}
