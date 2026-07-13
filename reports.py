# reports.py

import os
from database import fetch_all, fetch_one

REPORT_FOLDER = "reports"
os.makedirs(REPORT_FOLDER, exist_ok=True)


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


def total_transactions():
    row = fetch_one("""
        SELECT COUNT(*) AS total
        FROM transactions
    """)
    return row["total"]


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


def average_expense():
    row = fetch_one("""
        SELECT IFNULL(AVG(amount),0) AS avg
        FROM transactions
        WHERE type='Expense'
    """)
    return round(row["avg"], 2)


def savings():
    return total_income() - total_expense()


def generate_summary_report():

    file_path = os.path.join(
        REPORT_FOLDER,
        "summary_report.txt"
    )

    with open(file_path, "w", encoding="utf-8") as file:

        file.write("=" * 50 + "\n")
        file.write("        EXPENSE TRACKER SUMMARY REPORT\n")
        file.write("=" * 50 + "\n\n")

        file.write(f"Total Income        : ₹{total_income():,.2f}\n")
        file.write(f"Total Expense       : ₹{total_expense():,.2f}\n")
        file.write(f"Total Savings       : ₹{savings():,.2f}\n")
        file.write(f"Transactions        : {total_transactions()}\n")
        file.write(f"Highest Expense     : ₹{highest_expense():,.2f}\n")
        file.write(f"Lowest Expense      : ₹{lowest_expense():,.2f}\n")
        file.write(f"Average Expense     : ₹{average_expense():,.2f}\n")

    print("✅ summary_report.txt generated")


def generate_monthly_report():

    rows = fetch_all("""

    SELECT

        substr(date,1,7) as month,

        SUM(CASE
                WHEN type='Income'
                THEN amount
                ELSE 0
            END) as income,

        SUM(CASE
                WHEN type='Expense'
                THEN amount
                ELSE 0
            END) as expense

    FROM transactions

    GROUP BY month

    ORDER BY month

    """)

    file_path = os.path.join(
        REPORT_FOLDER,
        "monthly_report.txt"
    )

    with open(file_path, "w", encoding="utf-8") as file:

        file.write("=" * 65 + "\n")
        file.write("               MONTHLY REPORT\n")
        file.write("=" * 65 + "\n\n")

        for row in rows:

            saving = row["income"] - row["expense"]

            file.write(f"Month   : {row['month']}\n")
            file.write(f"Income  : ₹{row['income']:,.2f}\n")
            file.write(f"Expense : ₹{row['expense']:,.2f}\n")
            file.write(f"Saving  : ₹{saving:,.2f}\n")
            file.write("-" * 40 + "\n")

    print("✅ monthly_report.txt generated")


def generate_all_reports():

    generate_summary_report()

    generate_monthly_report()

    print("\n📄 Reports Generated Successfully")


if __name__ == "__main__":

    generate_all_reports()