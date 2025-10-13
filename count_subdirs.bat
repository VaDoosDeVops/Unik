@echo off
setlocal enabledelayedexpansion
if "%~1"=="" echo Usage: count_subdirs.bat "C:\path" & exit /b 1
set "ROOT=%~1"
if not exist "%ROOT%" echo Error: directory not found & exit /b 2
set /a cnt=0
for /d /r "%ROOT%" %%D in (*) do set /a cnt+=1
echo %cnt%
endlocal
