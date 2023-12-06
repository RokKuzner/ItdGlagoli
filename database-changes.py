import sqlite3

conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
c = conn.cursor()

c.execute("DELETE FROM verbs WHERE infinitive=?", ("offendere",))
conn.commit()