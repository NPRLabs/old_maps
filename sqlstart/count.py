import sqlite3


db = sqlite3.connect('fcc.db')


c = db.cursor()

c.execute("SELECT COUNT(*) FROM tv")
print c.fetchall()
'''for row in c.execute("SELECT * FROM tv"):
    print row
'''
db.commit()
db.close()
