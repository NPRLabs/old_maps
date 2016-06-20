import argparse
import csv
import sqlite3
import sys
import random
import time
import sys
import math

def update_member_sql(table):
    s='''UPDATE {} SET member=? WHERE callsign LIKE ?'''.format(table)
    return s


s='''SELECT * FROM tv WHERE callsign LIKE ?'''
def update_tv_sql():
    s='''UPDATE tv SET lictype=?, joint=? WHERE callsign LIKE ?'''
    return s

def cread():
    db = sqlite3.connect('fcc.db')
    c = db.cursor()
    with open('data/full_list.csv') as csvfile:
        list_reader = csv.DictReader(csvfile)
        for line in list_reader:
            stat = line['stationstatus']
            splitup = line['calletter'].split('-')
            if splitup[0] == 'WILL':
                print splitup
            c.execute(update_member_sql(splitup[1].lower()), (stat, splitup[0]+'%'))


    with open('data/tv.csv') as tvcsv:
        reader = csv.DictReader(tvcsv)
        for line in reader:
            stat = line['Joint Licensee?']
            typ = line['Licensee type']
            splitup = line['Station'].split()
            if len(splitup) == 2:
                c.execute(s, (splitup[0]+'%',))
                c1 = c.fetchall()
                c.execute(s, (splitup[1].strip('()')+'%', ))
                c2 = c.fetchall()
                if len(c1) == 0 and len(c2) == 0:
                    print "Problem with, not in fcc as callsign:{}".format(splitup)
                else:
                    c.execute(update_tv_sql(), (typ, stat, splitup[0]+'%'))
                    c.execute(update_tv_sql(), (typ, stat, splitup[1].strip('()')+'%'))
            else:
                c.execute(s, (splitup[0]+'%', ))
                c1 = c.fetchall()
                if len(c1) == 0:
                    print "Problem with, not in fcc as callsign:{}".format(splitup)
                else:
                    c.execute(update_tv_sql(), (typ, stat, splitup[0]+'%'))

                        
            

    db.commit()
    db.close()

if __name__ == '__main__':
    cread()



