import argparse
import requests
import time
import sys
import math
from kml_to_geojson import parse_kml_to_dict, write_to_string
import sqlite3
import json
from lxml import html


def load_from_website_am(callsign,ant,appid,freq,city,state):

    payload = {
    'appid':appid,
    'antsysid':ant,
    'call':callsign,
    'freq':freq,
    'contour':'0.5',
    'city':city,
    'state':state,
    '.txt':''
    }

    url = 'https://transition.fcc.gov/fcc-bin/{}'.format('contourplot.kml')
    chunk_size = 1024
    r = requests.get(url, params=payload,stream=True)
    kml = r.text
    ses = kml.splitlines()
    return ses[0] + '\n<kml>' + '\n'.join(ses[2:])

def load_ant(fid):

    payload = {
    'arn':fid,
    'list':'0'
    }

    url = 'https://transition.fcc.gov/fcc-bin/amq'
    chunk_size = 1024
    r = requests.get(url, params=payload,stream=True)
    tree = html.fromstring(r.content)
    span = tree.xpath('.//span[contains(text(), "CDBS Ant. System ID")]')
    if len(span) > 0:
        return span[0].text.split(':')[1].strip()
    else:
        return None
        
def load_am_contour(fid, callsign,ant,appid,freq,city,state):
    ant = load_ant(fid)
    kml = load_from_website_am(callsign,ant,appid,freq,city,state)
    s = write_to_string(parse_kml_to_dict(kml, None), None)
    
    if not s:
        print 'bad contour, not committing'
        return None
    return s
    


if __name__ == '__main__':
    db = sqlite3.connect('fcc.db')
    cur = db.cursor()

    cur.execute('''SELECT id,callsign,appid,freq,city,state,fn FROM {} WHERE
                    member NOT NULL and con ISNULL and status=? and service=?'''.format(sys.argv[1]),
                        ('LIC', sys.argv[1].upper()))

    to_search = cur.fetchall()
    print 'Total: ' + str(len(to_search))
    for i, c in enumerate(to_search):
        print c
        
        l = c[6].split('-')
        if len(l) != 2:
            print 'bad vale'
            continue


        fid = l[1].strip()
        ant = load_ant(fid)
        if not ant:
            print 'No antenna possible'
            continue
    


        kml = load_from_website_am(c[1],ant,c[2],c[3],c[4].replace(' ','_').upper(),c[5])
        s = write_to_string(parse_kml_to_dict(kml, None), None)
        if not s:
            print 'bad contour, not committing'
            continue
        #print s
        
        cur.execute('''UPDATE am SET con=? WHERE id=?''', (s, c[0]))
        print 'committing'
        db.commit()

    
    db.close()
  



