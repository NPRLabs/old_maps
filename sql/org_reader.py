import argparse
import csv
import sqlite3
import sys
import random
import time
import sys
import math

#c.execute(UPDATE {} SET member=? WHERE callsign LIKE ?

def update_org(db, c, parent_callsign, table, id_to_update, status):
    c.execute("SELECT * FROM orgs WHERE parentcallsign LIKE ?", (parent_callsign+'%',))
    orgs = c.fetchall()
    if len(orgs) == 1:
        c.execute("UPDATE {} SET org=?, member=? WHERE id=?"
            .format(table), (orgs[0][0], status, id_to_update,))
        c.execute("UPDATE {} SET org=? WHERE callsign=? or callsign=?"
            .format(table), (orgs[0][0], parent_callsign.split('-')[0], parent_callsign))
    elif len(orgs) == 0:
        #make new org entry
        c.execute("INSERT INTO orgs VALUES(?,?,?)", (None, parent_callsign, None))

        #get id
        c.execute("SELECT * FROM orgs WHERE parentcallsign LIKE ?"
        .format(table), (parent_callsign+'%',))
        org = c.fetchone()
        print org
        print parent_callsign
        print 'AAA{}AAA'.format(table)
        c.execute("UPDATE {} SET org=?, member=? WHERE id=?"
            .format(table), (org[0], status, id_to_update,))
        #also have to set the parent's org
        c.execute("UPDATE {} SET org=? WHERE callsign=? or callsign=?"
            .format(table), (org[0], parent_callsign.split('-')[0], parent_callsign))
        
    else:
        #shouldn't happen
        print "ORG TABLE MESSED UP"
        pass

    #db.commit()
    


def set_orgs():
    db = sqlite3.connect('fcc.db')
    c = db.cursor()
    with open('data/orgs.csv') as csvfile:
        list_reader = csv.DictReader(csvfile)
        for line in list_reader:
            splitup = line['associate calletter'].split('-')
            c.execute("SELECT * FROM {} WHERE callsign LIKE ?"
                .format(splitup[1].lower()), (splitup[0]+'%',))
            output = c.fetchall()
            if len(output) == 1:
                ''' EXACTLY ONE MATCH GOOD'''
                print "1: one callsign match"
                update_org(db, c, line['parent calletter'], splitup[1].lower().strip(), output[0][0]
                        , line['stationstatus'])
            elif len(output) > 1:
                c.execute('SELECT * FROM {} WHERE callsign LIKE ? and service=? and status=?'''
                    .format(splitup[1].lower().strip()), (splitup[0]+'%',splitup[1].strip(),'LIC'))

                new_output = c.fetchall()
                #gonna need to update both
                if len(new_output) > 1:

                    '''
                    s = "SELECT * FROM {} WHERE callsign=? and service=? and status=?"
                        .format(splitup[1].lower().strip())
                    c.execute(s, (splitup[0],splitup[1].strip(),'LIC'))
                    o = c.fetchall()
                    if len(o) == 0:
                        c.execute('SELECT * FROM {} WHERE callsign=? and service=
                            .format(splitup[1].lower().strip()), 
                                (line['associate calletter'],splitup[1].strip()))
                        if len(c.fetchall()) == 0:
                            print 'bad3333'
                    elif len(o) > 1:
                        print len(o)
                        
                        print splitup
                        print 'uh oh'
                        '''
                    '''UPATING FIRST OF THEM'''
                    update_org(db, c, line['parent calletter'], 
                            splitup[1].lower().strip(), new_output[0][0], line['stationstatus'])


                elif len(new_output) == 0:
                    c.execute('SELECT * FROM {} WHERE callsign=? and service=?'''
                        .format(splitup[1].lower().strip()), (splitup[0],splitup[1].strip()))
                    print c.fetchall()
                    print splitup
                    print output
                    print 'bad1'
                else:
                    ''' EXACTLY ONE MATCH GOOD'''
                    print "2: one callsign service and status match"
                    update_org(db, c, line['parent calletter'], 
                            splitup[1].lower().strip(), output[0][0], line['stationstatus'])

            else:
                print "Not in database:{}".format(splitup[0])
                print "What do we do here?"
                print

    db.commit()
    db.close()


if __name__ == '__main__':
    set_orgs()

