# scheduler.py
import time

from earthquakes_usgs import fetch_earthquakes
from rainfall_openmeteo import fetch_rainfall
from floods_gfms import fetch_floods
from droughts_chirps import fetch_droughts
from landslides_nasa import fetch_landslides
from cyclones_gdacs import fetch_cyclones
from heatwaves_openmeteo import fetch_heatwaves
from glofs_glacial import fetch_glofs
from winterstorms_openmeteo import fetch_winterstorms
from wildfires_firms import fetch_wildfires
from tsunamis_ptwc import fetch_tsunamis

def run_scheduler():
    while True:
        fetch_earthquakes()
        fetch_rainfall()
        fetch_floods()
        fetch_droughts()
        fetch_landslides()
        fetch_cyclones()
        fetch_heatwaves()
        fetch_winterstorms()
        fetch_wildfires()
        fetch_tsunamis()

        # Run every 10 minutes
        time.sleep(600)

if __name__ == "__main__":
    run_scheduler()
