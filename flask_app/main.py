from flask import Flask, render_template, url_for, jsonify, g, request, send_file
import json
import combine_contours
import sqlite3

app = Flask(__name__)

# guarantee that the json doesn't waste bandwidth
# might be unneccesary depending on how flask works'''
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# if developing with flask as the web server, then set low cache timeout
# 
if app.debug:
    print 'IN DEBUG MODE, SETTING CACHE TIMEOUT TO 1'
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

# sqlite3 database path
DATABASE = 'fcc.db'

# deprecated, might be required by not-up-to-date browsers
@app.route('/favicon.ico')
def favicon():
    return send_file('static/favicon.ico')
    

# make the database accessible by get_db()
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# simply load the main page
@app.route('/') 
def root_map():
    '''simply load the leaflet js and set up the map''' 
    return render_template('first.html')


# Handle api requests
@app.route('/json')
def give_json():
    '''given a bounding box, 
       load the appropriate contours from the data base and return them as
       a single (geo)JSON object'''
       
    
    max_contours = 35
    #convert to decimal degrees
    w = float(request.args.get('w'))
    s = float(request.args.get('s'))
    n = float(request.args.get('n'))
    e = float(request.args.get('e'))
    
    typ = str(request.args.get('type'))
    if typ == 'am':
        max_contours = 1000
    
    # NEED TO THINK ABOUT SESSIONS TO keep track of current ones
    # would need to work with leaflet tho
    # do we just add new ones?
    # does it redraw ones that already exist?
    #also bigger bounds, how do we track those?
    # ORDER BY erph, erpv DESC


    db = get_db()
    if db is not None:
        d = combine_contours.combine_json(db, 
            '''SELECT con,member FROM {} WHERE con NOT NULL 
            and long > ?
            and lat > ?
            and long < ?
            and lat < ?
            '''.format(typ), (w, s, e, n), max_contours)
        return jsonify(**d)
        
        
        
@app.teardown_appcontext
def close_connection(exception):
    '''close database on ending of flask run'''
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()








