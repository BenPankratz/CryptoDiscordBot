import sqlite3

def initialize_database():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    for statement in CREATE_TABLE_STATEMENTS:
        cursor.execute(statement)
    conn.commit()
    conn.close()

def insert_coin(username, coin):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Check if the user already has a coin set
    cursor.execute("SELECT * FROM user_coins WHERE username = ?", (username))
    if cursor.fetchone():
        # Update the existing coin
        cursor.execute("UPDATE user_coins SET coin = ? WHERE username = ?", (coin, username))
    else:
        # Insert new user and coin
        cursor.execute("INSERT INTO user_coins (username, coin) VALUES (?, ?)", (username, coin))

    conn.commit()
    conn.close()

def query_data():
    # Query data from the database
    # ...
