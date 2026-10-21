# export.py

import csv
import os
import pandas as pd

from database import fetch_all

# ==============================
# Create Reports Folder
# ==============================

import tempfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IS_SERVERLESS = 'VERCEL' in os.environ or 'VERCEL_ENV' in os.environ or bool(os.environ.get('AWS_LAMBDA_FUNCTION_NAME'))

REPORT_FOLDER = str(Path(tempfile.gettempdir()) / "reports") if IS_SERVERLESS else str(BASE_DIR / "reports")
os.makedirs(REPORT_FOLDER, exist_ok=True)


# ==============================
# Fetch All Transactions
# ==============================

def fetch_transactions():
    query = """
    SELECT
        id,
        date,
        type,
        category,
        amount,
        description
    FROM transactions
    ORDER BY date ASC, id ASC
    """

    return fetch_all(query)


# ==============================
# Export CSV
# ==============================

def export_csv():

    rows = fetch_transactions()

    if not rows:
        print("\n❌ No transactions available.\n")
        return

    file_path = os.path.join(
        REPORT_FOLDER,
        "transactions.csv"
    )

    with open(
            file_path,
            mode="w",
            newline="",
            encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Date",
            "Type",
            "Category",
            "Amount",
            "Description"
        ])

        for row in rows:

            writer.writerow([
                row["id"],
                row["date"],
                row["type"],
                row["category"],
                row["amount"],
                row["description"]
            ])

    print(f"✅ CSV exported successfully.")
    print(file_path)


# ==============================
# Export Excel
# ==============================

def export_excel():

    rows = fetch_transactions()

    if not rows:
        print("\n❌ No transactions available.\n")
        return

    data = []

    for row in rows:

        data.append({

            "ID": row["id"],
            "Date": row["date"],
            "Type": row["type"],
            "Category": row["category"],
            "Amount": row["amount"],
            "Description": row["description"]

        })

    df = pd.DataFrame(data)

    file_path = os.path.join(
        REPORT_FOLDER,
        "transactions.xlsx"
    )

    df.to_excel(
        file_path,
        index=False
    )

    print(f"✅ Excel exported successfully.")
    print(file_path)


# ==============================
# Export Summary CSV
# ==============================

def export_summary():

    rows = fetch_transactions()

    if not rows:
        print("\n❌ No transactions available.\n")
        return

    income = 0
    expense = 0

    for row in rows:

        if row["type"] == "Income":
            income += row["amount"]

        else:
            expense += row["amount"]

    saving = income - expense

    file_path = os.path.join(
        REPORT_FOLDER,
        "summary.csv"
    )

    with open(
            file_path,
            mode="w",
            newline="",
            encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Total Income",
            "Total Expense",
            "Total Saving"
        ])

        writer.writerow([
            income,
            expense,
            saving
        ])

    print(f"✅ Summary exported successfully.")
    print(file_path)


# ==============================
# Export Everything
# ==============================

def export_all():

    export_csv()

    export_excel()

    export_summary()

    print("\n📁 All files exported successfully.")


# ==============================
# Test
# ==============================

if __name__ == "__main__":

    export_all()