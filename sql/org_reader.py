import argparse
import csv
import sqlite3
import sys
import random
import time
import sys
import math

if __name__ == '__main__':
    db = sqlite3.connect('fcc.db')
    c = db.cursor()
    with open('data/orgs.csv') as csvfile:
        list_reader = csv.DictReader(csvfile)
        for line in list_reader:
            splitup = line['associate calletter'].split('-')
            c.execute("SELECT * FROM {} WHERE callsign LIKE ?".format(splitup[1].lower()), (splitup[0]+'%',))
            output = c.fetchall()
            if len(output) == 1:
                pass
            elif len(output) > 1:
                #c.execute('''SELECT * FROM {} WHERE callsign=?'''
                 #   .format(splitup[1].lower()), (line['associate calletter'],))
                c.execute('SELECT * FROM {} WHERE callsign LIKE ? and service=? and status=?'''
                        .format(splitup[1].lower().strip()), (splitup[0]+'%',splitup[1].strip(),'LIC'))

                new_output = c.fetchall()
                #gonna need to update both
                if len(new_output) > 1:

                    s = '''SELECT * FROM {} WHERE callsign=? and service=? and status=?'''.format(splitup[1].lower().strip())
                    c.execute(s, (splitup[0],splitup[1].strip(),'LIC'))
                    o = c.fetchall()
                    if len(o) == 0:
                        c.execute('SELECT * FROM {} WHERE callsign=? and service=?'''
                            .format(splitup[1].lower().strip()), (line['associate calletter'],splitup[1].strip()))
                        if len(c.fetchall()) == 0:
                            print 'bad3333'
                    elif len(o) > 1:
                        print len(o)
                        
                        print splitup
                        print 'uh oh'

                elif len(new_output) == 0:
                    c.execute('SELECT * FROM {} WHERE callsign=? and service=?'''
                        .format(splitup[1].lower().strip()), (splitup[0],splitup[1].strip()))
                    print c.fetchall()
                    print splitup
                    print output
                    print 'bad1'
            else:
                print "Not in database:{}".format(splitup[0])

    db.commit()
    db.close()


'''
                stat = line['stationstatus']
                splitup = line['calletter'].split('-')
                if splitup[1] == sys.argv[1].upper():
                c.execute(UPDATE {} SET member=? WHERE callsign LIKE ?
                        .format(sys.argv[1]), (stat, splitup[0]+'%'))
                '''


