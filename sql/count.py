import sqlite3
               # org INTEGER, UNIQUE(hours, fid, da)
import sys

db = sqlite3.connect('fcc.db')


c = db.cursor()

c.execute("SELECT COUNT(*) FROM {}".format(sys.argv[1]))
print c.fetchall()
'''for row in c.execute("SELECT * FROM tv"):
    print row
'''
'''
c.execute("SELECT fid, appid, da, hours, power, COUNT(*)  FROM {} GROUP BY appid, da, hours, power HAVING COUNT(*) > 1".format(sys.argv[1]))
print c.fetchall()
for row in c.execute("SELECT * FROM tv"):
    print row

'''
'''
print 'THIS ONE'
c.execute("SELECT fid, fn, appid, asrn, COUNT(*)  FROM {} GROUP BY fn, fid, appid, asrn HAVING COUNT(*) > 1".format(sys.argv[1]))
print c.fetchall()
'''
'''for row in c.execute("SELECT * FROM tv"):
    print row
'''
db.commit()
db.close()
