A toy room booking system
=====
The web application is build with python Flask framwork along with SQLite3 database. It has basic login system since the booking have to be done with authentication. A admin account is created by default, with username: admin, and password: admin. The administrator have the access to directly manipulate team and users. 

## Requirements
1. Python 3.6, recommending [Anaconda](https://anaconda.org/anaconda/python)
2. Install SQLite3 from [Here](http://www.sqlite.org/download.html)
3. Recommend SQLite browser [Available](http://sqlitebrowser.org/)

## Setup
1. Install flask and packages
```
$ pip install flask
$ pip install flask-wtf
$ pip install flask-sqlalchemy
$ pip install flask-migrate
$ pip install flask-login
```
2. Define the project
```
$ export FLASK_APP=lab2.py
```

3. Init the database
```
$ flask db init
```

## Migrating data
1. Run the migration command from the project directory to create tables
```
$ flask db upgrade
```
2. Populate the database with dummy data(if weren't populated after migration)
```
$ python populate.py
```

# Running
1. Run the flask application from the project directory, running on localhost
```
$ flask run
```
2. Open the app in browser: [localhost](http://127.0.0.1:5000/)
