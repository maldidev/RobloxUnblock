@echo off
chcp 65001 >nul

echo === Universal Region Changer ===
echo.
echo 1. Set random region
echo 2. Restore original
echo 3. Show status
echo 4. Exit
echo.

set /p choice="Select option (1-4): "

if "%choice%"=="1" (
    call region_win.bat set
) else if "%choice%"=="2" (
    call region_win.bat restore
) else if "%choice%"=="3" (
    call region_win.bat status
) else if "%choice%"=="4" (
    exit /b 0
) else (
    echo Invalid choice
)

pause