import requests
from langchain.tools import tool

API_BASE = "http://127.0.0.1:8000"

@tool
def check_calendar(start_time: str, end_time: str) -> str:
    """Check if the specified time slot is available in Google Calendar."""
    response = requests.post(f"{API_BASE}/check-availability", json={
        "start_time": start_time,
        "end_time": end_time
    })
    data = response.json()
    return "Available ✅" if data.get("available") else f"Busy ❌: {data.get('busy')}"

@tool
def book_calendar(start_time: str, end_time: str, summary: str) -> str:
    """Book a Google Calendar event between the given times with a summary."""
    response = requests.post(f"{API_BASE}/book", json={
        "start_time": start_time,
        "end_time": end_time,
        "summary": summary,
        "description": "Booked via TailorTalk"
    })
    data = response.json()
    return f"Event booked! 📅 Link: {data.get('event_link')}"
