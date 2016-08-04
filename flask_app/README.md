##Python Flask App 

####If using virtual env
```
#activate the virtual environment and run the app
$ . venv/bin/activate
(venv) $ export FLASK_APP=main.py
(venv) $ export FLASK_DEBUG=1
(venv) $ flask run
 * Serving Flask app "main"
 * Forcing debug mode on
IN DEBUG MODE, SETTING CACHE TIMEOUT TO 1
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
IN DEBUG MODE, SETTING CACHE TIMEOUT TO 1
 * Debugger is active!
 * Debugger pin code: 315-276-825
...
```

####API
```
/ : base url with map
/json?w=<west>&s=<south>&e=<east>&n=<north>&type=<type> : return geoJson with contours and centerpoints whose
  centers are included in the bounding box specified by w,s,e,n parameters.
  These latitudes and longitudes should be in decimal degrees.
  The type should be (at this point just) am and fm, for what kind of contours to specify
/geocode?q=<query> : takes a URI-encoded address as a query and returns a lat,lng of the address, 
  depends on the accuracy of the OSM geocoding api
/callsign?cs=<callsign>&type=<type> returns the lat,lng of the given callsign for the given callsign for the given service type (am and fm right now). If there is an inexact match, gives the first one in the database; ie. 'AMU' or 'amu' match WAMU and KAMU so only one is given.
```











