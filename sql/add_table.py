import sqlite3
import sys


db = sqlite3.connect('fcc.db')


c = db.cursor()

'''

print c.lastrowid
'''

c.execute('''CREATE TABLE {}
            (id INTEGER PRIMARY KEY, {})'''.format(sys.argv[1], sys.argv[2])




db.commit()
db.close()
