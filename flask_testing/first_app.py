from flask import Flask, render_template, url_for, jsonify, g, request, send_file
import json
import combine_contours
import sqlite3

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

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
def root_map():
    '''simply load the leaflet js and set up the map''' 
    return render_template('first.html')

'''
@app.route('/js/leaflet.js')
def give_js():
    return send_file('static/leaflet.js', mimetype='application/javascript')
'''

@app.route('/json')
def give_json():
    '''given a bounding box, 
       load the appropriate contours from the data base and return them as
       a single (geo)JSON object'''
    w = request.args.get('w')
    s = request.args.get('s')
    n = request.args.get('n')
    e = request.args.get('e')
    
       
    w = float(w)
    s = float(s)
    e = float(e)
    n = float(n)
    
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


