import sys
import sqlite3
import csv
from am_contour_dl import load_am_contour
# (fid, callsign,ant,appid,freq,city,state)
# cur.execute('''UPDATE am SET con=? WHERE id=?''', (s, ID))
from fm_contour_dl import load_fm_contour
# (callsign,ant,appid,freq,city,state)
#cur.execute('''UPDATE fm SET con=? WHERE id=?''', (s, ID))


def update_member_sql(db, cur, table, callsign_sql, memberstatus, contour):
    return 
    s='''UPDATE {} SET member=?, con=? WHERE callsign LIKE ?'''.format(table)
    cur.execute(s, (memberstatus, contour, callsign_sql))
    db.commit()


s='''SELECT * FROM tv WHERE callsign LIKE ?'''
def update_tv_sql():
    s='''UPDATE tv SET lictype=?, joint=? WHERE callsign LIKE ?'''
    return s
    
    
def get_contour(cur, table, callsign_sql):
    cur.execute('''SELECT id,callsign,appid,freq,city,state,fn,lat,long FROM {} WHERE
                    callsign LIKE ? and member ISNULL'''.format(table),
                        (callsign_sql,))
    output = cur.fetchall()
    if len(output) == 0:
        return True
    
    if table == 'fm':
        c = output[0]
        (contour, needs_fixing) = load_fm_contour(
                    c[1],c[2],c[3],c[4].replace(' ','_').upper(),c[5])
    elif table == 'am':
        c = output[0]
        (contour, needs_fixing) = load_fm_contour(
                    c[6],c[1],c[2],c[3],c[4].replace(' ','_').upper(),c[5])

    # redundant load, needs refactoring
    testjs = json.loads(contour)
    if testjs['geometries'][0]['geometry']['coordinates'][0] == 0.0 and
        testjs['geometries'][0]['geometry']['coordinates'][1] == 0.0
        return fix_shift(testjs,c[7],c[8])
    return contour
        
def fix_shift(d,lat, lon):
    for i,x in testjs['geometries'][1]['geometry']['coordinates']:
        new_c = [(x[0]+lon), (x[1]+lat)]
        testjs['geometries'][1]['geometry']['coordinates'][i] = new_c
    testjs['geometries'][0]['geometry']['coordinates'] = [lon, lat]


def cread():
    db = sqlite3.connect('fcc.db')
    c = db.cursor()
    with open(sys.argv[1]) as csvfile:
        list_reader = csv.DictReader(csvfile)
        for line in list_reader:
            memberstatus = line['stationstatus']
            splitup = line['calletter'].split('-')
            #am or fm
            table = splitup[1].lower()
            callsign = splitup[0]
            contour = None
            contour = get_contour(c, table, callsign+'%')
            if contour == True:
                #already a member or no data available
                continue
            print "actually updating"
            print callsign
            update_member_sql(c, db, table, callsign+'%', memberstatus, contour)

                        
            

    db.commit()
    db.close()

if __name__ == '__main__':
    cread()



