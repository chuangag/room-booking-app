from flask import Flask,render_template
import sqlite3


# Instantiate our Node
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/mine', methods=['GET'])
def mine():
    conn = sqlite3.connect('lab2.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM company")
 
    rows = cur.fetchall()
 
    conn.close()
    return render_template('allrecords.html',output=rows)



if __name__ == '__main__':
    app.debug=True
    app.run(host='127.0.0.1', port=5000)
    