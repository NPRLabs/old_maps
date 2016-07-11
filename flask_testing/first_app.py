from flask import Flask, render_template, url_for, jsonify, g
import json
import combine_contours
import sqlite3

app = Flask(__name__)

# sqlite3 database
DATABASE = 'fcc.db'

# make the database accessible by get_db()
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

#simply load the
@app.route('/') 
@app.route('/<name>') #deprecated testing
def root_map(name=None):
    '''simply load the leaflet js and set up the map''' 
    return render_template('first.html', name=name)

@app.route('/json/<west>/<south>/<east>/<north>')
def give_json(west=None, south=None, east=None, north=None):
    '''given a bounding box, 
       load the appropriate contours from the data base and return them as
       a single (geo)JSON object'''
       
    w = float(west)
    s = float(south)
    e = float(east)
    n = float(north)
    
    # NEED TO THINK ABOUT SESSIONS TO keep track of current ones
    # would need to work with leaflet tho
    # do we just add new ones?
    # does it redraw ones that already exist?
    #also bigger bounds, how do we track those?
    
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
    '''close database on ending of flask run'''
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


