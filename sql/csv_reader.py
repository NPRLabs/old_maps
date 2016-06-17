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
    db.commit()
    db.close()

if __name__ == '__main__':
    cread()



