export type PlatformType = "all" | "shorts" | "reels" | "tiktok";

export interface SubTopic {
  id: string;
  name: string;
  description: string;
  count: number;
}

export interface ViralVideo {
  id: string;
  title: string;
  platform: "shorts" | "reels" | "tiktok";
  subTopicId: string;
  views: number;
  viewsFormatted: string;
  likesFormatted: string;
  duration: string;
  author: string;
  authorHandle: string;
  thumbnail: string;
  videoUrl: string;
  viralScore: number;
  hookSummary: string;
  viralReason: string;
}

export interface TimelineItem {
  timestamp: string;
  stage: "초반 훅 (Hook)" | "문제 제기 (Problem)" | "반전/해결책 (Solution)" | "행동 유도 (CTA)";
  narration: string;
  visualDirection: string;
}

export interface CreatorActionPlan {
  reproducibleIdeas: {
    suggestedTitle: string;
    hookScript: string;
    keyPlot: string;
  }[];
  editingGuide: {
    recommendedBpm: string;
    captionPreset: string;
    transitionTechnique: string;
    soundEffectCues: string;
  };
  aiPromptSnippet: string;
}

export interface VideoDetailAnalysis {
  videoId: string;
  videoTitle: string;
  platform: "shorts" | "reels" | "tiktok";
  // ① 초반 3초 훅 대사 및 시각적 연출법
  hookAnalysis: {
    hookScript: string;
    visualAction: string;
    psychologicalTrigger: string;
  };
  // ② 해당 영상의 성공 요인 및 트렌드 특징
  successFactors: {
    title: string;
    description: string;
  }[];
  // ③ 컷 전환 속도 및 영상 편집 방식
  editingAnalysis: {
    cutSpeed: string;
    editingStyle: string;
    soundMood: string;
    captionStyle: string;
  };
  // ④ 전체 타임라인별 대사 (스크립트)
  timelineScript: TimelineItem[];
  // ⑤ [요구사항 5] 크리에이터의 고민을 종결짓는 AI 맞춤형 떡상 기획 & 편집 액션플랜
  actionPlan: CreatorActionPlan;
}

export interface SearchAnalysisResult {
  keyword: string;
  subTopics: SubTopic[];
  videos: ViralVideo[];
  totalSearched: number;
  insights: {
    avgViewCount: string;
    topPlatform: string;
    hookPattern: string;
  };
}
