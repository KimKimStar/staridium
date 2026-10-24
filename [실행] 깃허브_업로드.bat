@echo off
chcp 65001 >nul
title 3번 프로젝트 깃허브 업로드
cd /d "%~dp0"
echo ========================================================
echo   [3번 프로젝트] ViralScope 깃허브 업로드 프로그램
echo   저장소: https://github.com/KimKimStar/staridium.git
echo ========================================================
echo.
echo 깃허브 보안 정책상 일반 비밀번호 대신 [개인 액세스 토큰]이 필요합니다.
echo.
echo [토큰 발급 30초 안내]
echo 1. https://github.com/settings/tokens 에 접속
echo 2. [Generate new token (classic)] 클릭
echo 3. Note에 staridium 입력, 'repo' 체크박스 체크 후 맨 아래 생성 클릭
echo 4. 생성된 ghp_... 토큰을 복사하여 아래에 붙여넣기
echo.
set /p TOKEN="깃허브 토큰(ghp_...) 입력: "

if "%TOKEN%"=="" (
    echo 토큰이 입력되지 않았습니다.
    pause
    exit /b
)

echo.
echo 깃허브(KimKimStar/staridium)로 업로드를 시작합니다...
"C:\Users\kwang\AppData\Local\Programs\Git\cmd\git.exe" push https://%TOKEN%@github.com/KimKimStar/staridium.git main
if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================================
    echo  ★ 업로드 대성공! 깃허브에 최신 파일이 반영되었습니다! ★
    echo ========================================================
) else (
    echo.
    echo [오류] 업로드 중 문제가 발생했습니다. 토큰 권한(repo 체크 여부)을 확인해주세요.
)
pause
