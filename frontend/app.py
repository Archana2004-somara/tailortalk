import sys
import os

# ✅ Add parent directory to sys.path so `agent/` can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agent.agent_flow import run_agent
import base64

# ✅ Page settings
st.set_page_config(page_title="TailorTalk 🤖", page_icon="📅")

# ✅ Load and display logo
logo_path = os.path.join(os.path.dirname(__file__), "tailortalk-logo.png")
with open(logo_path, "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode()

st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{encoded}" width="200">
        <h1>TailorTalk - AI Calendar Booking Agent</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# ✅ Instruction message
st.markdown("Ask me to book or check meetings like:")
st.code("Book a meeting for tomorrow at 4 PM")

# ✅ Chat input
user_input = st.chat_input("What would you like to do?")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        response = run_agent(user_input)
        st.write(response)
