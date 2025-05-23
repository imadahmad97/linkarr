import sqlite3

con = sqlite3.connect("app/instance/link_hisory.db")
cur = con.cursor()
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS link_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        request_type TEXT NOT NULL,
        files TEXT NOT NULL,
        source_dir TEXT NOT NULL,
        target_dir TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
"""
)
con.commit()
