# floods_gfms.py
import requests
from base_sender import send_to_backend

GFMS_URL = "https://flooddata.apps.nasa.gov/gfms/v1/"

def fetch_floods():
    try:
        data = requests.get(GFMS_URL).json()
        #send_to_backend("flood", "NASA_GFMS", "Pakistan", data)
        print(data)
    except:
        print("[ERROR] GFMS fetch failed")
