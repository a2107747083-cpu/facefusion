@echo off
setlocal

REM Build Windows desktop app for FaceFusion
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pyinstaller

pyinstaller --noconfirm --clean --windowed --name FaceFusionDesktop ^
  --icon facefusion.ico ^
  --add-data "facefusion;facefusion" ^
  desktop_app_entry.py

echo.
echo Build completed.
echo EXE path: dist\FaceFusionDesktop\FaceFusionDesktop.exe
endlocal
