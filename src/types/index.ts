export type PlatformType = "all" | "shorts" | "reels" | "tiktok";

export type PeriodFilterType = "1d" | "1w" | "1m" | "3m" | "6m" | "1y" | "all_time";

export interface SubTopic {
  id: string;
  name: string;
  description?: string;
  count?: number;
}

export interface ViralVideo {
  id: string;
  title: string;
  platform: "shorts" | "reels" | "tiktok";
  videoUrl: string;
  thumbnail: string;
  views: number;
  viewsFormatted: string;
  likesFormatted: string;
  duration: string;
  author: string;
  uploadDate: string;
  mainKeyword: string;
  subCategory: string;
  subTopicId: string;
  viralScore: number;
  hookSummary: string;
  viralReason: string;
  rank?: number;
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

// [핵심 요구사항 3] Gemini API 4대 심층 분석 데이터 구조
export interface VideoDetailAnalysis {
  videoId: string;
  videoTitle: string;
  platform: "shorts" | "reels" | "tiktok";
  // ① 초반 3초 훅(Hook) 텍스트 및 대사 추출
  hookAnalysis: {
    hookScript: string;
    visualAction: string;
    psychologicalTrigger: string;
  };
  // ② 해당 영상의 핵심 성공 요인 및 트렌드 특징 (조회수가 폭발한 진짜 이유!)
  successFactors: {
    title: string;
    description: string;
  }[];
  // ③ 컷 전환 템포 및 시각적 편집 스타일 분석
  editingAnalysis: {
    cutSpeed: string;
    editingStyle: string;
    soundMood: string;
    captionStyle: string;
  };
  // ④ 전체 영상의 타임라인별 대본 (스크립트)
  timelineScript: TimelineItem[];
  // ⑤ 크리에이터를 위한 맞춤형 떡상 기획안 3선
  actionPlan: CreatorActionPlan;
}

export interface SearchAnalysisResult {
  keyword: string;
  subTopics: SubTopic[];
  videos: ViralVideo[];
}

export interface UserProfile {
  id: string;
  email: string;
  credits: number;
  subscriptionStatus: "free" | "pro" | "canceled";
}
