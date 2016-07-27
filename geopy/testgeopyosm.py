from geopy.geocoders import Nominatim
# OSM geocoder
import sys


gl = Nominatim()
loc = gl.geocode(sys.argv[1])
print loc.address
print loc
print str(loc.latitude) + str(loc.longitude) 
