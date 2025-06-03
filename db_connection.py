import sqlite3

def get_connection():
    conn = sqlite3.connect('library.db')
    return conn

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        copies INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

setup_database()
