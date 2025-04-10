# database.py
import sqlite3
from datetime import date

DB_NAME = "habits.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER,
            date_completed DATE,
            UNIQUE(habit_id, date_completed),
            FOREIGN KEY(habit_id) REFERENCES habits(id)
        )
    ''')
    conn.commit()
    conn.close()

def add_habit(name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO habits (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

def get_habits():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM habits")
    habits = c.fetchall()
    conn.close()
    return habits

def mark_completed(habit_id):
    today = date.today()
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO completions (habit_id, date_completed) VALUES (?, ?)", (habit_id, today))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

def get_completions(habit_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT date_completed FROM completions WHERE habit_id = ?", (habit_id,))
    dates = [row[0] for row in c.fetchall()]
    conn.close()
    return dates
