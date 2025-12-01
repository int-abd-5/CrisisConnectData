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
    glacial_report = {
        "icimod_glof_hazard": [],
        "glims_glacial_lakes": {},
        "high_risk_lakes": 0
    }

    # -------------------------
    # 1. ICIMOD GLOF HAZARD API
    # -------------------------
    try:
        params = {
            "min_lat": REGION["lat_min"],
            "max_lat": REGION["lat_max"],
            "min_lon": REGION["lon_min"],
            "max_lon": REGION["lon_max"]
        }

        resp = requests.get(ICIMOD_GLOF_URL, params=params, timeout=15)
        data = resp.json()

        # API sometimes returns {"data":[...]} instead of [...]
        if isinstance(data, dict) and "data" in data:
            glacial_report["icimod_glof_hazard"] = data["data"]
        elif isinstance(data, list):
            glacial_report["icimod_glof_hazard"] = data
        else:
            glacial_report["icimod_glof_hazard"] = []

    except Exception as e:
        glacial_report["icimod_error"] = str(e)

    # -------------------------
    # 2. GLIMS GLACIAL LAKE DATA
    # -------------------------
    try:
        glims_params = {
            "min_latitude": REGION["lat_min"],
            "max_latitude": REGION["lat_max"],
            "min_longitude": REGION["lon_min"],
            "max_longitude": REGION["lon_max"],
            "format": "geojson"
        }

        resp = requests.get(GLIMS_API, params=glims_params, timeout=20)
        if resp.headers.get("Content-Type", "").startswith("application/json") \
           or resp.text.strip().startswith("{"):

            glacial_report["glims_glacial_lakes"] = resp.json()
        else:
            glacial_report["glims_glacial_lakes"] = {"error": "Invalid response format"}

    except Exception as e:
        glacial_report["glims_error"] = str(e)

    # -------------------------
    # 3. RISK SCORING
    # -------------------------
    try:
        high_count = 0
        for lake in glacial_report["icimod_glof_hazard"]:
            level = lake.get("hazard_level", "").lower()
            if level in ("high", "very_high"):
                high_count += 1

        glacial_report["high_risk_lakes"] = high_count

    except Exception as e:
        glacial_report["risk_calc_error"] = str(e)

    # -------------------------
    # 4. SEND TO BACKEND
    # -------------------------
    send_to_backend(
        disaster_type="glof",
        source="icimod + glims",
        region="Northern Pakistan (Karakoram, Himalaya)",
        data=glacial_report
        #print(data)
    )
