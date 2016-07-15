#!/bin/bash

if [[ "$VIRTUAL_ENV" == "" ]] 
then
  . venv/bin/activate;
fi
export FLASK_APP=first_app.py
export FLASK_DEBUG=1
flask run
