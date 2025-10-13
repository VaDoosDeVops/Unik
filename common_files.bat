@echo off
setlocal
if "%~1"=="" echo Usage: common_files.bat "C:\dir1" "C:\dir2" & exit /b 1
if "%~2"=="" echo Usage: common_files.bat "C:\dir1" "C:\dir2" & exit /b 1
set "D1=%~1"
set "D2=%~2"
if not exist "%D1%" echo Error: dir1 not found & exit /b 2
if not exist "%D2%" echo Error: dir2 not found & exit /b 3
for %%F in ("%D1%\*") do if exist "%D2%\%%~nxF" echo %%~nxF
endlocal
