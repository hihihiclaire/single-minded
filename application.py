import sqlite3
import time
from db import *
from task import Task
from flask import Flask, render_template, request, g, session

app = Flask(__name__)
DATABASE = 'singleminded.db'

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    tasklist = db_get_tasks()
    print(tasklist)
    return render_template('index.html', tasks=tasklist)

@app.route("/<username>/")
def index_of(username):
    tasklist = db_get_tasks_by_user(username)
    print(tasklist)
    return render_template('index.html', tasks=tasklist)

@app.route("/create", methods=["POST"])
def receive_create():
    print(request.form)
    task = Task(request.form['user'], request.form['title'], request.form['description'], request.form['deadline'], request.form['priority'], request.form['effort'])
    task.save_to_db()
    return "Success! Go back to <a href='/'>Index</a>"

if __name__ == "__main__":
    app.run(debug=True)
    
