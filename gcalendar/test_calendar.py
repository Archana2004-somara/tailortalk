from datetime import datetime, timedelta
from calendar_utils import check_availability, create_event

now = datetime.utcnow()
start = (now + timedelta(hours=2)).isoformat() + 'Z'
end = (now + timedelta(hours=3)).isoformat() + 'Z'

busy = check_availability(start, end)
print("Busy slots:", busy)

if not busy:
    link = create_event(start, end, "TailorTalk Meeting", "Let's meet")
    print("Event created:", link)
else:
    print("Slot not available")
