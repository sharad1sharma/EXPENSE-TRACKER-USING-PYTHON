# crud.py

from database import execute_query, fetch_all, fetch_one


# -----------------------------
# ADD TRANSACTIONS
# -----------------------------

def add_income(date, category, amount, description):
    """
    Add an income transaction.
    """
    query = """
    INSERT INTO transactions
    (date, type, category, amount, description)
    VALUES (?, 'Income', ?, ?, ?)
    """

    execute_query(query, (date, category, amount, description))
    print("\n✅ Income added successfully.\n")


def add_expense(date, category, amount, description):
    """
    Add an expense transaction.
    """
    query = """
    INSERT INTO transactions
    (date, type, category, amount, description)
    VALUES (?, 'Expense', ?, ?, ?)
    """

    execute_query(query, (date, category, amount, description))
    print("\n✅ Expense added successfully.\n")


# -----------------------------
# VIEW TRANSACTIONS
# -----------------------------

def view_transactions():
    """
    Display all transactions.
    """
    rows = fetch_all("""
        SELECT *
        FROM transactions
        ORDER BY date DESC, id DESC
    """)

    if not rows:
        print("\nNo transactions found.\n")
        return

    print("\n" + "=" * 95)
    print(
        f"{'ID':<5}"
        f"{'DATE':<15}"
        f"{'TYPE':<10}"
        f"{'CATEGORY':<18}"
        f"{'AMOUNT':<12}"
        f"DESCRIPTION"
    )
    print("=" * 95)

    for row in rows:
        print(
            f"{row['id']:<5}"
            f"{row['date']:<15}"
            f"{row['type']:<10}"
            f"{row['category']:<18}"
            f"{row['amount']:<12.2f}"
            f"{row['description']}"
        )

    print("=" * 95 + "\n")


# -----------------------------
# SEARCH
# -----------------------------

def search_by_category(category):
    """
    Search transactions by category.
    """
    rows = fetch_all("""
        SELECT *
        FROM transactions
        WHERE category LIKE ?
        ORDER BY date DESC
    """, (f"%{category}%",))

    return rows


def search_by_type(transaction_type):
    """
    Search Income or Expense.
    """
    rows = fetch_all("""
        SELECT *
        FROM transactions
        WHERE type=?
        ORDER BY date DESC
    """, (transaction_type,))

    return rows


def search_by_month(month):
    """
    Search by month.

    Example:
    month = "2026-07"
    """
    rows = fetch_all("""
        SELECT *
        FROM transactions
        WHERE substr(date,1,7)=?
        ORDER BY date
    """, (month,))

    return rows


# -----------------------------
# UPDATE
# -----------------------------

def update_transaction(
        transaction_id,
        date,
        category,
        amount,
        description
):
    """
    Update transaction details.
    """

    row = fetch_one(
        "SELECT * FROM transactions WHERE id=?",
        (transaction_id,)
    )

    if row is None:
        print("\n❌ Transaction not found.\n")
        return

    execute_query("""
        UPDATE transactions
        SET
            date=?,
            category=?,
            amount=?,
            description=?
        WHERE id=?
    """,
    (
        date,
        category,
        amount,
        description,
        transaction_id
    ))

    print("\n✅ Transaction updated successfully.\n")


# -----------------------------
# DELETE
# -----------------------------

def delete_transaction(transaction_id):
    """
    Delete transaction by ID.
    """

    row = fetch_one(
        "SELECT * FROM transactions WHERE id=?",
        (transaction_id,)
    )

    if row is None:
        print("\n❌ Transaction not found.\n")
        return

    execute_query(
        "DELETE FROM transactions WHERE id=?",
        (transaction_id,)
    )

    print("\n🗑️ Transaction deleted successfully.\n")


# -----------------------------
# TOTALS
# -----------------------------

def total_income():
    row = fetch_one("""
        SELECT IFNULL(SUM(amount),0) AS total
        FROM transactions
        WHERE type='Income'
    """)

    return row["total"]


def total_expense():
    row = fetch_one("""
        SELECT IFNULL(SUM(amount),0) AS total
        FROM transactions
        WHERE type='Expense'
    """)

    return row["total"]


def total_savings():
    return total_income() - total_expense()


# -----------------------------
# SQL AGGREGATION
# -----------------------------

def transaction_count():
    row = fetch_one("""
        SELECT COUNT(*) AS total
        FROM transactions
    """)

    return row["total"]


def average_expense():
    row = fetch_one("""
        SELECT IFNULL(AVG(amount),0) AS avg
        FROM transactions
        WHERE type='Expense'
    """)

    return round(row["avg"], 2)


def highest_expense():
    row = fetch_one("""
        SELECT IFNULL(MAX(amount),0) AS highest
        FROM transactions
        WHERE type='Expense'
    """)

    return row["highest"]


def lowest_expense():
    row = fetch_one("""
        SELECT IFNULL(MIN(amount),0) AS lowest
        FROM transactions
        WHERE type='Expense'
    """)

    return row["lowest"]


# -----------------------------
# MONTHLY SUMMARY
# -----------------------------

def monthly_summary(month):
    """
    month example:
    2026-07
    """

    income = fetch_one("""
        SELECT IFNULL(SUM(amount),0) AS total
        FROM transactions
        WHERE type='Income'
        AND substr(date,1,7)=?
    """, (month,))

    expense = fetch_one("""
        SELECT IFNULL(SUM(amount),0) AS total
        FROM transactions
        WHERE type='Expense'
        AND substr(date,1,7)=?
    """, (month,))

    saving = income["total"] - expense["total"]

    return {
        "month": month,
        "income": income["total"],
        "expense": expense["total"],
        "saving": saving
    }