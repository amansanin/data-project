import sqlite3

def get_connection():
    conn=sqlite3.connect("student.db")
    return conn

def create_table():
    conn = get_connection()

    conn.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL
                )''')

    conn.commit()
    conn.close()