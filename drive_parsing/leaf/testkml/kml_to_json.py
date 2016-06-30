import xml.etree.ElementTree as ET
import datetime as dt
import time
import csv
import json



tree = ET.parse('test.kml')
root = tree.getroot()


i = 0
lis = []
# center point
center = root[0][3]
print center[2][0].text
lon, lat, z = center[2][0].text.split(',')
lis.append({"type":"Feature", "id":i+1, "properties":{"name":center[0].text, "description":center[1].text},
            "geometry":{"type":"Point",
            "coordinates":[float(lon),float(lat), float(z)]}})

i+=1


linemark = root[0][5]
cs = []
for coords in linemark[3][2].text.splitlines():
    if not coords:
        continue
    splitup = coords.split(',') 
    if len(splitup) < 3:
        continue
    lon, lat, z = splitup
    cs.append([float(lon), float(lat), float(z)])

lis.append({"type":"Feature", "id":i+1, "properties":{"name":center[0].text},
            "geometry":{"type":"LineString",
            "coordinates":cs}})

d = {"type":"FeatureCollection", "features":lis}

with open('ownparse.js', 'w') as jfile:
    jfile.write('var new_test = \n')

with open('ownparse.js', 'a') as jfile:
    json.dump(d, jfile, indent=2)
