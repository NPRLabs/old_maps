import sqlite3


db = sqlite3.connect('test.db')


c = db.cursor()

'''

print c.lastrowid
'''

c.execute('''CREATE TABLE execmany
             (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, password TEXT)''')
c.execute('''CREATE TABLE onecommit
             (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, password TEXT)''')
c.execute('''CREATE TABLE multcommits 
             (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, password TEXT)''')
db.commit()
db.close()
