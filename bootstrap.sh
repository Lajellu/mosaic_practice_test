#!/bin/sh
export FLASK_APP=./source_code_practice/index.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0
