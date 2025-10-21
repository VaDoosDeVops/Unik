@echo off
setlocal enabledelayedexpansion
if "%~1"==""  echo Usage: list_by_ext.bat "C:\path" EXT & exit /b 1
if "%~2"==""  echo Usage: list_by_ext.bat "C:\path" EXT & exit /b 1
set "DIR=%~1"
set "EXT=%~2"
if not exist "%DIR%" echo Error: directory not found & exit /b 2
for %%F in ("%DIR%\*.%EXT%") do echo %%~nxF
endlocal
