import requests
from base_sender import send_to_backend

URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"

PAK_LAT_MIN = 23
PAK_LAT_MAX = 38
PAK_LON_MIN = 60
PAK_LON_MAX = 80

def fetch_earthquakes():
    response = requests.get(URL)
    data = response.json()

    pakistan_eqs = []

    for feature in data["features"]:
        lon, lat, depth = feature["geometry"]["coordinates"]

        if PAK_LAT_MIN <= lat <= PAK_LAT_MAX and PAK_LON_MIN <= lon <= PAK_LON_MAX:
            pakistan_eqs.append({
                "magnitude": feature["properties"]["mag"],
                "place": feature["properties"]["place"],
                "time": feature["properties"]["time"],
                "depth_km": depth,
                "coordinates": {"lat": lat, "lon": lon}
            })

    if pakistan_eqs:
        #send_to_backend("earthquake", "USGS", "Pakistan", {"events": pakistan_eqs})
        print(pakistan_eqs)