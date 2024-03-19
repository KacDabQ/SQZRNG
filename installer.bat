@echo off
setlocal EnableDelayedExpansion

REM Installing Keyboard Module...
echo Installing Keyboard Module...
pip install keyboard

REM Check, if installed properly...
if %errorlevel% neq 0 (
    echo Error - Keyboard module installing went wrong
    exit /b %errorlevel%
) else (
    echo Keyboard module installed
)

pause
