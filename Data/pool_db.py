import sqlite3

def participant_data():
    start = sqlite3.connect("pool.db")
    start.execute("CREATE TABLE IF NOT EXISTS pool(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    start.commit()
    start.close()

def add_name(name):
    start = sqlite3.connect("pool.db")
    pointer = start.cursor()
    test = pointer.execute("INSERT INTO pool(id, name) VALUES (NULL,?)",(name,),)
    print(test)
    start.commit()
    start.close()

def get_participant():
    start = sqlite3.connect("pool.db")
    pointer = start.cursor()
    pointer.execute("SELECT * FROM pool")
    row = pointer.fetchall()
    start.close()
    return row
