import sqlite3
import sys
import random
import argparse
import requests
import time
import sys
import math

fm_defaults = { 'callsign' : None, 'da' : 'ND', 'channel' : None, 'class' : None,
                'service' : None, 'freq' : None, 'status' : None, 'city' : None, 
                'state' : None, 'country' : None, 'fn' : None, 'fid' : None, 
                'erph' : None, 'erpv' : None, 'haath' : None, 'haatv' : None,
                'lat' : None, 'long' : None, 'name' : None, 'rcamlslh' : None,
                'rcamlslv' : None, 'daid' : None, 'dapr' : None, 'asrn' : None,
                'h' : None, 'appid' : None, 'dmi' : None, 'dkm' : None, 'ddeg' : None, 'org' : None }

am_defaults = { 'callsign' : None, 'da' : 'ND', 'usclass' : None, 'iclass' : None,
                'service' : None, 'hours' : None, 'freq' : None, 'status' : None, 'city' : None, 
                'state' : None, 'country' : None, 'fn' : None, 'fid' : None, 
                'power' : None,'lat' : None, 'long' : None, 'name' : None,
                'appid' : None, 'dmi' : None, 'dkm' : None, 'ddeg' : None, 'org' : None }

tv_defaults = { 'callsign' : None, 'da' : 'ND', 'channel' : None, 'tvzone' : None, 'tvstatus' : None,
                'service' : None, 'freqoff' : None, 'status' : None, 'city' : None, 
                'state' : None, 'country' : None, 'fn' : None, 'fid' : None, 
                'erp' : None, 'haat' : None, 'lat' : None, 'long' : None, 'name' : None, 
                'rcamlsl' : None, 'polar' : None, 'daid' : None, 'dapr' : None, 'asrn' : None,
                'h' : None, 'appid' : None, 'dmi' : None, 'dkm' : None, 'ddeg' : None, 
                'virtchan' : None,'org' : None }
def execmany():
    db = sqlite3.connect('test.db')
    c = db.cursor()
    c.executemany('''INSERT INTO execmany(name, phone, email, password) VALUES(?,?,?,?)''',rand_vals())
    db.commit()
    db.close()


def setup_args():
    parser = argparse.ArgumentParser(description='small tool')


    parser.add_argument('which', choices=['tv', 'am', 'fm'])
    parser.add_argument('-o', '--output-file', default='', dest='outfile')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', '--reload_from_source', action='store_true')
    group.add_argument('-s', '--load_file', default='', dest='filename')

    group2 = parser.add_mutually_exclusive_group()
    group2.add_argument('-q', '--query', nargs=2, default='', dest='query')
    group2.add_argument('-l', '--listquery', nargs=2, default='', dest='listquery')
    group2.add_argument('-f', '--filter', help='1:field filter by 2: value it must be, 3:new filename', nargs=3, default='', dest='filt')

    return parser

def format_line(line):
    
        vals = line.split('|')
        if not vals[0]:
            vals.pop(0)
        return ','.join(map(str.strip,vals))


def call_q(line, value):
    l = line.split(',')
    return value.lower() == l[0].lower()


def freq_q(line, value):
    l = line.split(',')
    return abs(float(value) - float(l[1].split()[0])) < .0001

def type_q(line, value):
    l = line.split(',')
    return l[2] == value

def lic_q(line, value):
    l = line.split(',')
    return l[4] == value

def lat_to_real(hem, deg, minutes, secs):
    return (float(deg) + float(minutes) + float(secs))*(-1 if hem in ('W', 'S') else 1)

def line_read(line, typ):
    print line
    l = line.split('|')
    output = []
    if typ == 'fm':
        for i, entry in enumerate(l):
            if entry[0] == '-':
                output.append(None)
            elif i in [1,13,14,15,16,27,28,29,30,31,35]:
                print entry
                output.append(float(entry.split()[0]))
            elif i in [3, 17]:
                output.append(int(entry))
            elif i in (18, 22):
                output.append(lat_to_real(entry, l[i + 1], l[i + 2], l[i + 3]))
            elif i in [19,20,21,23,24,25]:
                continue
            else:
                output.append(entry)
    #deal with org
    output.append(None)

    return output
                

def query_file(filename, value, option):
    f = open(filename, 'r')
    query_func = None
    if option == 'callsign':
        query_func = call_q
    elif option == 'freq':
        query_func = freq_q

    list_to_insert = []
    for i, line in enumerate(f):
        if line:
            #if query_func(line, value):
               print line_read(line, 'fm')
    f.close()

def filter_by(src, dest, value, option):
    f = open(src, 'r')
    f2 = open(dest, 'w')
    query_func = None
    if option == 'callsign':
        query_func = call_q
    elif option == 'freq':
        query_func = freq_q
    elif option == 'type':
        query_func = type_q
    elif option == 'license':
        query_func = lic_q

    for line in f:
        if line:
#            for entry in filter(lambda l: callsign in l, line.split(',')):
#                if entry:
#                    sys.stdout.write(line)
            if query_func(line, value):
                f2.write(line)
    f.close()
    f2.close()


if __name__ == '__main__':
    parser = setup_args()
    args = parser.parse_args()
    if args.reload_from_source:
        load_from_website(args, args.outfile, args.callsign)
    filename = None
    if args.filename:
        filename = args.filename
    else:
        filename = 'data/{}_data.txt'.format(args.which)
    if args.query:
        print 'good'
        query_file(filename, args.query[1],args.query[0])
    elif args.listquery:
        fl = open(args.listquery[1], 'r')
        print args.listquery
        for line in fl:
            print 'AAA{}AAA'.format(line)
            print 'Query for: {}'.format(line)
            query_file(filename, line.rstrip(), args.listquery[0])
            print 
    elif args.filt:
        print args.filt
        filter_by(filename, args.filt[2], args.filt[1], args.filt[0]) 

  



