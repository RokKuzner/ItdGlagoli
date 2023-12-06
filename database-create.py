import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

VERBS = """
CREATE TABLE IF NOT EXISTS verbs(
infinitive TEXT UNIQUE,
FrstPrsnPast TEXT,
before TEXT
)
"""


c.execute(VERBS)

conn.commit()
conn.close()