import requests
import schedule
import time
from plyer import notification
import pytz
from datetime import datetime

# https://www.youtube.com/watch?v=FRIyIlsHUXM&t=15s


def get_weather():
    api_key = "3008d41862772406dd614cc6a679ba67"
    lat = "40.90"
    lon = "73.77"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "lat=" + lat + "&lon=" + lon + "&appid=" + api_key

    response = requests.get(complete_url)
    data = response.json()
    
    if data['cod'] != "404":
        main = data["main"]
        current_temperature = main["temp"]

        return current_temperature

get_weather()

