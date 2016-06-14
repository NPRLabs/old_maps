import sqlite3
import sys

db = sqlite3.connect('fcc.db')


c = db.cursor()

c.execute("SELECT COUNT(*) FROM {}".format(sys.argv[1]))
print c.fetchall()
'''for row in c.execute("SELECT * FROM tv"):
    print row
'''
db.commit()
db.close()
