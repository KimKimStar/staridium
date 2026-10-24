-- ==============================================================================
-- ViralScope AI: Supabase (PostgreSQL) Production Schema
-- ==============================================================================

-- 1. Enable UUID Extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. User Profiles & Credits Table
CREATE TABLE IF NOT EXISTS public.profiles (
  id UUID REFERENCES auth.users(id) ON DELETE CASCADE PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  credits INTEGER DEFAULT 3 CHECK (credits >= 0),
  subscription_status TEXT DEFAULT 'free' CHECK (subscription_status IN ('free', 'pro', 'canceled')),
  stripe_customer_id TEXT,
  stripe_subscription_id TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Viral Videos Master Table (유튜브 쇼츠, 인스타 릴스, 틱톡 수집 데이터)
CREATE TABLE IF NOT EXISTS public.videos (
  id TEXT PRIMARY KEY,                       -- e.g. 'yt-kJQP7kiw5Fk' or platform ID
  platform TEXT NOT NULL CHECK (platform IN ('shorts', 'reels', 'tiktok')),
  title TEXT NOT NULL,
  video_url TEXT NOT NULL UNIQUE,
  thumbnail_url TEXT NOT NULL,
  view_count BIGINT NOT NULL DEFAULT 0,
  like_count BIGINT DEFAULT 0,
  comment_count BIGINT DEFAULT 0,
  duration_seconds INTEGER DEFAULT 45,
  channel_title TEXT NOT NULL,
  channel_handle TEXT,
  upload_date TIMESTAMPTZ NOT NULL,
  main_keyword TEXT NOT NULL,                -- e.g. '다이어트', '재테크', '인간관계'
  sub_category TEXT NOT NULL,                -- e.g. '식단', '홈트레이닝'
  viral_score INTEGER DEFAULT 95,            -- 0-100 Viral Momentum Score
  hook_summary TEXT,                         -- 초반 3초 훅 요약
  viral_reason TEXT,                         -- 알고리즘 바이럴 원인 태그
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. AI Deep Dive Analyses Table (Gemini API 4가지 필수 심층 해부 분석)
CREATE TABLE IF NOT EXISTS public.video_analyses (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  video_id TEXT REFERENCES public.videos(id) ON DELETE CASCADE UNIQUE,
  hook_text TEXT NOT NULL,                    -- 1) 초반 3초 훅(Hook) 텍스트 및 대사
  hook_visual_action TEXT,                    -- 초반 3초 시각적 연출법
  hook_psychology TEXT,                       -- 시청자 심리 트리거 (손실 회피, 도파민 등)
  success_factors JSONB NOT NULL,             -- 2) 핵심 성공 요인 및 트렌드 특징 (왜 조회수가 많은지!)
  editing_tempo TEXT NOT NULL,                -- 3) 컷 전환 템포 (평균 0.85초 등)
  editing_style JSONB NOT NULL,               -- 시각적 편집 스타일, BGM, 자막 프리셋
  timeline_script JSONB NOT NULL,             -- 4) 전체 영상 타임라인별 대본(스크립트)
  creator_action_plan JSONB NOT NULL,         -- 내 채널 적용 떡상 기획안 3선 & 프롬프트
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Credit Transactions Audit Table
CREATE TABLE IF NOT EXISTS public.credit_transactions (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
  amount INTEGER NOT NULL,                   -- e.g. -1 for analysis, +10 for purchase
  balance_after INTEGER NOT NULL,
  reason TEXT NOT NULL,                      -- e.g. 'DEEP_DIVE_ANALYSIS', 'STRIPE_PRO_UPGRADE'
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 6. Indexes for Blazing Fast Queries by Period and View Count
CREATE INDEX IF NOT EXISTS idx_videos_main_keyword ON public.videos(main_keyword);
CREATE INDEX IF NOT EXISTS idx_videos_sub_category ON public.videos(sub_category);
CREATE INDEX IF NOT EXISTS idx_videos_platform ON public.videos(platform);
CREATE INDEX IF NOT EXISTS idx_videos_upload_date ON public.videos(upload_date DESC);
CREATE INDEX IF NOT EXISTS idx_videos_views ON public.videos(view_count DESC);
CREATE INDEX IF NOT EXISTS idx_videos_composite ON public.videos(main_keyword, upload_date DESC, view_count DESC);

-- 7. Trigger: Auto-create Profile on Supabase User Signup (3 Free Credits)
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.profiles (id, email, credits, subscription_status)
  VALUES (new.id, new.email, 3, 'free');
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE PROCEDURE public.handle_new_user();

-- 8. Row Level Security (RLS)
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.videos ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.video_analyses ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own profile" ON public.profiles FOR SELECT USING (auth.uid() = id);
CREATE POLICY "Public can view videos" ON public.videos FOR SELECT TO authenticated, anon USING (true);
CREATE POLICY "Public can view analyses" ON public.video_analyses FOR SELECT TO authenticated, anon USING (true);
