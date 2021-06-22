from datetime import datetime
from datetime import date

from suntime import Sun
from geopy import Nominatim
import json

from wallpapers import wallpapers

def get_data(place):

    #* Create a locator
    geolocator = Nominatim(user_agent="geoapiExercises")

    #* Get location for a place
    location = geolocator.geocode(place)

    #* Get latitude and longitude
    latitude = location.latitude
    longitude = location.longitude

    #* Get sun object
    sun = Sun(latitude, longitude)

    #* Find current time
    now = datetime.now()

    #* Calculate time
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    current_day = now.strftime("%d")

    #* Get time zone 
    time_zone = date(int(current_year), int(current_month), int(current_day))

    #* return sunrise and sunset
    sun_rise = sun.get_local_sunrise_time(time_zone)
    sun_dusk = sun.get_local_sunset_time(time_zone)

    sun_data = {
        'sunrise' : sun_rise.strftime("%H:%M"),
        'sunset': sun_dusk.strftime("%H:%M")
    }
    return sun_data



sun = get_data("belgrade")
