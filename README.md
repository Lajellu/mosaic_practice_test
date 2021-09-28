# mosaic_practice_test

Test Instructions by Mosaic found here: https://hatchways.notion.site/hatchways/Back-End-Practice-Assessment-0a110db665384575a94d93faab787f0e
To run the software:
1. Download this mosaic_practice_test repository
2. Download the requirements by going through the steps below:

a) `>> python3 --version`
Ensure you have python version 3

b) `>> python3 -m ensurepip --upgrade`

c) `>> pip3 --version`
d) `>> pip3 install Flask`

e) `>> export FLASK_APP=index.py`
To find the main file that Flask should run

f) `>> cd mosaic_practice_test/`

g) `>> flask run`


h) `>> pip3 install pipenv`
i) `>> pipenv --three`
To create a virtual environment that automatically manages the dependencies for the project

j) `>> pipenv install flask`
Flask is one of the dependencies for our virtual environment

Create a folder for the practice source code

k) `>> cd source_code_practice/`
l) `>> touch __init__.py`
To create an empty init file for the module containing the practice source code

m) `>> cd ..`

n) Add the file bootstrap.sh to the mosaic_practice_test folder with these contents
`#!/bin/sh
export FLASK_APP=./source_code_practice/index.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0`


o) `>> chmod +x bootstrap.sh`

p) `>> pip3 install requests`
To install the package to send POST and PUT requests using python, to debug questions 3 and 4

q) `>>  pipenv --three`
So a virtual environment is created for the updated situation

r) `>> ./bootstrap.sh`
This now sets the main file,  runs the virtual environment, and then runs the flask website

s)`>> ​​pip3 install pytest`



3. And to run your application on localhost, run the bootstrap file. It sets the main file,  runs the virtual environment, and then runs the flask website
`>> ./bootstrap.sh`
