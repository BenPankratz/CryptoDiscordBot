import sqlite3

def init_db():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    for statement in CREATE_TABLE_STATEMENTS:
        cursor.execute(statement)
    conn.commit()
    conn.close()

def insert_data(name, age):
    # Insert data into the database
    # ...

def query_data():
    # Query data from the database
    # ...
