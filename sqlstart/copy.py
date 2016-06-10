import sqlite3


db = sqlite3.connect('test.db')


c = db.cursor()

c.execute("SELECT * FROM users")
print c.fetchall()



db.commit()
db.close()
