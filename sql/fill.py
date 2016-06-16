import argparse

import sqlite3
import sys
import random
import time
import sys
import math

def setup_args():
    parser = argparse.ArgumentParser(description='small tool')


    parser.add_argument('which', choices=['tv', 'am', 'fm'])
    parser.add_argument('-o', '--output-file', default='', dest='outfile')
    parser.add_argument('-s', '--load_file', default='', dest='filename')
    '''
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', '--reload_from_source', action='store_true')
    group.add_argument('-s', '--load_file', default='', dest='filename')

    group2 = parser.add_mutually_exclusive_group()
    group2.add_argument('-q', '--query', nargs=2, default='', dest='query')
    group2.add_argument('-l', '--listquery', nargs=2, default='', dest='listquery')
    group2.add_argument('-f', '--filter', 
            help='1:field filter by 2: value it must be, 3:new filename', 
                nargs=3, default='', dest='filt')
    '''
    return parser

def format_line(line):
    vals = line.split('|')
    if not vals[0]:
        vals.pop(0)
    return ','.join(map(str.strip,vals))


def lat_to_real(hem, deg, minutes, secs):
    return (float(deg) + float(minutes)/60.0 + float(secs)/3600.0)*(-1 if hem in ('W', 'S') else 1)

def line_read(line, typ):
    l = line.split('|')
    output = [None]
    if typ == 'fm':
        for i, entry in enumerate(l):
            if i in [5, 7]:
                continue
            elif entry == '-':
                output.append(None)
            elif i in [1,13,14,15,16,27,28,29,30,31,35]:
                e = entry.split()
                if e[0] == '-':
                    output.append(None)
                else:
                    output.append(float(entry.split()[0]))
            elif i in [3, 17]:
                output.append(int(entry))
            elif i in (18, 22):
                output.append(lat_to_real(entry, l[i + 1], l[i + 2], l[i + 3]))
            elif i in [19,20,21,23,24,25]  or entry[0] == '\n':
                continue
            else:
                output.append(entry)
        output.append(None)
    if typ == 'am':
        for i, entry in enumerate(l):
            if i in [3, 14, 15, 16] or entry == '\n':
                continue
            elif entry == '-':
                output.append(None)
            elif i in [1,13,27,28,29]:
                e = entry.split()
                if e[0] == '-' or entry == '':
                    output.append(None)
                else:
                    output.append(float(entry.split()[0]))
            elif i in [17, 30]:
                output.append(int(entry))
            elif i in (18, 22):
                output.append(lat_to_real(entry, l[i + 1], l[i + 2], l[i + 3]))
            elif i in [19,20,21,23,24,25]:
                continue
            else:
                output.append(entry)
        output.append(None)
    if typ == 'tv':
        for i, entry in enumerate(l):
            if i in [1, 7, 14, 16] or entry == '\n':
                continue
            elif entry == '-':
                output.append(None)
            elif i in [13,14,15,16,27,28,29,30,35]:
                e = entry.split()
                if entry == '' or e[0] == '-' :
                    output.append(None)
                else:
                    output.append(float(entry.split()[0]))
            elif i in [3, 17]:
                output.append(int(entry))
            elif i in (18, 22):
                output.append(lat_to_real(entry, l[i + 1], l[i + 2], l[i + 3]))
            elif i in [19,20,21,23,24,25]:
                continue
            else:
                output.append(entry)
        output.append(None)
    #deal with org
    output.append(None)
    print output
    o = tuple(output)
    return o

fm_sql = '''INSERT INTO fm VALUES({})'''.format('?,'*31 + '?')
am_sql = '''INSERT INTO am VALUES({})'''.format('?,'*23 + '?')
tv_sql = '''INSERT OR IGNORE INTO tv VALUES({})'''.format('?,'*30 + '?')

def insert_list(db_f, l, sql):
    db = sqlite3.connect(db_f)
    c = db.cursor()

    c.executemany(sql,
            l)
    db.commit()
    db.close()


def fill_file(filename, out, which):
    f = open(filename, 'r')

    sql = None
    if which == 'fm':
        sql = fm_sql
    elif which == 'am':
        sql = am_sql
    elif which == 'tv':
        sql = tv_sql

    list_to_insert = []
    for i, line in enumerate(f):
        if line:
            list_to_insert.append(line_read(line, which))
            if i % 10000 == 0 and i > 0:
                print 'Attempting to insert up to {}'.format(i)
                insert_list(out, list_to_insert, sql)
                list_to_insert = []
            
    # fill last ones
    insert_list(out, list_to_insert, sql)
    f.close()

if __name__ == '__main__':
    parser = setup_args()
    args = parser.parse_args()
    outfile = None
    if args.outfile:
        outfile = args.outfile
    else:
        outfile = 'fcc.db'
    if args.filename:
        filename = args.filename
    else:
        filename = 'data/{}_data.txt'.format(args.which)

    fill_file(filename, outfile, args.which)
  



