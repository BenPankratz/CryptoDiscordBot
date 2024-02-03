import sqlite3
import json


def initialize_database():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Create the users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT)''')

    # Create the coins table
    cursor.execute('''CREATE TABLE IF NOT EXISTS coins
                    (user_id INTEGER, coin TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(id))''')

    conn.commit()
    cursor.close()
    conn.close()

def insert_user(username):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Insert new user
    cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
    user_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return user_id

def insert_coin(username, coin):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Check if the user exists, if not, add them to the database
    user_id = cursor.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
    if not user_id:
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        user_id = cursor.lastrowid
    else:
        user_id = user_id[0]

    # Insert coin for a user
    cursor.execute("INSERT INTO coins (user_id, coin) VALUES (?, ?)", (user_id, coin))

    conn.commit()
    conn.close()

def get_user_coins(username):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Retrieve user ID based on username
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    user_id = cursor.fetchone()

    if user_id:
        # Retrieve coins associated with the user
        cursor.execute("SELECT coin FROM coins WHERE user_id = ?", (user_id[0],))
        coins = [row[0] for row in cursor.fetchall()]
        conn.close()
        return coins
    else:
        # If user is not found, add them to the database
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        user_id = cursor.lastrowid

        conn.commit()
        conn.close()

        print(f"User added to the database: {username}")

        return []


def query_data():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Query data from the database
    cursor.execute("SELECT u.username, c.coin FROM users u LEFT JOIN coins c ON u.id = c.user_id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


