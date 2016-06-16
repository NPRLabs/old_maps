import sqlite3

def create_table():
    db = sqlite3.connect('fcc.db')
    c = db.cursor()
    c.execute('''CREATE TABLE fm
                (id INTEGER PRIMARY KEY, callsign TEXT, freq REAL, service TEXT, channel TEXT, da TEXT, 
                    class TEXT, status TEXT, city TEXT, state TEXT, country TEXT, fn TEXT, 
                    erph REAL, erpv REAL, haath REAL, haatv REAL, fid INTEGER, lat REAL, 
                    long REAL, name TEXT, dkm REAL, dmi REAL, ddeg REAL, 
                    rcamslh REAL, rcamslv REAL, daid REAL, dapr REAL, asrn REAL, 
                    h REAL, appid INTEGER, org INTEGER, member TEXT
                )''')

    c.execute('''CREATE TABLE am
                (id INTEGER PRIMARY KEY, callsign TEXT, freq REAL, service TEXT, da TEXT, hours TEXT, 
                    usclass TEXT, iclass TEXT, status TEXT, city TEXT, state TEXT, 
                    country TEXT, fn TEXT, power REAL, fid INTEGER, lat REAL, long REAL, 
                    name TEXT, dkm REAL, dmi REAL, ddeg REAL, appid INTEGER,
                    org INTEGER, member TEXT

                )''')

                   # org INTEGER, UNIQUE(hours, fid, da)
    c.execute('''CREATE TABLE tv
                (id INTEGER PRIMARY KEY, callsign TEXT, service TEXT, channel TEXT, da TEXT, freqoff TEXT, 
                    tvzone TEXT, tvstatus TEXT, city TEXT, state TEXT, 
                    country TEXT, fn TEXT, erp REAL, haat REAL, fid INTEGER, lat REAL, 
                    long REAL, name TEXT, dkm REAL, dmi REAL, ddeg REAL, rcamsl REAL, 
                    polar TEXT, daid REAL, dapr REAL, asrn REAL, 
                    h REAL, appid INTEGER, virtchan INTEGER, org INTEGER, member TEXT
                )''')


    c.execute('''CREATE TABLE orgs
                (id INTEGER PRIMARY KEY, parentcallsign TEXT, parentid INTEGER 
                )''')


    db.commit()
    db.close()
