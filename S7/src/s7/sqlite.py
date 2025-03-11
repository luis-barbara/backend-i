from contextlib import contextmanager
import sqlite3

@contextmanager
def sql_connection(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    try:
        yield cur
        con.commit()
    finally:
        con.close()

with sql_connection("user_registration.db") as cur:
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    print("Table 'users' created with success")

    users = [
        ('John Doe', 'john.doe@example.com', 'password123'),
        ('Jane Smith', 'jane.smith@example.com', 'password456'),
        ('Alice Brown', 'alice.brown@example.com', 'password789')
    ]

    cur.executemany('''
    INSERT INTO users (name, email, password) VALUES (?, ?, ?)
    ''', users)

    print("Users added successfully")

