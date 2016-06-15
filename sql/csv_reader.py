import argparse
import csv
import sqlite3
import sys
import random
import time
import sys
import math

if __name__ == '__main__':
    with open('data/full_list.csv') as csvfile:
        list_reader = csv.DictReader(csvfile)
        for c in list_reader:
            print c['calletter'] 
            print c['stationstatus']
            print



