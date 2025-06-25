from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gcalendar.calendar_utils import check_availability, create_event
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AvailabilityRequest(BaseModel):
    start_time: str
    end_time: str

class BookingRequest(BaseModel):
    start_time: str
    end_time: str
    summary: str
    description: str = ""

@app.post("/check-availability")
def api_check_availability(request: AvailabilityRequest):
    try:
        busy = check_availability(request.start_time, request.end_time)
        return {"available": len(busy) == 0, "busy": busy}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/book")
def api_book(request: BookingRequest):
    try:
        link = create_event(request.start_time, request.end_time, request.summary, request.description)
        return {"success": True, "event_link": link}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
