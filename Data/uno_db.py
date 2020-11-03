import sqlite3

def participant_data():
    start = sqlite3.connect("uno.db")
    start.execute("CREATE TABLE IF NOT EXISTS uno(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    start.commit()
    start.close()

def add_name(name):
    start = sqlite3.connect("uno.db")
    pointer = start.cursor()
    test = pointer.execute("INSERT INTO uno(id, name) VALUES (NULL,?)",(name,),)
    print(test)
    start.commit()
    start.close()

def get_participant():
    start = sqlite3.connect("uno.db")
    pointer = start.cursor()
    pointer.execute("SELECT * FROM uno")
    row = pointer.fetchall()
    start.close()
    return row
