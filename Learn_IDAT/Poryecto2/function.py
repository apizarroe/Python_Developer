from datetime import datetime, timedelta
import os.path
import pytz
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

lima_timezone = pytz.timezone('America/Lima')

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
SERVICE_ACCOUNT_FILE = 'service.json'

date_time_start = ""
date_start = ""
time_start = ""
date_time_end = ""
date_end = ""
time_end = ""
summary = ""
description = ""
location = ""


def lambda_handler(event, context):

  creds = None
  calendar_id = 'apizarroe13@gmail.com'  # Replace with the actual calendar ID

  creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    lima_time = datetime.now(lima_timezone)
    lime_time_iso = lima_time.isoformat()
    one_minute_later = (lima_time + timedelta(minutes=1))
    one_minute_later_iso = one_minute_later.isoformat()

    #"primary"
    
    print("Getting the upcoming 10 events")
    events_result = (
        service.events().list(
            calendarId=calendar_id,
            timeMin=lime_time_iso,
            timeMax=one_minute_later_iso,
            maxResults=5,
            singleEvents=True,
            orderBy="startTime",
        ).execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 1 event
    for event in events:
      date_time_start = event["start"].get("dateTime", event["start"].get("date"))[:19]
      date_start = date_time_start[:10]
      time_start = date_time_start[11:19]
      date_time_end = event["end"].get("dateTime", event["end"].get("date"))[:19]
      date_end = date_time_end[:10]
      time_end = date_time_end[11:19]
      summary = event.get('summary', '')
      description = event.get('description', '')
      location = event.get('location', '')
      #print(f"Fecha Inicio: {date_start}")
      #print(f"Hora Inicio: {time_start}")
      #print(f"Fecha Fin: {date_end}")
      #print(f"Hora Fin: {time_end}")
      #print(f"Resumen: {summary}")
      #print(f"Descripción: {description}")
      #print(f"Ubicación: {location}")
      
      dictionary ={"date_start":date_start, "time_start":time_start,
            "date_end":date_end, "time_end":time_end,
            "summary":summary, "description": description,
            "location":location
      }
    
    return {
      'statusCode': 200,
      'body': json.dumps(dictionary)
    }

  except HttpError as error:
    print(f"An error occurred: {error}")