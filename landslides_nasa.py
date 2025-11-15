# landslides_nasa.py
import requests
from base_sender import send_to_backend

URL = "https://data.nasa.gov/resource/mset-9xjg.json"

def fetch_landslides():
    params = {"$limit": 5000}
    data = requests.get(URL, params=params).json()
    #send_to_backend("landslide", "NASA_Landslides", "Pakistan", data)
    print(data)