# cyclones_gdacs.py
import requests
from base_sender import send_to_backend

URL = "https://www.gdacs.org/xml/rss.xml"

def fetch_cyclones():
    data = requests.get(URL).text
    #send_to_backend("cyclone", "GDACS", "Asia", {"rss": data})
    print(data)