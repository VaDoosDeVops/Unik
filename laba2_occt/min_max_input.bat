@echo off
setlocal ENABLEDELAYEDEXPANSION

echo Enter integers one by one. Type "-" to finish.

set "min="
set "max="

:loop
set "x="
REM важный фикс: подсказка в кавычках, иначе ">" станет перенаправлением
set /p "x=> "
if "%x%"=="-" goto done
if "%x%"=="" goto loop

REM проверка: целое (может начинаться с -)
echo %x%| findstr /r "^-*[0-9][0-9]*$" >nul || (
  echo Invalid input, enter integer or "-" to finish.
  goto loop
)

if not defined min (
  set "min=%x%"
  set "max=%x%"
) else (
  REM числовое сравнение без set /a
  if !x! LSS !min! set "min=!x!"
  if !x! GTR !max! set "max=!x!"
)

goto loop

:done
if not defined min (
  echo No numbers were entered.
) else (
  echo MIN = !min!
  echo MAX = !max!
)
endlocal
