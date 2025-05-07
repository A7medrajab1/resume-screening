# chat_memory.py

import sqlite3
import os
from datetime import datetime

DB_FILE = "chat_memory.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS chatlog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            role TEXT,
            message TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_message(user_id, role, message):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO chatlog (user_id, role, message, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (user_id, role, message, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def get_chat_history(user_id, limit=20):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        SELECT role, message FROM chatlog
        WHERE user_id = ?
        ORDER BY timestamp DESC
        LIMIT ?
    ''', (user_id, limit))
    rows = c.fetchall()
    conn.close()
    # Return history in reverse order (oldest → newest)
    return rows[::-1]

def clear_chat_history(user_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        DELETE FROM chatlog WHERE user_id = ?
    ''', (user_id,))
    conn.commit()
    conn.close()
    
    
if __name__ == "__main__":
    clear_chat_history("demo_user")
    print("Chat history cleared for demo_user.")
    
