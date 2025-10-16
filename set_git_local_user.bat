@echo off
setlocal

REM ---- Проверка параметров ----
if "%~1"=="" (
  echo Usage: %~nx0 "User Name" "email@example.com"
  exit /b 1
)
if "%~2"=="" (
  echo Usage: %~nx0 "User Name" "email@example.com"
  exit /b 1
)

set "GIT_USER=%~1"
set "GIT_EMAIL=%~2"

REM ---- Проверка наличия Git ----
where git >nul 2>&1
if errorlevel 1 (
  echo Git is not found in PATH. Install Git and retry.
  exit /b 2
)

REM ---- Проверка, что скрипт запускается внутри репозитория ----
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
  echo Not inside a Git repository. Change to repository folder and retry.
  exit /b 3
)

REM ---- Установка локального пользователя ----
git config --local user.name "%GIT_USER%"
git config --local user.email "%GIT_EMAIL%"

echo Local Git user for THIS repository set successfully:
echo   user.name  = %GIT_USER%
echo   user.email = %GIT_EMAIL%

endlocal
exit /b 0
