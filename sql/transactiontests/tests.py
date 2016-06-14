import sqlite3
import sys
import random


def ran():
    return str(random.randint(0, 1000000))

def rand_vals():
    return [(ran(), ran(), ran(), ran()) for i in xrange(10000)]

def execmany():
    db = sqlite3.connect('test.db')
    c = db.cursor()
    c.executemany('''INSERT INTO execmany(name, phone, email, password) VALUES(?,?,?,?)''',rand_vals())
    db.commit()
    db.close()


def onecommit():
    db = sqlite3.connect('test.db')
    c = db.cursor()
    for entry in rand_vals():
        c.execute('''INSERT INTO onecommit(name, phone, email, password) VALUES(?,?,?,?)''', entry)
    db.commit()
    db.close()


def multcommits():
    db = sqlite3.connect('test.db')
    c = db.cursor()
    for entry in rand_vals():
        c.execute('''INSERT INTO multcommits(name, phone, email, password) VALUES(?,?,?,?)''', entry)
        db.commit()
    db.close()


if __name__ == '__main__':
    if sys.argv[1] == 'execmany':
        execmany()
    elif sys.argv[1] == 'onecommit':
        onecommit()
    else:
        multcommits()



