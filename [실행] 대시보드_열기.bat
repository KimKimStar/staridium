@echo off
chcp 65001 > nul
title [3번 프로젝트] ViralScope AI - 대한민국 유튜브 쇼츠 실시간 바이럴 분석 대시보드
echo =======================================================================
echo     [3번] ViralScope AI 유튜브 쇼츠 실시간 바이럴 대시보드를 엽니다
echo =======================================================================
echo.

cd /d "%~dp0"

set "PYTHON_EXE="

:: 1. Check python in PATH
python --version > nul 2>&1
if not errorlevel 1 (
    set "PYTHON_EXE=python"
    goto :START_SERVER
)

:: 2. Check py launcher
py --version > nul 2>&1
if not errorlevel 1 (
    set "PYTHON_EXE=py"
    goto :START_SERVER
)

:: 3. Check common Python installation paths
if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
    set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
    goto :START_SERVER
)
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
    goto :START_SERVER
)
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
    goto :START_SERVER
)

:START_SERVER
if defined PYTHON_EXE (
    echo [1/2] 로컬 웹서버(http://127.0.0.1:8500) 구동 중 (유튜브 Error 153 방지)...
    start /b "" "%PYTHON_EXE%" serve.py > nul 2>&1
    timeout /t 2 /nobreak > nul
    echo [2/2] 브라우저에서 대시보드를 엽니다...
    start "" "http://127.0.0.1:8500/index.html"
) else (
    echo [안내] Python을 감지하지 못하여 로컬 파일 모드로 즉시 실행합니다...
    start "" "index.html"
)

exit
