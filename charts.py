# charts.py

import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_NAME = "expense.db"
REPORT_FOLDER = "reports"


# ---------------------------------
# Create reports folder
# ---------------------------------

if not os.path.exists(REPORT_FOLDER):
    os.makedirs(REPORT_FOLDER)


# ---------------------------------
# Database Connection
# ---------------------------------

def get_connection():
    return sqlite3.connect(DB_NAME)


# ---------------------------------
# Load Data
# ---------------------------------

def load_data():
    conn = get_connection()

    query = """
    SELECT
        date,
        type,
        category,
        amount
    FROM transactions
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


# ---------------------------------
# Pie Chart
# ---------------------------------

def expense_pie_chart():

    df = load_data()

    expense = df[df["type"] == "Expense"]

    if expense.empty:
        print("❌ No expense data available.")
        return

    data = expense.groupby("category")["amount"].sum()

    plt.figure(figsize=(8, 8))

    plt.pie(
        data,
        labels=data.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Expense Distribution by Category")

    plt.tight_layout()

    file_path = os.path.join(
        REPORT_FOLDER,
        "expense_pie_chart.png"
    )

    plt.savefig(file_path)
    plt.close()

    print(f"✅ Pie chart saved to {file_path}")


# ---------------------------------
# Bar Chart
# ---------------------------------

def income_vs_expense_bar():

    df = load_data()

    if df.empty:
        print("❌ No transactions found.")
        return

    income = df[df["type"] == "Income"]["amount"].sum()
    expense = df[df["type"] == "Expense"]["amount"].sum()

    plt.figure(figsize=(6, 5))

    plt.bar(
        ["Income", "Expense"],
        [income, expense]
    )

    plt.ylabel("Amount (₹)")
    plt.title("Income vs Expense")

    plt.tight_layout()

    file_path = os.path.join(
        REPORT_FOLDER,
        "income_vs_expense.png"
    )

    plt.savefig(file_path)
    plt.close()

    print(f"✅ Bar chart saved to {file_path}")


# ---------------------------------
# Monthly Trend
# ---------------------------------

def monthly_trend_chart():

    df = load_data()

    if df.empty:
        print("❌ No transactions found.")
        return

    df["date"] = pd.to_datetime(df["date"])

    df["month"] = df["date"].dt.strftime("%Y-%m")

    monthly = (
        df.groupby(["month", "type"])["amount"]
        .sum()
        .unstack(fill_value=0)
    )

    plt.figure(figsize=(10, 5))

    if "Income" in monthly.columns:
        plt.plot(
            monthly.index,
            monthly["Income"],
            marker="o",
            label="Income"
        )

    if "Expense" in monthly.columns:
        plt.plot(
            monthly.index,
            monthly["Expense"],
            marker="o",
            label="Expense"
        )

    plt.title("Monthly Income vs Expense")
    plt.xlabel("Month")
    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()

    file_path = os.path.join(
        REPORT_FOLDER,
        "monthly_trend.png"
    )

    plt.savefig(file_path)
    plt.close()

    print(f"✅ Monthly trend chart saved to {file_path}")


# ---------------------------------
# Category Expense Bar Chart
# ---------------------------------

def category_expense_chart():

    df = load_data()

    expense = df[df["type"] == "Expense"]

    if expense.empty:
        print("❌ No expense data available.")
        return

    category = (
        expense.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 5))

    plt.bar(
        category.index,
        category.values
    )

    plt.title("Expense by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=30)

    plt.tight_layout()

    file_path = os.path.join(
        REPORT_FOLDER,
        "category_expense.png"
    )

    plt.savefig(file_path)
    plt.close()

    print(f"✅ Category chart saved to {file_path}")


# ---------------------------------
# Generate All Charts
# ---------------------------------

def generate_all_charts():

    expense_pie_chart()

    income_vs_expense_bar()

    monthly_trend_chart()

    category_expense_chart()

    print("\n📊 All charts generated successfully.")


# ---------------------------------
# Test
# ---------------------------------

if __name__ == "__main__":

    generate_all_charts()