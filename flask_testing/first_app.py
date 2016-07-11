from flask import Flask, render_template, url_for, jsonify, g
import json
import combine_contours
import sqlite3

app = Flask(__name__)
DATABASE = 'fcc.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template('first.html', name=name)

@app.route('/json/<west>/<south>/<east>/<north>')
def give_json(west=None, south=None, east=None, north=None):
    w = float(west)
    s = float(south)
    e = float(east)
    n = float(north)
    db = get_db()
    if db is not None:
        d = combine_contours.combine_json(db, 
            '''SELECT con,member FROM fm WHERE con NOT NULL 
            and long > ?
            and lat > ?
            and long < ?
            and lat < ?
            ''', w, s, e, n)
        return jsonify(**d)
        
        
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


