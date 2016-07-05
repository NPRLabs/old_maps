import argparse
import requests
import time
import sys
import math
from kml_to_geojson import parse_kml_to_dict, write_to_string
import sqlite3
import json



#def check_loc(f, d):
    #return f[
def load_json(d):
    return json.loads(d[0])['features']

if __name__ == '__main__':
    db = sqlite3.connect('fcc.db')
    cur = db.cursor()

    cur.execute('''SELECT con FROM fm WHERE con NOT NULL''')

    # most likely need to optimize
    features_list = [
        {
            "geometry":{"type":"GeometryCollection",
                        "geometries": [ con[0]['geometry'],
                                        con[1]['geometry'] ]},
                        "type":"Feature",
                        "properties":con[0]["properties"],
                        "id":i+1}
                        for i,con in enumerate( map(load_json, cur) )] 
    #print len(features_list)
    #print features_list[0]['geometry']
    #features_list = [item for item in features_list if 'geometries' in item['geometry']]
    #print len(features_list)

    lats = []
    filtered_list = []
    for f in features_list:
        lat = f["geometry"]["geometries"][0]["coordinates"]
        if not lat in lats:
            lats.append(lat)
            filtered_list.append(f)

    
    #print "Features: " + str(len(features_list))
    #print "Filtered: " + str(len(filtered_list))



    d = {"type":"FeatureCollection"}
    d['features'] = filtered_list
    print 'var test_json = '
    print json.dumps(d)

    
db.commit()
db.close()
  



