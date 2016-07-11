import argparse
import time
import sys
import math
import sqlite3
import json



def load_json(d):
    return (json.loads(d[0]),d[1])

def combine_json(database, sql, w, s, e, n):
    cur = database.cursor()

    if not w:
        cur.execute(sql)
        print 'uh oh'
    else:
        cur.execute(sql, (w, s, e, n))

    features_list = [
        {
            "geometry":{"type":"GeometryCollection",
                        "geometries": [ con[0]['features'][0]['geometry'],
                                        con[0]['features'][1]['geometry'] ]},
                        "type":"Feature",
                        "properties":dict(con[0]['features'][0]["properties"], 
                                            **{"memberstatus":con[1]}),
                        "id":i+1}
                        for i,con in enumerate( map(load_json, cur) )] 

    lats = []
    filtered_list = []
    for f in features_list:
        lat = f["geometry"]["geometries"][0]["coordinates"]
        if not lat in lats:
            lats.append(lat)
            filtered_list.append(f)

    



    d = {"type":"FeatureCollection"}
    d['features'] = filtered_list
    database.commit()
    return d

if __name__ == '__main__':
    db = sqlite3.connect('fcc.db')
    cur = db.cursor()

    d = combine_json(db, '''SELECT con,member FROM fm WHERE con NOT NULL''')
    print 'var test_json = '
    print json.dumps(d)
    database.close()


