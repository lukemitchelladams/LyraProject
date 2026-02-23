import streamlit as st
import anthropic
import os

st.set_page_config(
    page_title="Lyra",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:ital,wght@0,300;0,400;1,300&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Mono', monospace;
    background-color: #0a0a0f;
    color: #e8e4d9;
}
.stApp { background: #0a0a0f; }

.lyra-logo {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #c8b8ff 0%, #8be8cb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.stTextInput input, .stTextArea textarea {
    background: #0f0f18 !important;
    border: 1px solid #252540 !important;
    border-radius: 8px !important;
    color: #e8e4d9 !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.87rem !important;
}

.stButton > button {
    background: linear-gradient(135deg, #1e1040 0%, #0f1e2e 100%) !important;
    border: 1px solid #3a2a7a !important;
    color: #c8b8ff !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.82rem !important;
    border-radius: 8px !important;
    width: 100% !important;
}
.stButton > button:hover {
    border-color: #8be8cb !important;
    color: #8be8cb !important;
}

hr { border-color: #1a1a2e !important; }
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

LYRA_SYSTEM = """You are "Lyra," a prompt-optimization specialist. When the user asks you something, help them directly and conversationally — answer their questions, assist with tasks, write things, explain concepts, debug code, brainstorm ideas, and so on.

However, you bring your prompt-optimization expertise naturally into every response. When relevant, you suggest clearer ways to phrase future questions, note if a task could be broken down better, or offer to generate optimized prompts for use in other tools. Apply the 4-D framework (Deconstruct, Diagnose, Develop, Deliver) only when the user explicitly wants a prompt built.

You are warm, sharp, and direct. You don't over-explain. You treat the user as intelligent. You lead with the answer, not the process."""

if "messages" not in st.session_state:
    st.session_state.messages = []
if "api_key" not in st.session_state:
    st.session_state.api_key = os.environ.get("ANTHROPIC_API_KEY", "")

# Header
col_logo, col_new = st.columns([4, 1])
with col_logo:
    st.markdown('<div class="lyra-logo">✦ Lyra</div>', unsafe_allow_html=True)
with col_new:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("New Chat"):
        st.session_state.messages = []
        st.rerun()

st.markdown("---")

# API key gate
if not st.session_state.api_key:
    api_input = st.text_input("🔑 Anthropic API Key", type="password", placeholder="sk-ant-...")
    if api_input:
        st.session_state.api_key = api_input
        st.rerun()
    st.info("Enter your API key above to start chatting.")
    st.stop()

# Chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.write(msg["content"])

# Input
user_input = st.chat_input("Type your message…")

if user_input and user_input.strip():
    # Show user message immediately
    st.session_state.messages.append({"role": "user", "content": user_input.strip()})
    with st.chat_message("user"):
        st.write(user_input.strip())

    # Stream Lyra's response
    with st.chat_message("assistant"):
        try:
            client = anthropic.Anthropic(api_key=st.session_state.api_key)
            with client.messages.stream(
                model="claude-sonnet-4-6",
                max_tokens=2048,
                system=LYRA_SYSTEM,
                messages=st.session_state.messages
            ) as stream:
                reply = st.write_stream(stream.text_stream)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Error: {e}")
            st.session_state.messages.pop()
