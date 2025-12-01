# glofs_glacial.py
import requests
from base_sender import send_to_backend

ICIMOD_GLOF_URL = "https://glofs.icimod.org/api/v1/hazards"
GLIMS_API = "https://www.glims.org/rest/glacier/"

REGION = {
    "lat_min": 33,
    "lat_max": 37.5,
    "lon_min": 73,
    "lon_max": 78
}

def fetch_glofs():
    glacial_report = {}

    # ---- 1. Fetch ICIMOD GLOF Hazard Index ----
    try:
        params = {
            "min_lat": REGION["lat_min"],
            "max_lat": REGION["lat_max"],
            "min_lon": REGION["lon_min"],
            "max_lon": REGION["lon_max"]
        }

        icimod_resp = requests.get(ICIMOD_GLOF_URL, params=params, timeout=10)
        glacial_report["icimod_glof_hazard"] = icimod_resp.json()

    except Exception as e:
        glacial_report["icimod_error"] = str(e)

    # ---- 2. Fetch GLIMS glacier/lake inventory ----
    try:
        glims_params = {
            "min_latitude": REGION["lat_min"],
            "max_latitude": REGION["lat_max"],
            "min_longitude": REGION["lon_min"],
            "max_longitude": REGION["lon_max"],
            "format": "geojson"
        }

        glims_resp = requests.get(GLIMS_API, params=glims_params, timeout=12)
        glacial_report["glims_glacial_lakes"] = glims_resp.json()

    except Exception as e:
        glacial_report["glims_error"] = str(e)

    # ---- 3. Alert threshold example ----
    # You can modify logic later inside Ktor backend
    try:
        high_risk_count = 0
        for lake in glacial_report.get("icimod_glof_hazard", []):
            if lake.get("hazard_level") in ["high", "very_high"]:
                high_risk_count += 1

        glacial_report["high_risk_lakes"] = high_risk_count
    except:
        pass

    # ---- Send to Ktor backend ----
    send_to_backend(
        disaster_type="glof",
        source="ICIMOD + GLIMS",
        region="Northern Pakistan (Karakoram, Himalaya)",
        data=glacial_report
    )
