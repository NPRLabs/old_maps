import sys
import sqlite3
import json
from collections import OrderedDict


def load_json(d):
    '''helper to load individual json'''
    return (json.loads(d[0]),d[1])

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
        OrderedDict([
            ("geometry",make_into_pol(con[0]['features'][1]['geometry'])),
            ("type","Feature"),
            ("properties",dict(con[0]['features'][0]["properties"], 
                                            **{"memberstatus":con[1]})),
            ("id", i+1)])
                        for i,con in enumerate( map(load_json, cur) ) ] 

    d = OrderedDict([('features',features_list), ("type","FeatureCollection")])
    database.commit()
    return d

if __name__ == '__main__':
    db = sqlite3.connect('fcc.db')
    cur = db.cursor()

    d = combine_json_qgis(db, '''SELECT con,member FROM {} WHERE con NOT NULL'''.format(sys.argv[1]))
    #print 'var test_json = '
    print json.dumps(d)
    db.close()


