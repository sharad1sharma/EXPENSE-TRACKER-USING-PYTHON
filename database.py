# database.py

import os
import shutil
import tempfile
import stat
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IS_SERVERLESS = 'VERCEL' in os.environ or 'VERCEL_ENV' in os.environ or bool(os.environ.get('AWS_LAMBDA_FUNCTION_NAME'))

if IS_SERVERLESS:
    DB_NAME = str(Path(tempfile.gettempdir()) / "expense.db")
    orig_db = BASE_DIR / "expense.db"
    # Copy pre-seeded database to writable temporary directory if it doesn't exist yet
    if not os.path.exists(DB_NAME) and orig_db.exists():
        try:
            shutil.copyfile(str(orig_db), DB_NAME)
            try:
                os.chmod(DB_NAME, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
            except Exception:
                pass
        except Exception:
            pass
else:
    DB_NAME = str(BASE_DIR / "expense.db")


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