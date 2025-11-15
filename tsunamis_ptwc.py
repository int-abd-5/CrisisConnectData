# tsunamis_ptwc.py
import requests
from base_sender import send_to_backend

URL = "https://www.tsunami.gov/events/xml/PTWC.xml"

def fetch_tsunamis():
    data = requests.get(URL).text
    #send_to_backend("tsunami", "PTWC", "Indian Ocean", {"xml": data})
    print(data)