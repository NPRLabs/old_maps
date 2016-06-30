import xml.etree.ElementTree as ET
import datetime as dt
import time
import csv
import json

with open('test.csv') as csvfile:
    writer = csv.DictReader(csvfile)
    lis = [{"type":"Feature", "id":i+1, "properties":{"power":float(col['val'])},
            "geometry":{"type":"Point",
            "coordinates":[float(col['longitude']),float(col['latitude'])]}} for i, col in
                                                                            enumerate(writer)]

with open('test.json', 'w') as jfile:
    jfile.write('var fcc_json =\n')

d = {"type":"FeatureCollection", "features":lis}

with open('test.json', 'a') as jfile:
    json.dump(d, jfile, indent=2)



