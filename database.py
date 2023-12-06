import sqlite3, random

conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
c = conn.cursor()

def get_all_verbs():
    c.execute("SELECT * FROM verbs")
    return c.fetchall()

def get_verb_by_infinitive(verb:str):
    c.execute("SELECT * FROM verbs WHERE infinitive=?", (verb,))
    return c.fetchone()

def get_random_verb():
    c.execute("SELECT * FROM verbs")
    verbs = c.fetchall()
    return verbs[random.randint(0, len(verbs)-1)]

def get_shuffled_verbs():
    c.execute("SELECT * FROM verbs")
    verbs = c.fetchall()
    random.shuffle(verbs)
    return verbs

def add_verb(infinitive:str, FrstPrsnPast:str, before:str):
    c.execute("INSERT INTO verbs VALUES(?, ?, ?)", (infinitive, FrstPrsnPast, before))
    conn.commit()

#print(get_verb_by_infinitive("fare"))