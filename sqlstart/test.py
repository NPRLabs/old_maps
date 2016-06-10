import sqlite3
# used this tutorial: http://pythoncentral.io/introduction-to-sqlite-in-python/

db = sqlite3.connect('test.db')


c = db.cursor()

# create the first table

#c.execute('''CREATE TABLE users 
#             (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)''')

c.execute('''SELECT id FROM users WHERE email=?''',('yes.txt2',))
val = c.fetchone()[0]
print 'type:{}'.format(type(val))
print 'email:yes.txt2 id={}'.format(val);


# now update the entry who's id we got
# this is kindof roundabout but its practice (ALSO this should be ''' comment

c.execute('''UPDATE users SET name=? where id = ?''', (

db.commit()
db.close()
