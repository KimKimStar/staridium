# -*- coding: utf-8 -*-
import os
import shutil

root_dir = r'c:\Users\kwang\OneDrive\Desktop\제미나이 바이블코딩'
dir_1 = os.path.join(root_dir, '1_자동매매_시스템')
dir_2 = os.path.join(root_dir, '2_쇼츠생성기_ShortsClone')
dir_3 = os.path.join(root_dir, '3_바이럴분석_SaaS_ViralScope')
scripts_dir = os.path.join(dir_3, 'scripts')

os.makedirs(scripts_dir, exist_ok=True)

# 1. Move temporary fix/update python scripts to 3_바이럴분석_SaaS_ViralScope/scripts/
temp_py_files = [
    'apply_full_topic_separation_fix.py',
    'apply_korean_filter_fix.py',
    'apply_mega_viral_fix.py',
    'apply_modal_sync_fix.py',
    'apply_pure_korean_account_fix.py',
    'apply_realtime_period_fix.py',
    'apply_strict_period_hierarchy_fix.py',
    'apply_unconditional_korean.py',
    'apply_view_sorting_fix.py',
    'test_fix.py',
    'update_dashboard.py'
]

for py in temp_py_files:
    src = os.path.join(root_dir, py)
    if os.path.exists(src):
        dst = os.path.join(scripts_dir, py)
        shutil.move(src, dst)
        print(f"Moved {py} -> 3_바이럴분석_SaaS_ViralScope/scripts/")

# 2. Sync index.html to 3_바이럴분석_SaaS_ViralScope
index_html = os.path.join(root_dir, 'index.html')
if os.path.exists(index_html):
    shutil.copy(index_html, os.path.join(dir_3, 'index.html'))
    shutil.copy(index_html, os.path.join(dir_3, 'preview.html'))
    print("Synchronized index.html to 3_바이럴분석_SaaS_ViralScope (index.html & preview.html)")

# 3. Clean up root directory clutter (redundant/corrupted bat files)
for item in os.listdir(root_dir):
    if item in ['run_dashboard.bat', 'run_studio.bat', 'run_viral_saas.bat'] or '\u26a1' in item or item.startswith('?'):
        p = os.path.join(root_dir, item)
        if os.path.isfile(p):
            os.remove(p)
            print(f"Removed clutter file from root: {item.encode('unicode_escape').decode('ascii')}")

# 4. Clean up dir_3 clutter (redundant/corrupted bat files)
for item in os.listdir(dir_3):
    if item in ['run_saas_preview.bat', '대시보드_바로열기.html', '실행_3_바이럴분석.bat'] or '\u26a1' in item or item.startswith('?'):
        p = os.path.join(dir_3, item)
        if os.path.isfile(p):
            os.remove(p)
            print(f"Removed clutter file from dir_3: {item.encode('unicode_escape').decode('ascii')}")

# 5. Create 3 ultra-clean, intuitive executable batch files in ROOT
bat_1_content = """@echo off
chcp 65001 > nul
title [1번 프로젝트] 제미나이 암호화폐 AI 자동매매 시스템
echo =======================================================================
echo     [1번] 제미나이 비트코인/이더리움 AI 자동매매 시스템을 실행합니다
echo =======================================================================
echo.
cd /d "%~dp01_자동매매_시스템"
if exist "[실행] 1_제미나이_자동매매.bat" (
    call "[실행] 1_제미나이_자동매매.bat"
) else (
    python main.py
)
pause
"""

bat_2_content = """@echo off
chcp 65001 > nul
title [2번 프로젝트] ShortsClone AI 쇼츠/릴스 자동 생성 스튜디오
echo =======================================================================
echo     [2번] ShortsClone AI 쇼츠 자동 생성 스튜디오를 실행합니다
echo =======================================================================
echo.
echo [1/2] 웹 스튜디오 브라우저를 엽니다 (http://127.0.0.1:8000)...
start "" "http://127.0.0.1:8000"
echo [2/2] 백엔드 AI 엔진 서버를 구동합니다...
echo.
cd /d "%~dp02_쇼츠생성기_ShortsClone"
python -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload
pause
"""

bat_3_content = """@echo off
chcp 65001 > nul
title [3번 프로젝트] ViralScope AI - 대한민국 숏폼 실시간 바이럴 분석 대시보드
echo =======================================================================
echo     [3번] ViralScope AI 숏폼 바이럴 분석 대시보드를 엽니다
echo =======================================================================
echo.
echo 웹 브라우저에서 대시보드를 즉시 실행합니다...
start "" "%~dp0index.html"
exit
"""

with open(os.path.join(root_dir, '[실행] 1_자동매매_시스템.bat'), 'w', encoding='utf-8') as f:
    f.write(bat_1_content)

with open(os.path.join(root_dir, '[실행] 2_쇼츠생성기_스튜디오.bat'), 'w', encoding='utf-8') as f:
    f.write(bat_2_content)

with open(os.path.join(root_dir, '[실행] 3_바이럴분석_대시보드.bat'), 'w', encoding='utf-8') as f:
    f.write(bat_3_content)

# Inside dir_3 as well:
with open(os.path.join(dir_3, '[실행] 대시보드_열기.bat'), 'w', encoding='utf-8') as f:
    f.write(bat_3_content)

print("Created 3 clean executable batch files in root!")

# 6. Update root README.md with clear, crystal-clear instructions
readme_content = """# 🚀 제미나이 바이블 코딩 - 프로젝트 통합 안내

이 폴더는 3개의 핵심 완성형 프로젝트로 완벽하게 정리되어 있습니다.  
폴더를 열고 **아래 3개의 실행 파일 중 원하시는 번호만 더블 클릭**하시면 즉시 실행됩니다!

---

## ⚡ 원클릭 바로 실행 목록

| 번호 | 바로가기 실행 파일 | 설명 |
| :---: | :--- | :--- |
| **1번** | **`[실행] 1_자동매매_시스템.bat`** | 제미나이 기반 비트코인/이더리움 AI 자동매매 봇 실행 |
| **2번** | **`[실행] 2_쇼츠생성기_스튜디오.bat`** | ShortsClone AI 영상 자동 제작 웹 스튜디오 (로컬 서버 + 웹 UI) |
| **3번** | **`[실행] 3_바이럴분석_대시보드.bat`** | ViralScope AI 대한민국 숏폼 실시간 바이럴 분석 대시보드 (또는 `index.html` 더블클릭) |

---

## 📁 프로젝트별 폴더 구성

1. **`1_자동매매_시스템/`**
   - 코인원(Coinone) API 기반 비트코인(BTC), 이더리움(ETH) 자동매매
   - 다중 지표(RSI, MACD, 볼린저밴드) + Gemini AI 시장 판단

2. **`2_쇼츠생성기_ShortsClone/`**
   - 텍스트 입력으로 60초 세로형 숏폼/릴스 영상 자동 렌더링
   - AI 내레이션(TTS), 자막 애니메이션, 템플릿 엔진

3. **`3_바이럴분석_SaaS_ViralScope/`**
   - 대한민국 종합 및 13개 카테고리별 실시간 숏폼 랭킹 분석 대시보드
   - 기간별(오늘, 1주, 1달, 3개월, 6개월, 1년) 75+개 영상 순위
   - 3초 훅 스크립트, 알고리즘 성공 요인, 바로 촬영 가능한 3선 복제 기획안
   - 보조 빌드 스크립트는 `3_바이럴분석_SaaS_ViralScope/scripts/`에 안전하게 보관됨
"""

with open(os.path.join(root_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("Updated root README.md successfully.")
