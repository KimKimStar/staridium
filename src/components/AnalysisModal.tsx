"use client";

import React, { useState } from "react";
import { VideoDetailAnalysis, ViralVideo } from "@/types";
import {
  X,
  Sparkles,
  Flame,
  Clock,
  Scissors,
  FileText,
  Lightbulb,
  Copy,
  Check,
  TrendingUp,
  BrainCircuit,
  Film,
  Music,
  Tv,
} from "lucide-react";

interface AnalysisModalProps {
  video: ViralVideo | null;
  analysis: VideoDetailAnalysis | null;
  isLoading: boolean;
  onClose: () => void;
}

export const AnalysisModal: React.FC<AnalysisModalProps> = ({
  video,
  analysis,
  isLoading,
  onClose,
}) => {
  const [activeTab, setActiveTab] = useState<"action" | "hook" | "editing" | "script">("action");
  const [copiedKey, setCopiedKey] = useState<string | null>(null);

  if (!video) return null;

  const handleCopy = (text: string, key: string) => {
    navigator.clipboard.writeText(text);
    setCopiedKey(key);
    setTimeout(() => setCopiedKey(null), 2000);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/80 backdrop-blur-md overflow-y-auto">
      <div className="relative w-full max-w-4xl max-h-[92vh] flex flex-col rounded-3xl bg-surface border border-surface-border shadow-2xl shadow-primary-500/20 overflow-hidden my-auto">
        {/* Top Header Bar */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-surface-border bg-surface/90">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-primary-600 to-accent-pink flex items-center justify-center text-white shadow-md">
              <BrainCircuit className="w-5 h-5 animate-pulse" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs font-bold text-accent-cyan tracking-wider uppercase">
                  Gemini Deep Viral Anatomy
                </span>
                <span className="text-[10px] px-2 py-0.5 rounded-full bg-accent-amber/20 text-accent-amber font-semibold border border-accent-amber/30">
                  바이럴 스코어 {video.viralScore}점
                </span>
              </div>
              <h2 className="text-sm sm:text-base font-bold text-white line-clamp-1 max-w-xl">
                {video.title}
              </h2>
            </div>
          </div>

          <button
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white flex items-center justify-center transition-all"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Modal Navigation Tabs */}
        <div className="flex items-center gap-2 px-6 pt-3 border-b border-surface-border bg-surface/50 overflow-x-auto scrollbar-none">
          <button
            onClick={() => setActiveTab("action")}
            className={`flex items-center gap-2 px-4 py-2.5 text-xs sm:text-sm font-bold border-b-2 transition-all whitespace-nowrap ${
              activeTab === "action"
                ? "border-accent-pink text-white"
                : "border-transparent text-gray-400 hover:text-gray-200"
            }`}
          >
            <Lightbulb className="w-4 h-4 text-accent-pink" />
            <span>🚀 내 채널 즉시 적용 (떡상 기획안)</span>
          </button>

          <button
            onClick={() => setActiveTab("hook")}
            className={`flex items-center gap-2 px-4 py-2.5 text-xs sm:text-sm font-semibold border-b-2 transition-all whitespace-nowrap ${
              activeTab === "hook"
                ? "border-primary-500 text-white"
                : "border-transparent text-gray-400 hover:text-gray-200"
            }`}
          >
            <Sparkles className="w-4 h-4 text-primary-400" />
            <span>① 3초 훅 & 성공 요인</span>
          </button>

          <button
            onClick={() => setActiveTab("editing")}
            className={`flex items-center gap-2 px-4 py-2.5 text-xs sm:text-sm font-semibold border-b-2 transition-all whitespace-nowrap ${
              activeTab === "editing"
                ? "border-accent-cyan text-white"
                : "border-transparent text-gray-400 hover:text-gray-200"
            }`}
          >
            <Scissors className="w-4 h-4 text-accent-cyan" />
            <span>② 컷 전환 & 편집 방식</span>
          </button>

          <button
            onClick={() => setActiveTab("script")}
            className={`flex items-center gap-2 px-4 py-2.5 text-xs sm:text-sm font-semibold border-b-2 transition-all whitespace-nowrap ${
              activeTab === "script"
                ? "border-accent-amber text-white"
                : "border-transparent text-gray-400 hover:text-gray-200"
            }`}
          >
            <FileText className="w-4 h-4 text-accent-amber" />
            <span>③ 타임라인별 대사 스크립트</span>
          </button>
        </div>

        {/* Modal Content Body */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6">
          {isLoading ? (
            <div className="py-20 text-center space-y-4">
              <div className="w-12 h-12 rounded-full border-2 border-primary-500 border-t-transparent animate-spin mx-auto" />
              <p className="text-sm font-medium text-gray-300">
                Gemini AI가 영상의 프레임과 대본, 편집 리듬을 심층 분석 중입니다...
              </p>
            </div>
          ) : !analysis ? (
            <div className="text-center py-12 text-gray-400 text-sm">
              분석 데이터를 불러오지 못했습니다.
            </div>
          ) : (
            <>
              {/* TAB 1: 내 채널 즉시 적용 (요구사항 5번 핵심 고민 해결) */}
              {activeTab === "action" && (
                <div className="space-y-6">
                  {/* Banner */}
                  <div className="p-4 rounded-2xl bg-gradient-to-r from-accent-pink/15 via-primary-600/15 to-accent-cyan/15 border border-accent-pink/30">
                    <h3 className="text-base font-bold text-white flex items-center gap-2 mb-1">
                      <Flame className="w-4 h-4 text-accent-pink" />
                      크리에이터 고민 해결 솔루션: "어떤 영상을, 어떻게 만들 것인가?"
                    </h3>
                    <p className="text-xs text-gray-300 leading-relaxed">
                      이 영상이 조회수 <strong>{video.viewsFormatted}</strong>를 기록한 알고리즘 승리 공식을 분해하여, 당신의 채널에서 당장 제작할 수 있는 기획안 3가지와 편집 가이드를 설계했습니다.
                    </p>
                  </div>

                  {/* 3가지 신규 숏폼 기획 아이디어 */}
                  <div className="space-y-3">
                    <h4 className="text-sm font-bold text-white flex items-center gap-2">
                      <Lightbulb className="w-4 h-4 text-accent-amber" />
                      바로 촬영 가능한 복제 기획안 3선
                    </h4>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                      {analysis.actionPlan.reproducibleIdeas.map((idea, idx) => (
                        <div
                          key={idx}
                          className="p-4 rounded-2xl bg-surface-card border border-surface-border hover:border-accent-pink/40 transition-all flex flex-col justify-between"
                        >
                          <div>
                            <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-accent-pink/20 text-accent-pink mb-2 inline-block">
                              기획안 #{idx + 1}
                            </span>
                            <h5 className="font-bold text-sm text-white mb-2 leading-snug">
                              {idea.suggestedTitle}
                            </h5>
                            <div className="p-2.5 rounded-lg bg-black/40 border border-white/5 text-xs text-accent-amber mb-2 italic">
                              "{idea.hookScript}"
                            </div>
                            <p className="text-xs text-gray-400 leading-relaxed">
                              {idea.keyPlot}
                            </p>
                          </div>
                          <button
                            onClick={() =>
                              handleCopy(
                                `제목: ${idea.suggestedTitle}\n훅 대사: ${idea.hookScript}\n전개: ${idea.keyPlot}`,
                                `idea-${idx}`
                              )
                            }
                            className="mt-4 w-full py-1.5 px-3 rounded-lg bg-white/5 hover:bg-white/10 text-xs text-gray-300 hover:text-white font-medium flex items-center justify-center gap-1.5 transition-all"
                          >
                            {copiedKey === `idea-${idx}` ? (
                              <>
                                <Check className="w-3.5 h-3.5 text-emerald-400" />
                                <span>복사 완료!</span>
                              </>
                            ) : (
                              <>
                                <Copy className="w-3.5 h-3.5" />
                                <span>이 기획안 복사</span>
                              </>
                            )}
                          </button>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* 컷 편집 실전 가이드 */}
                  <div className="p-4 rounded-2xl bg-surface-card border border-surface-border space-y-3">
                    <h4 className="text-sm font-bold text-white flex items-center gap-2">
                      <Scissors className="w-4 h-4 text-accent-cyan" />
                      영상 편집 디렉팅 가이드라인
                    </h4>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                      <div className="p-3 rounded-xl bg-black/30 border border-white/5">
                        <span className="text-gray-400 block mb-1">🎵 추천 비트 및 음악 템포:</span>
                        <span className="text-white font-semibold">
                          {analysis.actionPlan.editingGuide.recommendedBpm}
                        </span>
                      </div>
                      <div className="p-3 rounded-xl bg-black/30 border border-white/5">
                        <span className="text-gray-400 block mb-1">🔤 자막 폰트 및 컬러 프리셋:</span>
                        <span className="text-white font-semibold">
                          {analysis.actionPlan.editingGuide.captionPreset}
                        </span>
                      </div>
                      <div className="p-3 rounded-xl bg-black/30 border border-white/5">
                        <span className="text-gray-400 block mb-1">⚡ 트랜지션 및 화면 전환:</span>
                        <span className="text-white font-semibold">
                          {analysis.actionPlan.editingGuide.transitionTechnique}
                        </span>
                      </div>
                      <div className="p-3 rounded-xl bg-black/30 border border-white/5">
                        <span className="text-gray-400 block mb-1">🔊 사운드 이펙트(SFX) 타이밍:</span>
                        <span className="text-white font-semibold">
                          {analysis.actionPlan.editingGuide.soundEffectCues}
                        </span>
                      </div>
                    </div>
                  </div>

                  {/* AI 대본 생성 프롬프트 복사 */}
                  <div className="p-4 rounded-2xl bg-gradient-to-br from-primary-950/70 to-surface border border-primary-500/30">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-xs font-bold text-primary-300 flex items-center gap-1.5">
                        <Sparkles className="w-3.5 h-3.5" />
                        ChatGPT / Claude / Gemini 대본 제작 프롬프트
                      </span>
                      <button
                        onClick={() => handleCopy(analysis.actionPlan.aiPromptSnippet, "prompt")}
                        className="flex items-center gap-1 px-3 py-1 rounded-lg bg-primary-600 hover:bg-primary-500 text-xs font-semibold text-white transition-all shadow-md shadow-primary-600/30"
                      >
                        {copiedKey === "prompt" ? (
                          <>
                            <Check className="w-3 h-3 text-emerald-300" />
                            <span>복사됨!</span>
                          </>
                        ) : (
                          <>
                            <Copy className="w-3 h-3" />
                            <span>프롬프트 복사</span>
                          </>
                        )}
                      </button>
                    </div>
                    <pre className="p-3 rounded-xl bg-black/60 border border-white/5 text-[11px] text-gray-300 font-mono whitespace-pre-wrap leading-relaxed max-h-36 overflow-y-auto">
                      {analysis.actionPlan.aiPromptSnippet}
                    </pre>
                  </div>
                </div>
              )}

              {/* TAB 2: 3초 훅 & 성공 요인 */}
              {activeTab === "hook" && (
                <div className="space-y-6">
                  {/* Hook Analysis Box */}
                  <div className="p-5 rounded-2xl bg-gradient-to-br from-accent-amber/10 via-surface-card to-surface-card border border-accent-amber/30 space-y-4">
                    <div className="flex items-center gap-2">
                      <div className="w-7 h-7 rounded-lg bg-accent-amber/20 flex items-center justify-center text-accent-amber">
                        <Sparkles className="w-4 h-4" />
                      </div>
                      <h4 className="text-sm font-bold text-white">
                        초반 3초 훅(Hook) 대사 & 시각 연출 해부
                      </h4>
                    </div>

                    <div className="p-4 rounded-xl bg-black/40 border border-white/10 space-y-2">
                      <div className="text-xs text-gray-400 font-semibold">📢 실제 3초 훅 오디오 대사:</div>
                      <div className="text-base sm:text-lg font-extrabold text-accent-amber italic">
                        "{analysis.hookAnalysis.hookScript}"
                      </div>
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                      <div className="p-3 rounded-xl bg-surface/80 border border-surface-border">
                        <span className="text-gray-400 block font-medium mb-1">🎬 화면 시각적 연출:</span>
                        <span className="text-gray-200 leading-relaxed">
                          {analysis.hookAnalysis.visualAction}
                        </span>
                      </div>
                      <div className="p-3 rounded-xl bg-surface/80 border border-surface-border">
                        <span className="text-gray-400 block font-medium mb-1">🧠 시청자 심리 자극 기제:</span>
                        <span className="text-gray-200 leading-relaxed">
                          {analysis.hookAnalysis.psychologicalTrigger}
                        </span>
                      </div>
                    </div>
                  </div>

                  {/* Success Factors */}
                  <div className="space-y-3">
                    <h4 className="text-sm font-bold text-white flex items-center gap-2">
                      <TrendingUp className="w-4 h-4 text-emerald-400" />
                      알고리즘 떡상 요인 및 트렌드 특징
                    </h4>
                    <div className="space-y-2.5">
                      {analysis.successFactors.map((factor, idx) => (
                        <div
                          key={idx}
                          className="p-3.5 rounded-xl bg-surface-card border border-surface-border flex items-start gap-3"
                        >
                          <span className="w-5 h-5 rounded-full bg-emerald-500/20 text-emerald-400 text-xs font-bold flex items-center justify-center flex-shrink-0 mt-0.5">
                            {idx + 1}
                          </span>
                          <div>
                            <div className="text-sm font-bold text-white mb-0.5">
                              {factor.title}
                            </div>
                            <div className="text-xs text-gray-400 leading-relaxed">
                              {factor.description}
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              )}

              {/* TAB 3: 컷 전환 & 편집 방식 */}
              {activeTab === "editing" && (
                <div className="space-y-6">
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div className="p-4 rounded-2xl bg-surface-card border border-surface-border space-y-2">
                      <div className="flex items-center gap-2 text-accent-cyan text-sm font-bold">
                        <Clock className="w-4 h-4" />
                        <span>컷 전환 속도 (Pacing)</span>
                      </div>
                      <p className="text-base font-bold text-white">
                        {analysis.editingAnalysis.cutSpeed}
                      </p>
                      <p className="text-xs text-gray-400">
                        시청자가 이탈할 틈을 주지 않는 초고속 도파민 템포
                      </p>
                    </div>

                    <div className="p-4 rounded-2xl bg-surface-card border border-surface-border space-y-2">
                      <div className="flex items-center gap-2 text-accent-pink text-sm font-bold">
                        <Film className="w-4 h-4" />
                        <span>영상 편집 스타일</span>
                      </div>
                      <p className="text-xs sm:text-sm font-medium text-gray-200 leading-relaxed">
                        {analysis.editingAnalysis.editingStyle}
                      </p>
                    </div>

                    <div className="p-4 rounded-2xl bg-surface-card border border-surface-border space-y-2">
                      <div className="flex items-center gap-2 text-accent-amber text-sm font-bold">
                        <Music className="w-4 h-4" />
                        <span>사운드 & BGM 무드</span>
                      </div>
                      <p className="text-xs sm:text-sm font-medium text-gray-200 leading-relaxed">
                        {analysis.editingAnalysis.soundMood}
                      </p>
                    </div>

                    <div className="p-4 rounded-2xl bg-surface-card border border-surface-border space-y-2">
                      <div className="flex items-center gap-2 text-primary-400 text-sm font-bold">
                        <Tv className="w-4 h-4" />
                        <span>자막(Caption) 스타일</span>
                      </div>
                      <p className="text-xs sm:text-sm font-medium text-gray-200 leading-relaxed">
                        {analysis.editingAnalysis.captionStyle}
                      </p>
                    </div>
                  </div>
                </div>
              )}

              {/* TAB 4: 타임라인별 대사 스크립트 */}
              {activeTab === "script" && (
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <span className="text-xs text-gray-400">
                      영상 시작부터 끝까지의 기승전결 타임라인 대본입니다.
                    </span>
                    <button
                      onClick={() => {
                        const fullScript = analysis.timelineScript
                          .map((t) => `[${t.timestamp}] (${t.stage})\n대사: ${t.narration}\n연출: ${t.visualDirection}`)
                          .join("\n\n");
                        handleCopy(fullScript, "full-script");
                      }}
                      className="flex items-center gap-1.5 px-3 py-1 rounded-lg bg-surface border border-surface-border text-xs text-gray-300 hover:text-white font-medium"
                    >
                      {copiedKey === "full-script" ? (
                        <>
                          <Check className="w-3.5 h-3.5 text-emerald-400" />
                          <span>전체 대본 복사됨!</span>
                        </>
                      ) : (
                        <>
                          <Copy className="w-3.5 h-3.5" />
                          <span>전체 대본 복사</span>
                        </>
                      )}
                    </button>
                  </div>

                  <div className="space-y-3">
                    {analysis.timelineScript.map((item, idx) => (
                      <div
                        key={idx}
                        className="p-4 rounded-2xl bg-surface-card border border-surface-border space-y-2 relative"
                      >
                        <div className="flex items-center justify-between">
                          <span className="text-xs font-mono font-bold text-accent-cyan px-2 py-0.5 rounded bg-cyan-500/10 border border-cyan-500/20">
                            {item.timestamp}
                          </span>
                          <span className="text-xs font-semibold px-2 py-0.5 rounded bg-primary-500/10 text-primary-300">
                            {item.stage}
                          </span>
                        </div>

                        <div className="text-sm font-medium text-white leading-relaxed">
                          {item.narration}
                        </div>

                        <div className="text-xs text-gray-400 flex items-start gap-1.5 pt-1 border-t border-white/5">
                          <span className="text-primary-400 font-semibold">🎬 연출 가이드:</span>
                          <span>{item.visualDirection}</span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </>
          )}
        </div>

        {/* Modal Footer */}
        <div className="px-6 py-3.5 bg-surface/90 border-t border-surface-border flex items-center justify-between text-xs text-gray-400">
          <span>💡 팁: 마음에 드는 기획안은 복사하여 나만의 숏폼 대본으로 커스텀하세요.</span>
          <button
            onClick={onClose}
            className="px-4 py-2 rounded-xl bg-surface hover:bg-white/10 text-white font-medium border border-surface-border transition-all"
          >
            닫기
          </button>
        </div>
      </div>
    </div>
  );
};
