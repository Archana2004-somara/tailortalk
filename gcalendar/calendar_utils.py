import datetime, os, pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = None
    token_path = os.path.join(os.path.dirname(__file__), 'token.json')
    creds_path = os.path.join(os.path.dirname(__file__), 'credentials.json')

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)

def check_availability(start_time, end_time, calendar_id='primary'):
    service = get_calendar_service()
    body = {
        "timeMin": start_time,
        "timeMax": end_time,
        "timeZone": "Asia/Kolkata",
        "items": [{"id": calendar_id}]
    }
    result = service.freebusy().query(body=body).execute()
    return result['calendars'][calendar_id]['busy']

def create_event(start_time_str, end_time_str, summary, description, calendar_id='primary'):
    service = get_calendar_service()
    event = {
        'summary': summary,
        'description': description,
        'start': {'dateTime': start_time_str, 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end_time_str, 'timeZone': 'Asia/Kolkata'},
    }
    result = service.events().insert(calendarId=calendar_id, body=event).execute()
    return result.get('htmlLink')
