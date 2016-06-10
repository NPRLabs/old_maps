import sqlite3
import sys


db = sqlite3.connect('test.db')


c = db.cursor()

c.execute("SELECT * FROM {}".format(sys.argv[1]))
print c.fetchall()



db.commit()
db.close()
