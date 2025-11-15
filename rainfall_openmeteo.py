import requests
from base_sender import send_to_backend

URL = "https://api.open-meteo.com/v1/forecast"

def fetch_rainfall():
    params = {
        "latitude": 30.0,
        "longitude": 70.0,
        "hourly": "precipitation,wind_speed_10m,temperature_2m",
        "timezone": "Asia/Karachi"
    }

    data = requests.get(URL, params=params).json()
    #send_to_backend("rainfall", "Open-Meteo", "Pakistan", data)
    print(data)