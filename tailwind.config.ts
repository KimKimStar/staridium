import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: ["class"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Pretendard", "-apple-system", "BlinkMacSystemFont", "system-ui", "Roboto", "sans-serif"],
      },
      colors: {
        background: "#020617", // slate-950
        surface: "#0f172a", // slate-900
        "surface-card": "#1e293b", // slate-800
        "surface-border": "#334155", // slate-700
        primary: {
          50: "#eff6ff",
          100: "#dbeafe",
          400: "#60a5fa",
          500: "#3b82f6", // neon blue
          600: "#2563eb",
          700: "#1d4ed8",
        },
        violet: {
          400: "#a78bfa",
          500: "#8b5cf6", // neon violet
          600: "#7c3aed",
          700: "#6d28d9",
        },
        accent: {
          blue: "#3b82f6",
          violet: "#8b5cf6",
          pink: "#ec4899",
          cyan: "#06b6d4",
          emerald: "#10b981",
          amber: "#f59e0b",
        },
      },
      borderRadius: {
        lg: "0.75rem",
        md: "0.5rem",
        sm: "0.375rem",
      },
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "hero-glow": "radial-gradient(circle at 50% 0%, rgba(59, 130, 246, 0.15) 0%, rgba(139, 92, 246, 0.08) 35%, transparent 70%)",
        "card-shimmer": "linear-gradient(90deg, rgba(30, 41, 59, 0) 0%, rgba(51, 65, 85, 0.5) 50%, rgba(30, 41, 59, 0) 100%)",
      },
      animation: {
        "pulse-slow": "pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite",
        "shimmer": "shimmer 2s infinite linear",
      },
      keyframes: {
        shimmer: {
          "0%": { transform: "translateX(-100%)" },
          "100%": { transform: "translateX(100%)" },
        },
      },
    },
  },
  plugins: [],
};
export default config;
