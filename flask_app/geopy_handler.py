from geopy.geocoders import Nominatim
# OSM geocoder
import sys


def get_location(query):
    gl = Nominatim()
    loc = gl.geocode(query)
    return str(loc.latitude) + ', ' + str(loc.longitude) 
