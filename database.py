# database.py

import os
import shutil
import tempfile
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def determine_db_path():
    # Detect serverless or read-only filesystem environment
    serverless_vars = ('VERCEL', 'VERCEL_ENV', 'AWS_LAMBDA_FUNCTION_NAME', 'LAMBDA_TASK_ROOT', 'VERCEL_REGION')
    if any(var in os.environ for var in serverless_vars):
        return str(Path(tempfile.gettempdir()) / "expense.db")

    # Check if local directory is writable
    try:
        test_file = BASE_DIR / ".write_test"
        with open(test_file, "w") as f:
            f.write("1")
        os.remove(test_file)
        return str(BASE_DIR / "expense.db")
    except (OSError, IOError, PermissionError):
        return str(Path(tempfile.gettempdir()) / "expense.db")

DB_NAME = determine_db_path()

def get_connection():
    """
    Create and return SQLite database connection with error recovery.
    """
    global DB_NAME
    # If DB_NAME is in a temp directory and doesn't exist, try copying pre-seeded DB if possible
    if DB_NAME != str(BASE_DIR / "expense.db") and not os.path.exists(DB_NAME):
        orig_db = BASE_DIR / "expense.db"
        if orig_db.exists():
            try:
                shutil.copyfile(str(orig_db), DB_NAME)
            except Exception:
                pass

    try:
        conn = sqlite3.connect(DB_NAME)
    except sqlite3.OperationalError:
        # Fallback to /tmp if primary path fails
        DB_NAME = str(Path(tempfile.gettempdir()) / "expense.db")
        conn = sqlite3.connect(DB_NAME)

    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    """
    Create transactions table if it does not exist.
    """
    try:
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
    except Exception as e:
        print(f"create_table notice: {e}")


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