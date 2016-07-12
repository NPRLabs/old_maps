##Python Flask App 

####if using virtual env
```
#activate the virtual environment and run the app
$ . venv/bin/activate
(venv) $ export FLASK_APP=first_app.py
(venv) $ export FLASK_DEBUG=1
(venv) $ flask run
 * Serving Flask app "first_app"
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
/json/<west>/<south>/<east>/<north> : return geoJson with contours and centerpoints whose
  centers are included in the bounding box specified
```











