import sqlite3
import sys

db = sqlite3.connect('fcc.db')


c = db.cursor()

c.execute("SELECT COUNT(*) FROM {}".format(sys.argv[1]))
print c.fetchall()

'''
c.execute("SELECT * FROM {} WHERE member='Non-Member (NPR)'".format(sys.argv[1]))
print c.fetchall()
'''
c.execute("select * from tv where callsign like 'KSYS%'");
print c.fetchall()

db.commit()
db.close()
