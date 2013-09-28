from flask import g
import sqlite3

DATABASE = 'singleminded.db'

def insert(table, fields=(), values=()):
    db = get_db()
    cur = db.cursor()
    query = 'INSERT INTO %s (%s) VALUES (%s)' % (
        table,
        ', '.join(fields),
        ', '.join(['?'] * len(values))
    )
    cur.execute(query, values)
    db.commit()
    id = cur.lastrowid
    cur.close()
    return id

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def db_get_tasks():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM tasks")
    return cur.fetchall()

def db_get_tasks_by_user():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM tasks")
    return cur.fetchall()

def db_add_task(task):
    cur = get_db().cursor()
    cheep_info = (name, t, cheep)
    cur.execute("INSERT INTO tasks VALUES (?, ?, ?)", task.get_values())
    get_db().commit()
    
if __name__ == "__main__":
    print("initializing database:", DATABASE)
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS tasks")
    c.execute("CREATE TABLE tasks (id integer primary key autoincrement, userid, title, description, timestamp, deadline, priority, effort, ordinality, complete)")
    c.execute("INSERT INTO tasks (userid, title, description, timestamp, deadline, priority, effort, ordinality, complete) VALUES (0, 'buy milk', '', '9-28-13', '9-29-13', 1, 2, 0, 0)")
    c.execute("SELECT * FROM tasks")
    print(c.fetchall())
    conn.commit()
    conn.close()
