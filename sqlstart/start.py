import sqlite3


db = sqlite3.connect('test.db')


c = db.cursor()

# create the first table

#c.execute('''CREATE TABLE users 
#             (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)''')

c.execute('''INSERT INTO users(name, phone, email, password)
                            VALUES(?,?,?,?)''', ('gus','123','yes.txt','asdf'))

print c.lastrowid


db.commit()
db.close()
