import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "ViralScope AI - 숏폼 바이럴 분석 & 기획 대시보드 (Pre-production SaaS)",
  description:
    "유튜브 쇼츠, 인스타 릴스, 틱톡 떡상 영상을 해부하고 3초 훅, 컷 편집 속도, 타임라인 대본, AI 기획안을 도출하는 크리에이터 필수 SaaS",
  keywords: ["숏폼 기획", "쇼츠 떡상", "릴스 바이럴", "틱톡 알고리즘", "Gemini AI", "프리프로덕션"],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ko" className="dark">
      <head>
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css"
        />
      </head>
      <body className="antialiased selection:bg-primary-500 selection:text-white">
        {children}
      </body>
    </html>
  );
}
