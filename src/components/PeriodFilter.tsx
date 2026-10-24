"use client";

import React from "react";
import { Clock } from "lucide-react";
import { PeriodFilterType } from "@/types";

interface PeriodFilterProps {
  selectedPeriod: PeriodFilterType;
  onChange: (period: PeriodFilterType) => void;
}

const PERIOD_OPTIONS: { id: PeriodFilterType; label: string }[] = [
  { id: "1d", label: "오늘 (1일)" },
  { id: "1w", label: "최근 1주일" },
  { id: "1m", label: "최근 1개월" },
  { id: "3m", label: "최근 3개월" },
  { id: "6m", label: "최근 6개월" },
  { id: "1y", label: "최근 1년" },
  { id: "all_time", label: "역대 전체" },
];

export function PeriodFilter({ selectedPeriod, onChange }: PeriodFilterProps) {
  return (
    <div className="flex items-center gap-2 bg-surface/90 border border-surface-border p-1.5 rounded-2xl">
      <div className="flex items-center gap-1 px-2.5 text-xs text-gray-400 font-bold">
        <Clock className="w-3.5 h-3.5 text-primary-400" />
        <span>기간:</span>
      </div>
      <div className="flex items-center gap-1 overflow-x-auto">
        {PERIOD_OPTIONS.map((opt) => {
          const isActive = selectedPeriod === opt.id;
          return (
            <button
              key={opt.id}
              onClick={() => onChange(opt.id)}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all whitespace-nowrap ${
                isActive
                  ? "bg-gradient-to-r from-primary-600 to-primary-500 text-white shadow-md shadow-primary-600/30"
                  : "text-gray-400 hover:text-white hover:bg-white/5"
              }`}
            >
              {opt.label}
            </button>
          );
        })}
      </div>
    </div>
  );
}
