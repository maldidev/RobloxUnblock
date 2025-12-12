# IF YOU HAVE THOUGH THAT IS WILL RUIN YOUR COMPUTER THEN EDIT IT.
# THIS FILE IS NOT SAFE FOR USING AS NOT PROFFESIONAL!
@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo Region Changer for Windows
echo.

if "%1"=="set" (
    echo Setting random region...
    python region_manager.py set
) else if "%1"=="restore" (
    echo Restoring original settings...
    python region_manager.py restore
) else if "%1"=="status" (
    echo Current status:
    python region_manager.py status
) else (
    echo Usage: %0 [set^|restore^|status]
    echo.
    echo   set     - Set random region
    echo   restore - Restore original
    echo   status  - Show current
)

pause
