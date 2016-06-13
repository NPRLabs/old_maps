import sqlite3


db = sqlite3.connect('fcc.db')


c = db.cursor()

'''

print c.lastrowid
'''

c.execute('''CREATE TABLE fm
            (id INTEGER PRIMARY KEY, callsign TEXT, da TEXT, channel TEXT, class TEXT, service TEXT, 
                freq REAL, status TEXT, city TEXT, state TEXT, country TEXT, fn TEXT, 
                fid INTEGER, erph REAL, erpv REAL, haath REAL, haatv REAL, lat REAL, 
                long REAL, name TEXT, rcamslh REAL, rcamslv REAL, daid REAL, dapr REAL, asrn REAL, 
                h REAL, appid INTEGER, dmi REAL, dkm REAL, ddeg REAL,
                org INTEGER
            )''')

c.execute('''CREATE TABLE am
            (id INTEGER PRIMARY KEY, callsign TEXT, da TEXT, usclass TEXT, iclass TEXT, 
                service TEXT, hours TEXT, freq REAL, status TEXT, city TEXT, state TEXT, 
                country TEXT, fn TEXT, fid INTEGER, power REAL, lat REAL, long REAL, 
                name TEXT, appid INTEGER, dmi REAL, dkm REAL, ddeg REAL,
                org INTEGER
            )''')

c.execute('''CREATE TABLE tv
            (id INTEGER PRIMARY KEY, callsign TEXT, da TEXT, channel TEXT, tvzone TEXT, 
                tvstatus TEXT, service TEXT, freqoff REAL, status TEXT, city TEXT, state TEXT, 
                country TEXT, fn TEXT, fid INTEGER, erp REAL, haat REAL, lat REAL, 
                long REAL, name TEXT, rcamsl REAL, polar TEXT, daid REAL, dapr REAL, asrn REAL, 
                h REAL, appid INTEGER, dmi REAL, dkm REAL, ddeg REAL, virtchan INTEGER,
                org INTEGER
            )''')




db.commit()
db.close()
