import sqlite3

def participant_data():
    print("Entro al participant data")
    start = sqlite3.connect("participant.db")
    start.execute("CREATE TABLE IF NOT EXISTS participant(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    start.commit()
    start.close()

def add_name(name):
    start = sqlite3.connect("participant.db")
    pointer = start.cursor()
    test = pointer.execute("INSERT INTO participant(id, name) VALUES (NULL,?)",(name,),)
    print(test)
    start.commit()
    start.close()

def get_participant():
    start = sqlite3.connect("participant.db")
    pointer = start.cursor()
    pointer.execute("SELECT * FROM participant")
    row = pointer.fetchall()
    start.close()
    return row

