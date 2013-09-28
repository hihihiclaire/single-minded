import sqlite3
import time
from db import *
from flask import Flask, render_template, request, g

app = Flask(__name__)
DATABASE = 'singleminded.db'

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    cheeps = db_read_cheeps()
    return render_template('index.html', cheeps=cheeps)

@app.route("/api/cheep", methods=["POST"])
def receive_cheep():
    print(request.form)
    db_add_cheep(request.form['name'], request.form['cheep'])
    return "Success! Go back to <a href='/'>Index</a>"

if __name__ == "__main__":
    app.run(debug=True)
    
