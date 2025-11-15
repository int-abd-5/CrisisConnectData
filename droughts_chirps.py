# droughts_chirps.py
import requests
from base_sender import send_to_backend

CHIRPS_URL = "https://data.chc.ucsb.edu/products/CHIRPS-2.0/"

def fetch_droughts():
    # CHIRPS requires raster extraction; placeholder metadata
    data = {"status": "chirps_drought_analysis_pending"}
    #send_to_backend("drought", "CHIRPS", "Pakistan", data)
    print(data)