import requests
import json
from datetime import datetime

BACKEND_URL = "https://pajnukvjxmwhdglngkyc.supabase.co/api/disasters/ingest"

def send_to_backend(disaster_type: str, source: str, region: str, data: dict):
    payload = {
        "disaster_type": disaster_type,
        "source": source,
        "region": region,
        "timestamp": datetime.utcnow().isoformat(),
        "data": data
    }

    try:
        response = requests.post(BACKEND_URL, json=payload, timeout=10)
        print(f"[INFO] Sent {disaster_type} data → {response.status_code}")
        return response.status_code
    except Exception as e:
        print(f"[ERROR] Failed to send data: {str(e)}")
        return None
