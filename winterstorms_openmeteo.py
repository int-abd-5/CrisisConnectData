# winterstorms_openmeteo.py
import requests
from base_sender import send_to_backend

URL = "https://api.open-meteo.com/v1/forecast"

def fetch_winterstorms():
    params = {
        "latitude": 35,
        "longitude": 74,
        "hourly": "snowfall,temperature_2m",
        "timezone": "Asia/Karachi"
    }
    data = requests.get(URL, params=params).json()
    #send_to_backend("winter_storm", "Open-Meteo", "North Pakistan", data)
    print(data)