from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
import sqlite3

@app.route('/')
@app.route('/index')
def index():
    return render_template(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login for user {form.username} success')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)



@app.route('/mine', methods=['GET'])
def mine():
    conn = sqlite3.connect('lab2.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM company")
 
    rows = cur.fetchall()
 
    conn.close()
    return render_template('allrecords.html',output=rows)