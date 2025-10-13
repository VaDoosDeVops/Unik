@echo off
setlocal enabledelayedexpansion
if "%~1"=="" echo Usage: factorial.bat N & exit /b 1
set "n=%~1"
echo %n%| findstr /r "^[0-9][0-9]*$" >nul || (echo Error: N must be non-negative integer & exit /b 2)
if %n% gtr 12 echo Error: N too large for 32-bit (max 12) & exit /b 3
set /a f=1
for /l %%i in (1,1,%n%) do set /a f*=%%i
echo FACTORIAL(%n%)=%f%
endlocal
