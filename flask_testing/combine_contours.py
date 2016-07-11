import sys
import sqlite3
import json


def load_json(d):
    '''helper to load individual json'''
    return (json.loads(d[0]),d[1])

def combine_json(database, sql, w, s, e, n):
    '''get the geojson contours from the database and combine them into one object
    '''
    cur = database.cursor()

    #load every contour
    if not w or not s or not e or not n:
        cur.execute(sql)
    #or load within a bounding box (may want to move sql over here)
    else:
        cur.execute(sql, (w, s, e, n))

    # combine into geojson, with the center point and the contour in a 
    # geometry collection
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


