from datetime import datetime
from dateutil import parser
from langchain.tools import tool
from gcalendar.calendar_utils import check_availability, create_event

@tool
def check_calendar(start_time: str, end_time: str) -> str:
    """Check if a time slot is free between start_time and end_time."""
    start_dt = parser.parse(start_time)
    now = datetime.now()
    if start_dt < now:
        return "❌ Cannot check past time. Please select a future time slot."
    available = check_availability(start_time, end_time)
    return "✅ Slot is available." if available else "❌ Slot is already booked."

@tool
def book_calendar(start_time: str, end_time: str, summary: str) -> str:
    """Book a calendar meeting using start_time, end_time and summary."""
    start_dt = parser.parse(start_time)
    now = datetime.now()
    if start_dt < now:
        return "❌ Cannot book a meeting in the past. Please choose a future time."
    event = create_event(start_time, end_time, summary)
    return f"✅ Meeting booked: {event['htmlLink']}"
