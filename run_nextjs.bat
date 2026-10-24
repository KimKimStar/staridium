@echo off
chcp 65001 > nul
title ViralScope AI - Next.js 서버 구동

echo =====================================================================
echo  🔥 ViralScope AI - Next.js 풀스택 개발 서버 구동 스크립트
echo =====================================================================
echo.

where node >nul 2>nul
if %errorlevel% neq 0 (
    echo [안내] 시스템에 Node.js가 설치되어 있지 않습니다.
    echo Node.js 설치 전에도 UI와 기능을 즉시 체험할 수 있도록
    echo 독립형 웹 대시보드(preview.html)를 브라우저로 띄웁니다!
    echo.
    echo (Node.js 공식 다운로드: https://nodejs.org/)
    echo.
    start "" "%~dp0preview.html"
    pause
    exit /b
)

echo [1/3] Node.js 버전 확인 완료!
node -v

if not exist "%~dp0node_modules" (
    echo [2/3] 필수 패키지를 설치합니다 (최초 1회, 수 분 소요)...
    cd /d "%~dp0"
    call npm install
)

echo [3/3] Next.js 로컬 개발 서버를 시작합니다 (http://localhost:3000)...
cd /d "%~dp0"
start http://localhost:3000
call npm run dev

pause
