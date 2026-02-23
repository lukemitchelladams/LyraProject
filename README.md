# ✦ Lyra — AI Assistant & Prompt Optimization Engine

Lyra is a conversational AI assistant built on Anthropic's Claude API, wrapped in a clean, dark-themed web interface built with Streamlit. It combines the power of a large language model with a specialized prompt-optimization persona — helping users not just get answers, but get *better* at asking questions.

---

## 🖥️ Live Demo

> [Insert your Streamlit URL here once deployed]

---

## 💡 What It Does

Lyra acts as a general-purpose AI assistant with a twist: she brings prompt-engineering expertise into every conversation. She can:

- Answer questions and explain complex concepts
- Write, edit, and proofread content
- Debug and write code
- Brainstorm ideas and help with creative tasks
- Optimize and refine prompts for use across AI platforms (ChatGPT, Claude, Gemini)
- Apply the **4-D prompt framework** on demand: Deconstruct → Diagnose → Develop → Deliver

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| AI Model | Anthropic Claude (claude-sonnet-4-6) |
| Language | Python 3.9+ |
| Styling | Custom CSS with Google Fonts |
| Streaming | Anthropic streaming API |
| Hosting | Streamlit Community Cloud |

---

## ✨ Features

- **Real-time streaming responses** — see Lyra typing word by word
- **Full conversation memory** — context is preserved throughout the session
- **New Chat** button to start fresh at any time
- **Secure API key input** — users supply their own Anthropic key, never stored
- **Clean dark UI** — custom-designed interface with gradient typography and monospace fonts
- **Responsive layout** — works in browser on desktop and mobile

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/lyra.git
cd lyra
```

**2. Install dependencies**
```bash
pip3 install streamlit anthropic
```

**3. Run the app**
```bash
python3 -m streamlit run lyra.py
```

**4. Open your browser**
Navigate to `http://localhost:8501` and enter your [Anthropic API key](https://console.anthropic.com/settings/keys).

---

## 🔑 Getting an API Key

1. Sign up at [console.anthropic.com](https://console.anthropic.com)
2. Go to **Settings → API Keys → Create Key**
3. Paste it into the Lyra interface when prompted

Each user supplies their own key — Lyra does not store or share keys.

---

## 📁 Project Structure

```
lyra/
├── lyra.py          # Main Streamlit application
├── requirements.txt # Python dependencies
└── README.md        # This file
```

---

## 🧠 How the Prompt System Works

Lyra runs on a custom system prompt that gives Claude a specialized persona. Rather than acting as a generic assistant, Lyra is instructed to:

- Lead with answers, not process
- Bring prompt-engineering insight naturally into responses
- Apply structured frameworks only when explicitly requested
- Treat users as intelligent and capable

This demonstrates how system prompt design shapes model behavior — a core skill in modern AI product development.

---

## 🗺️ Roadmap

- [ ] Persistent chat history across sessions
- [ ] Export conversations as PDF or Markdown
- [ ] Custom persona/system prompt editor in the UI
- [ ] Multi-model support (GPT-4, Gemini)
- [ ] One-click deploy button

---

## 👤 Author

Built by [Your Name](https://github.com/yourusername)
[LinkedIn](https://linkedin.com/in/yourprofile) · [Portfolio](https://yourwebsite.com)

---

## 📄 License

MIT License — free to use, modify, and distribute.
