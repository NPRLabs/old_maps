##Python Flask App 

####if using virtual env
```
#activate the virtual environment and run the app
$ . venv/bin/activate
(venv) $ export FLASK_APP=first_app.py
(venv) $ flask run
 * Serving Flask app "first_app"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ...
```

####API
```
/ : base url with map
/json/<west>/<south>/<east>/<north> : return geoJson with contours and centerpoints whose
  centers are included in the bounding box specified
```











