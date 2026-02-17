import sqlite3

DB_NAME = "engine.db"

def get_conn():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS workflow_runs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        step_name TEXT,
        status TEXT,
        result TEXT
    )
    """)
    conn.commit()
    conn.close()
