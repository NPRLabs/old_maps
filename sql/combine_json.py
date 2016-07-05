import argparse
import requests
import time
import sys
import math
from kml_to_geojson import parse_kml_to_dict, write_to_string
import sqlite3
import json




if __name__ == '__main__':
    db = sqlite3.connect('fcc.db')
    cur = db.cursor()

    cur.execute('''SELECT con FROM fm WHERE con NOT NULL''')

    features_list = [feat for con in cur for feat in json.loads(con[0])['features']] 

    d = {"type":"FeatureCollection"}
    d['features'] = features_list
    print 'var test_json = '
    print json.dumps(d)

    
db.commit()
db.close()
  



