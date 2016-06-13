import sqlite3


db = sqlite3.connect('fcc.db')


c = db.cursor()

c.execute("SELECT COUNT(*) FROM fm")
print c.fetchall()

for row in c.execute("SELECT * FROM fm"):
    print row


db.commit()
db.close()
