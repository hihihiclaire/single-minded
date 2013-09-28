import sqlite3
conn = sqlite3.connect('singleminded.db')
c = conn.cursor()
c.execute("CREATE TABLE tasks (title, description, timestamp, deadline, priority, effort, ordinality)")
c.execute("INSERT INTO tasks VALUES ('buy milk', '', '9-28-13', '9-29-13', 1, 2, 0)")
c.execute("SELECT * FROM tasks")
print(c.fetchall())
conn.commit()
conn.close()
