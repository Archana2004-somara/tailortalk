import sys
import os
import base64

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agent.agent_flow import run_agent

# ✅ Page setup
st.set_page_config(page_title="TailorTalk 🤖", page_icon="📅")

# ✅ Absolute path logo loading (no errors!)
logo_path = os.path.join(os.path.dirname(__file__), "tailortalk-logo.png")
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{base64.b64encode(open(logo_path, "rb").read()).decode()}" width="230">
    </div>
    """,
    unsafe_allow_html=True
)


# ✅ Centered title under logo
st.markdown("<h1 style='text-align: center;'>TailorTalk - AI Calendar Booking Agent</h1>", unsafe_allow_html=True)

# ✅ Chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✅ Chat input
user_input = st.chat_input("Say something like: 'Book a call tomorrow at 4 PM'")

if user_input:
    # Show user message
    st.chat_message("user").write(user_input)

    # Call LangGraph agent
    try:
        ai_response = run_agent(user_input)
    except Exception as e:
        ai_response = f"⚠️ Error: {str(e)}"

    # Show AI response
    st.chat_message("assistant").write(ai_response)

    # Save to history
    st.session_state.chat_history.append((user_input, ai_response))
