TailorTalk – AI Calendar Booking Agent

TailorTalk is an AI-powered assistant that helps users schedule meetings via natural chat. It checks availability, suggests slots, and books meetings directly on your Google Calendar — all through a smooth conversational UI.

---

Features

- Conversational interface with Streamlit
-LangGraph-powered agent using GPT-style models
-Google Calendar integration (check & book)
-Modular project structure (agent/, backend/, frontend/, gcalendar/)
- Rejects invalid or past time slots
- Gracefully handles fallback messages and multiple requests

Example Prompts

```plaintext
• Book a meeting for tomorrow at 3 PM
• Do you have any free time on Friday?
• Check if 10 AM to 11 AM next Wednesday is free
• Schedule a 30-minute call next week
