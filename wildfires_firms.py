# wildfires_firms.py
import requests
from base_sender import send_to_backend

FIRMS_URL = "https://firms.modaps.eosdis.nasa.gov/api/area/csv/"

def fetch_wildfires():
    payload = {"region": "Pakistan"}
    #send_to_backend("wildfire", "FIRMS", "Pakistan", payload)
    print(payload)