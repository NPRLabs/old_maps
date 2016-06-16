import argparse
import csv
import sqlite3
import sys
import random
import time
import sys
import math

def cread():
    db = sqlite3.connect('fcc.db')
    c = db.cursor()
    with open('data/full_list.csv') as csvfile:
        list_reader = csv.DictReader(csvfile)
        for line in list_reader:
            print line['calletter'] 
            stat = line['stationstatus']
            splitup = line['calletter'].split('-')
            c.execute('''UPDATE {} SET member=? WHERE callsign LIKE ?'''
                    .format(splitup[1].lower()), (stat, splitup[0]+'%'))
    db.commit()
    db.close()

if __name__ == '__main__':
    cread()



