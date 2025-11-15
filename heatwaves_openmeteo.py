# heatwaves_openmeteo.py
import requests
from base_sender import send_to_backend

URL = "https://api.open-meteo.com/v1/forecast"

def fetch_heatwaves():
    params = {
        "latitude": 24,
        "longitude": 67,
        "hourly": "temperature_2m",
        "timezone": "Asia/Karachi"
    }
    data = requests.get(URL, params=params).json()
    #send_to_backend("heatwave", "Open-Meteo", "Pakistan", data)
    print(data)