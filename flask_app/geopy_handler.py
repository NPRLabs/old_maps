from geopy.geocoders import Nominatim
# OSM geocoder
import sys


def get_location(query):
    gl = Nominatim()
    print query
    loc = gl.geocode(query)
    print loc
    return str(loc.latitude) + ', ' + str(loc.longitude) 
