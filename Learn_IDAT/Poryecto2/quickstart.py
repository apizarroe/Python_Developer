from datetime import datetime, timedelta
import os.path
import pytz

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

lima_timezone = pytz.timezone('America/Lima')

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    lima_time = datetime.now(lima_timezone)
    lime_time_iso = lima_time.isoformat()
    one_minute_later = (lima_time + timedelta(minutes=1))
    one_minute_later_iso = one_minute_later.isoformat()
    #now = now_utc.astimezone(tz).isoformat()
    #now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    events_result = (
        service.events().list(
            calendarId="primary",
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

    # Prints the start and name of the next 10 events
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
      print(event["start"].get("dateTime", event["start"].get("date")))
      print(event["end"].get("dateTime", event["end"].get("date")))
      print(f"Fecha Inicio: {date_start}")
      print(f"Hora Inicio: {time_start}")
      print(f"Fecha Fin: {date_end}")
      print(f"Hora Fin: {time_end}")
      print(f"Resumen: {summary}")
      print(f"Descripción: {description}")
      print(f"Ubicación: {location}")

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()