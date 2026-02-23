#!/bin/bash
# Lyra — one-click launcher for Mac/Linux

echo "✦ Starting Lyra..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Please install it from https://python.org"
    exit 1
fi

# Install dependencies if needed
python3 -c "import streamlit" 2>/dev/null || pip3 install streamlit anthropic

# Launch
cd "$(dirname "$0")"
streamlit run lyra.py --server.port 8501 --server.headless false
