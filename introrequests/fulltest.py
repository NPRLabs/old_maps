import argparse
import requests
import time
import sys


def setup_args():
    parser = argparse.ArgumentParser(description='small tool')


    parser.add_argument('which', choices=['tv', 'am', 'fm'])
    parser.add_argument('-o', '--output-file', default='', dest='outfile')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', '--reload_from_source', action='store_true')
    group.add_argument('-f', '--load_file', default='', dest='filename')

    parser.add_argument('-c', '--call_sign', default='', dest='callsign')
    return parser

def load_from_website(args, filename, callsign):
    stdout = (not filename) or filename == '-'
    print 'FILENAME'
    print filename
    f = None
    if not stdout:
        print 'yep'
        f = open(filename, 'wb')

    r = requests.get('https://api.github.com/events')

    payload = {'call':'',
    'arn':'',
    'state':'',
    'city':'',
    'serv':'',
    'vac':'',
    'facid':'',
    'asrn':'',
    'class':'',
    'list':'3',
    'ThisTab':'Results+to+This+Page%2FTab',
    'dist':'',
    'dlat2':'',
    'mlat2':'',
    'slat2':'',
    'NS':'N',
    'dlon2':'',
    'mlon2':'',
    'slon2':'',
    'EW':'W',
    'size':9}

    
    if args.which == 'tv':
        payload['chan'] = '0.0'
        payload['cha2'] = '69'
    elif args.which == 'fm':
        payload['freq'] = '0.0'
        payload['fre2'] = '107.9'
    else:
        payload['freq'] = '530'
        payload['fre2'] = '1700'


    url = 'https://transition.fcc.gov/fcc-bin/{}q'.format(args.which)
    print 'Url to use:{}'.format(url)
    chunk_size = 1024
    r = requests.get(url, params=payload, stream=True)
    print r.url
    count = 0
    for line in r.iter_lines(chunk_size):
        line = (' '.join(line.split())).replace(' ', ',')
        count += 1
        
        if line: 
            if stdout:
                print line
            else:
                f.write(line + '\n')
        print 'Count:{}'.format(count)
        
    if not stdout:
        f.close()


def query_file(filename, callsign):
    f = open(filename, 'r')
    for line in f:
        if line:
            for entry in filter(lambda l: callsign in l, line.split(',')):
                if entry:
                    sys.stdout.write(line)

if __name__ == '__main__':
    parser = setup_args()
    args = parser.parse_args()
    if args.reload_from_source:
        load_from_website(args, args.outfile, args.callsign)
    elif not args.filename:
        filename = 'data/{}_data.txt'.format(args.which)
        query_file(filename, args.callsign)

  



