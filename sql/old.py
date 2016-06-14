import sqlite3


db = sqlite3.connect('test.db')


c = db.cursor()

c.execute("SELECT * FROM execmany")
print c.fetchall()



db.commit()
db.close()
