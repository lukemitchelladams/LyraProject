@echo off
echo ✦ Starting Lyra...

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found. Please install it from https://python.org
    pause
    exit /b
)

:: Install dependencies if needed
python -c "import streamlit" 2>nul || pip install streamlit anthropic

:: Launch
cd /d "%~dp0"
streamlit run lyra.py --server.port 8501 --server.headless false

pause
