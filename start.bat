@echo off
chcp 65001 >nul
setlocal
cd /d %~dp0

echo [FaceFusion] 正在启动，请稍候...
python quick_start.py
if errorlevel 1 (
  echo.
  echo [FaceFusion] 启动失败，请查看 error.log
  pause
)
endlocal
