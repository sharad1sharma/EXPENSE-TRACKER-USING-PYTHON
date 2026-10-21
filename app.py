"""
Expense Tracker Web Application Backend
Developed by Sharad Sharma | SyntecXHub Technologies Pvt. Ltd.
"""

import os
import sys
import json
import sqlite3
import webbrowser
from pathlib import Path
from flask import Flask, jsonify, request, send_file, send_from_directory
from flask_cors import CORS

from database import initialize_database, get_connection, execute_query, fetch_all, fetch_one
from reports import total_income, total_expense, total_transactions, highest_expense, lowest_expense, average_expense
from export import export_csv, export_excel

# Initialize SQLite database
initialize_database()

# Seed default transactions if empty so the UI looks great immediately
def seed_initial_data_if_empty():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM transactions")
    count = c.fetchone()[0]
    if count == 0:
        sample_records = [
            ("2026-07-01", "Income", "Salary", 55000.0, "Monthly Software Engineering Salary"),
            ("2026-07-03", "Expense", "Rent", 12000.0, "Apartment Monthly Rent"),
            ("2026-07-05", "Expense", "Groceries", 3450.0, "Supermarket weekly groceries"),
            ("2026-07-08", "Income", "Freelancing", 18500.0, "Python Scripting & API Project"),
            ("2026-07-10", "Expense", "Utilities", 1850.0, "Electricity & High-speed Fiber Bill"),
            ("2026-07-14", "Expense", "Dining", 1250.0, "Team dinner & pizza"),
            ("2026-07-18", "Expense", "Shopping", 4200.0, "Mechanical keyboard & tech gear"),
            ("2026-07-22", "Income", "Investments", 3200.0, "Quarterly dividend payout"),
            ("2026-07-25", "Expense", "Transportation", 1600.0, "Metro pass & fuel refill"),
            ("2026-07-28", "Expense", "Entertainment", 999.0, "Cloud stream subscription"),
        ]
        c.executemany(
            "INSERT INTO transactions (date, type, category, amount, description) VALUES (?, ?, ?, ?, ?)",
            sample_records
        )
        conn.commit()
    conn.close()

seed_initial_data_if_empty()

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=str(BASE_DIR), static_url_path="")
CORS(app)

@app.route("/")
def index():
    return send_file(BASE_DIR / "index.html")

@app.route("/api/transactions", methods=["GET"])
def get_transactions():
    category = request.args.get("category")
    tx_type = request.args.get("type")
    search = request.args.get("search")
    month = request.args.get("month")

    query = "SELECT id, date, type, category, amount, description FROM transactions WHERE 1=1"
    params = []

    if category and category != "All":
        query += " AND category = ?"
        params.append(category)

    if tx_type and tx_type != "All":
        query += " AND type = ?"
        params.append(tx_type)

    if month:
        query += " AND date LIKE ?"
        params.append(f"{month}%")

    if search:
        query += " AND (description LIKE ? OR category LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])

    query += " ORDER BY date DESC, id DESC"
    rows = fetch_all(query, tuple(params))
    
    transactions = [dict(row) for row in rows]
    return jsonify(transactions)

@app.route("/api/transactions", methods=["POST"])
def add_transaction():
    data = request.get_json() or {}
    date = data.get("date")
    tx_type = data.get("type")
    category = data.get("category")
    amount = data.get("amount")
    description = data.get("description", "")

    if not date or not tx_type or not category or amount is None:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        amount = float(amount)
        if amount < 0:
            return jsonify({"error": "Amount must be a positive number"}), 400
    except ValueError:
        return jsonify({"error": "Invalid amount format"}), 400

    query = """
    INSERT INTO transactions (date, type, category, amount, description)
    VALUES (?, ?, ?, ?, ?)
    """
    conn = get_connection()
    c = conn.cursor()
    c.execute(query, (date, tx_type, category, amount, description))
    conn.commit()
    new_id = c.lastrowid
    conn.close()

    return jsonify({"message": "Transaction added successfully", "id": new_id}), 201

