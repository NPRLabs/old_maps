import argparse



parser = argparse.ArgumentParser(description='small tool')


parser.add_argument('which', choices=['tv', 'am', 'fm'])

group = parser.add_mutually_exclusive_group()
group.add_argument('-r', '--reload_from_source', action='store_true')
group.add_argument('-f', '--load_file', default='', dest='filename')

parser.add_argument('-c', '--call_sign', default='', dest='call_sign')
import requests
import time

r = requests.get('https://api.github.com/events')

payload = {'call':'',
'arn':'',
'state':'',
'city':'',
'freq':'0.0',
'fre2':'107.9',
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

chunk_size = 1024
r = requests.get('https://transition.fcc.gov/fcc-bin/fmq', params=payload, stream=True)
print r.url
for line in r.iter_lines(chunk_size):
  #  print (' '.join(line.split())).replace(' ', ',')
  if line: 
    for entry in filter(lambda l: 'KSFH' in l, line.split(' ')):
      if entry:
        print entry
