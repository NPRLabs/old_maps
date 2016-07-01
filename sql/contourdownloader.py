import argparse
import requests
import time
import sys
import math


def format_line(line):
    
        vals = line.split('|')
        if not vals[0]:
            vals.pop(0)
        return '|'.join(map(str.strip,vals))

def load_from_website(callsign,appid,freq,city,state):

    payload = {
    'appid':appid,
    'call':callsign,
    'freq':freq,
    'contour':54,
    'city':city,
    'state':state,
    '.txt':''
    }

    url = 'https://transition.fcc.gov/fcc-bin/{}'.format('contourplot.kml')
    chunk_size = 1024
    r = requests.get(url, params=payload,stream=True)
    kml = r.text
    ses = kml.splitlines()
    kml = ses[0] + '\n<kml>' + '\n'.join(ses[2:])
    print kml

if __name__ == '__main__':
    load_from_website('WNYC-FM',1439113,93.9,'NEW_YORK','NY')

  