@app.route("/api/transactions/<int:tx_id>", methods=["PUT"])
def update_transaction_api(tx_id):
    data = request.get_json() or {}
    date = data.get("date")
    tx_type = data.get("type")
    category = data.get("category")
    amount = data.get("amount")
    description = data.get("description", "")

    if not date or not tx_type or not category or amount is None:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        amount = float(amount)
        if amount < 0:
            return jsonify({"error": "Amount must be positive"}), 400
    except ValueError:
        return jsonify({"error": "Invalid amount format"}), 400

    query = """
    UPDATE transactions
    SET date = ?, type = ?, category = ?, amount = ?, description = ?
    WHERE id = ?
    """
    execute_query(query, (date, tx_type, category, amount, description, tx_id))
    return jsonify({"message": "Transaction updated successfully"})

@app.route("/api/transactions/<int:tx_id>", methods=["DELETE"])
def delete_transaction_api(tx_id):
    query = "DELETE FROM transactions WHERE id = ?"
    execute_query(query, (tx_id,))
    return jsonify({"message": "Transaction deleted successfully"})

@app.route("/api/summary", methods=["GET"])
def get_summary():
    inc = total_income()
    exp = total_expense()
    net = round(inc - exp, 2)
    count = total_transactions()
    highest = highest_expense()
    lowest = lowest_expense()
    avg = average_expense()

    # Category breakdown for expenses
    cat_rows = fetch_all("""
        SELECT category, SUM(amount) AS total
        FROM transactions
        WHERE type = 'Expense'
        GROUP BY category
        ORDER BY total DESC
    """)
    category_breakdown = []
    for r in cat_rows:
        pct = round((r["total"] / exp * 100), 1) if exp > 0 else 0
        category_breakdown.append({
            "category": r["category"],
            "total": float(r["total"]),
            "percentage": pct
        })

    # Monthly trends
    monthly_rows = fetch_all("""
        SELECT 
            SUBSTR(date, 1, 7) AS month,
            SUM(CASE WHEN type = 'Income' THEN amount ELSE 0 END) AS income,
            SUM(CASE WHEN type = 'Expense' THEN amount ELSE 0 END) AS expense
        FROM transactions
        GROUP BY month
        ORDER BY month ASC
    """)
    monthly_trends = [
        {
            "month": r["month"],
            "income": float(r["income"]),
            "expense": float(r["expense"]),
            "net": float(r["income"] - r["expense"])
        }
        for r in monthly_rows
    ]

    # Categories list
    all_cats = fetch_all("SELECT DISTINCT category FROM transactions ORDER BY category ASC")
    categories_list = [c["category"] for c in all_cats]

    return jsonify({
        "total_income": float(inc),
        "total_expense": float(exp),
        "net_balance": float(net),
        "total_transactions": count,
        "highest_expense": float(highest),
        "lowest_expense": float(lowest),
        "average_expense": float(avg),
        "category_breakdown": category_breakdown,
        "monthly_trends": monthly_trends,
        "categories": categories_list
    })

@app.route("/api/export/<format_type>", methods=["GET"])
def export_file(format_type):
    from export import REPORT_FOLDER
    if format_type == "csv":
        export_csv()
        file_path = Path(REPORT_FOLDER) / "transactions.csv"
        if file_path.exists():
            return send_file(file_path, as_attachment=True, download_name="transactions.csv")
    elif format_type == "excel":
        export_excel()
        file_path = Path(REPORT_FOLDER) / "transactions.xlsx"
        if file_path.exists():
            return send_file(file_path, as_attachment=True, download_name="transactions.xlsx")
    return jsonify({"error": "Export failed or format invalid"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\\n========================================================")
    print(f"   EXPENSE TRACKER WEB DASHBOARD - RUNNING LOCALLY      ")
    print(f"   Developed by Sharad Sharma | SyntecXHub Technologies ")
    print(f"   URL: http://127.0.0.1:{port}                         ")
    print(f"========================================================\\n")
    if "--no-browser" not in sys.argv:
        try:
            webbrowser.open(f"http://127.0.0.1:{port}")
        except Exception:
            pass
    app.run(host="0.0.0.0", port=port, debug=False)
