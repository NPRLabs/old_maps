import sys
import sqlite3
import json


def load_json(d):
    '''helper to load individual json'''
    return (json.loads(d[0]),d[1])

def combine_json(database, sql, bounds, max_results=10000):
    '''get the geojson contours from the database and combine them into one object
    '''
    cur = database.cursor()

    #load every contour
    if not bounds:
        cur.execute(sql)
    #or load within a bounding box (may want to move sql over here)
    else:
        cur.execute(sql, bounds)

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
                        for i,con in enumerate( map(load_json, cur) ) 
                            if i < max_results] 

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

def make_into_pol(geo_dict):
    geo_dict['type'] = 'Polygon'
    geo_dict['coordinates'] = [ geo_dict['coordinates'] ] 
    return geo_dict

def combine_json_qgis(database, sql):
    '''get the geojson contours from the database and combine them into one object
    '''
    cur = database.cursor()

    #load every contour
    cur.execute(sql)

    # combine into geojson, with the center point and the contour in a 
    # geometry collection
    features_list = [
        {
            "geometry":make_into_pol(con[0]['features'][1]['geometry']),
            "type":"Feature",
            "properties":dict(con[0]['features'][0]["properties"], 
                                            **{"memberstatus":con[1]}),
            "id":i+1}
                        for i,con in enumerate( map(load_json, cur) ) ] 

    d = {"type":"FeatureCollection"}
    d['features'] = features_list
    database.commit()
    return d

if __name__ == '__main__':
    db = sqlite3.connect('fcc.db')
    cur = db.cursor()

    d = combine_json_qgis(db, '''SELECT con,member FROM {} WHERE con NOT NULL'''.format(sys.argv[1]))
    #print 'var test_json = '
    print json.dumps(d)
    db.close()


