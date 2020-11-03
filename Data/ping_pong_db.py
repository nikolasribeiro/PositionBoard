import sqlite3

def participant_data():
    start = sqlite3.connect("ping_pong.db")
    start.execute("CREATE TABLE IF NOT EXISTS ping_pong(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    start.commit()
    start.close()

def add_name(name):
    start = sqlite3.connect("ping_pong.db")
    pointer = start.cursor()
    test = pointer.execute("INSERT INTO ping_pong(id, name) VALUES (NULL,?)",(name,),)
    print(test)
    start.commit()
    start.close()

def get_participant():
    start = sqlite3.connect("ping_pong.db")
    pointer = start.cursor()
    pointer.execute("SELECT * FROM ping_pong")
    row = pointer.fetchall()
    start.close()
    return row

