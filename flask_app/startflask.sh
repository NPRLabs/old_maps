#!/bin/bash

if [[ "$VIRTUAL_ENV" == "" ]] 
then
  . venv/bin/activate;
fi
export FLASK_APP=main.py
export FLASK_DEBUG=1
flask run
