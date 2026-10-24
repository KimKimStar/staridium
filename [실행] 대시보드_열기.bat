@echo off
chcp 65001 > nul
title [3번 프로젝트] ViralScope AI - 대한민국 유튜브 쇼츠 실시간 바이럴 분석 대시보드
echo =======================================================================
echo     [3번] ViralScope AI 유튜브 쇼츠 실시간 바이럴 대시보드를 엽니다
echo =======================================================================
echo.
echo [1/2] 로컬 웹서버를 실행합니다 (유튜브 영상 오류 153 방지)...
cd /d "%~dp0"
start /b "" python serve.py > nul 2>&1
timeout /t 1 /nobreak > nul

echo [2/2] 브라우저에서 대시보드를 엽니다...
start "" "http://127.0.0.1:8500/index.html"
exit
