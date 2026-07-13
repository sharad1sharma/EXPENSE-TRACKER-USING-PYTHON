# database.py

import sqlite3

DB_NAME = "expense.db"


def get_connection():
    """
    Create and return SQLite database connection.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    """
    Create transactions table if it does not exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            type TEXT NOT NULL CHECK(type IN ('Income', 'Expense')),
            category TEXT NOT NULL,
            amount REAL NOT NULL CHECK(amount >= 0),
            description TEXT
        )
    """)

    conn.commit()
    conn.close()


def execute_query(query, params=()):
    """
    Execute INSERT, UPDATE, DELETE queries.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    conn.commit()
    conn.close()


def fetch_all(query, params=()):
    """
    Execute SELECT query and return all rows.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)
    rows = cursor.fetchall()

    conn.close()
    return rows


def fetch_one(query, params=()):
    """
    Execute SELECT query and return one row.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)
    row = cursor.fetchone()

    conn.close()
    return row


def initialize_database():
    """
    Initialize database.
    """
    create_table()


if __name__ == "__main__":
    initialize_database()
    print("✅ SQLite database initialized successfully.")