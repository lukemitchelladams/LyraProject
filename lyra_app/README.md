# ✦ Lyra — Prompt Optimization Desktop App

## Setup (one time only)

### 1. Install Python
Download from https://python.org (3.9 or higher)

### 2. Install dependencies
Open Terminal (Mac) or Command Prompt (Windows) and run:
```
pip install streamlit anthropic
```

### 3. Get your Anthropic API key
Go to https://console.anthropic.com → API Keys → Create Key

---

## Launch

**Mac/Linux:**
Double-click `launch_lyra_mac.sh`
(or run: `bash launch_lyra_mac.sh`)

**Windows:**
Double-click `launch_lyra_windows.bat`

Your browser will open automatically at http://localhost:8501

---

## Usage
1. Paste your API key in the sidebar
2. Type what you want to build or optimize
3. Lyra will deconstruct, diagnose, develop, and deliver your prompt
4. Use "New Chat" to start fresh or "Export Chat" to save your session

---

## Optional: Set API key permanently
So you don't have to paste it every time, set an environment variable:

**Mac/Linux** (add to ~/.zshrc or ~/.bashrc):
```
export ANTHROPIC_API_KEY="sk-ant-..."
```

**Windows** (run in Command Prompt):
```
setx ANTHROPIC_API_KEY "sk-ant-..."
```
