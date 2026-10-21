<div align="center">

# 💰 Expense Tracker Using Python

**A modular, full-featured CLI personal finance management application with SQLite database persistence, interactive visual charts, and multi-format export capabilities.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-SQLite3-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Pandas](https://img.shields.io/badge/Data-Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-11557C)](https://matplotlib.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-success)](#)

<br/>

> *Developed by **Sharad Sharma** as part of the Python Programming Internship at **SyntecXHub Technologies Pvt. Ltd.***

</div>

---

## 📌 Overview

**Expense Tracker** is a command-line financial management system engineered in Python. It provides complete control over personal finances by recording income and expenditure, evaluating monthly budgets, generating visual graphical analytics, and exporting structured datasets into CSV and Excel spreadsheets.

Built on top of a modular architecture with a persistent **SQLite3** relational database, this application enforces data integrity with input validation, date formatting checks, and safe numerical conversion.

---

## ✨ Features

- 💵 **Dual Transaction Accounting**: Log both **Income** and **Expense** entries with date, category, amount, and custom descriptions.
- 🗃️ **Robust CRUD Operations**:
  - Add, view, update, and delete individual transaction records.
  - Search and filter records by category or by specific months.
- 📊 **Visual Analytics (Matplotlib)**:
  - **Category Pie Chart**: Visual distribution of expense breakdown.
  - **Monthly Bar Chart**: Month-by-month spending trends.
  - **Income vs. Expense Bar Chart**: Side-by-side comparison of total earnings vs outgoings.
- 📑 **Data Exporting (CSV & Excel)**:
  - One-click export to `reports/transactions.csv`.
  - Formatted multi-column export to `reports/transactions.xlsx` using Pandas.
- 📈 **Financial Summary Reports**:
  - Automated calculation of Total Income, Total Expenses, Net Savings Balance, and Average/Highest/Lowest expenses.
  - Generates downloadable text summary files in `reports/`.
- 🛡️ **Defensive Input Validation**: Validates date formats (`YYYY-MM-DD`), non-negative currency amounts, and invalid menu inputs.

---

## 🖥️ Terminal Menu Interface

```text
================================================================================
                               EXPENSE TRACKER
================================================================================
1. Add Income
2. Add Expense
3. View Transactions
4. Update Transaction
5. Delete Transaction
6. Search by Category
7. Monthly Summary
8. Export CSV & Excel
9. Generate Charts
10. Generate Reports
11. Exit
================================================================================
```

---

## 🛠️ Tech Stack & Dependencies

| Module / Library | Purpose |
| :--- | :--- |
| **Python 3** | Core programming language |
| **`sqlite3`** | Embedded relational database management |
| **`pandas`** | Data aggregation, SQL query reading, and spreadsheet export |
| **`matplotlib`** | Plotting pie charts and bar charts for financial analytics |
| **`openpyxl`** | Excel `.xlsx` workbook generation engine |
| **`csv` & `os`** | File system operations and CSV handling |

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8 or higher installed:
```bash
python --version
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sharad1sharma/EXPENSE-TRACKER-USING-PYTHON.git
   cd EXPENSE-TRACKER-USING-PYTHON
   ```

2. **(Optional) Create and activate a virtual environment:**
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the required packages:**
   ```bash
   pip install pandas matplotlib openpyxl
   ```

---

## 💻 How to Run

Launch the interactive application by executing:

```bash
python main.py
```

### Example Usage Workflow:

1. Select `1` to record an income source (e.g., *Salary*, *Freelancing*).
2. Select `2` to log daily expenses (e.g., *Groceries*, *Utilities*, *Dining*).
3. Select `3` to inspect the tabular transaction ledger:
   ```text
   ===============================================================================================
   ID   DATE            TYPE       CATEGORY        AMOUNT          DESCRIPTION
   -----------------------------------------------------------------------------------------------
   1    2026-07-01      Income     Salary          50000.00        Monthly Tech Stipend
   2    2026-07-05      Expense    Groceries       3500.00         Supermarket supplies
   ===============================================================================================
   ```
4. Select `8` to automatically output `.csv` and `.xlsx` files into the `reports/` directory.
5. Select `9` to generate high-resolution visual charts.

---

## 📂 Project Architecture

```text
EXPENSE-TRACKER-USING-PYTHON/
│
├── main.py          # Application entrypoint & interactive CLI menu loop
├── database.py      # SQLite connection, schema definition & query executors
├── crud.py          # Create, Read, Update, Delete & search transaction business logic
├── charts.py        # Data visualizer generating pie charts and comparison bar charts
├── export.py        # Data export pipeline to CSV and Excel (.xlsx) formats
├── reports.py       # Financial statistical calculations & text summary reports
├── utils.py         # Input validation (dates, floats, integers) and formatting utilities
│
├── reports/         # Auto-generated directory containing exported charts & spreadsheets
└── README.md        # Project documentation
```

---

## 📊 Generated Output Files

When running export or chart generation routines, files are neatly organized inside the `reports/` folder:

- `reports/transactions.csv` — Full ledger in standard CSV format.
- `reports/transactions.xlsx` — Formatted Excel workbook.
- `reports/expense_category_pie.png` — Category spending distribution chart.
- `reports/monthly_expense_bar.png` — Monthly spending trend analysis.
- `reports/income_vs_expense.png` — Income vs expense comparison graph.
- `reports/financial_summary.txt` — Snapshot summary of overall financial health.

---

## 👤 Author

**Sharad Sharma**
- GitHub: [@sharad1sharma](https://github.com/sharad1sharma)
- Email: [sharmasharad9531@gmail.com](mailto:sharmasharad9531@gmail.com)
- Organization: **SyntecXHub Technologies Pvt. Ltd.**

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).
