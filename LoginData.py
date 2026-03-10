import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'LoginData.db')

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cmd1 = """
CREATE TABLE IF NOT EXISTS users (
    first_name TEXT,
    last_name TEXT,
    email TEXT PRIMARY KEY,
    password TEXT
)
"""
cursor.execute(cmd1)

existing = cursor.execute("SELECT * FROM users WHERE email = 'anshum@gmail.com'").fetchone()
if not existing:
    cursor.execute("""
    INSERT INTO users (first_name, last_name, email, password)
    VALUES ('Anshum', 'Kumar', 'anshum@gmail.com', 'anshum123')
    """)

connection.commit()

ans = cursor.execute("SELECT * FROM users").fetchall()
for i in ans:
    print(i)

print(f"Database created at: {DB_PATH}")
