<div align="center">

# 💰 Expense Tracker Pro Using Python

**A modern, full-stack personal finance and budget management platform featuring an interactive dark-glassmorphism Web Frontend Dashboard, SQLite persistence, and a modular Python CLI interface.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Backend-Flask%203.x-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/Database-SQLite3-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Frontend](https://img.shields.io/badge/Frontend-HTML5%20%2F%20Vanilla%20CSS%20%2F%20JS-E34F26?logo=html5&logoColor=white)](index.html)
[![Pandas](https://img.shields.io/badge/Data-Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-success)](#)

<img width="1513" height="806" alt="Screenshot 2026-10-22 010031" src="https://github.com/user-attachments/assets/4a7d6c95-20a2-4064-b202-cfbb1e7e5cbf" />


<br/>

> *Developed by **Sharad Sharma** for **SyntecXHub Technologies Pvt. Ltd.** (Task-4: Python Programming Internship).*

</div>

---

## 📌 Overview

**Expense Tracker Pro** is a comprehensive personal finance tracking suite available in **two distinct modes**:
1. 🌐 **Modern Web Frontend Dashboard (`index.html` & `app.py`)**: A visual, dark-mode glassmorphic single-page web app with real-time KPI metrics, dynamic HTML5 canvas charts, filtering search bars, transaction modals, and instant CSV/Excel downloads.
2. 💻 **Modular Terminal CLI (`main.py`)**: An 11-step interactive command-line interface with menu prompts, tabular ledger viewing, and Matplotlib chart generation.

The application interfaces directly with an embedded **SQLite3** relational database (`expense.db`) with complete CRUD operations, category aggregations, and robust validation.

---

## ✨ Web Dashboard & Application Features

- 💎 **Modern Dark Glassmorphism UI**: High-contrast, sleek financial dashboard styled with translucent frosted glass, vibrant gradients, and Google Fonts (*Outfit* and *JetBrains Mono*).
- 📊 **Real-Time Financial KPIs**: Instant tracking of **Total Income**, **Total Expenses**, **Net Savings Balance**, and **Average Expense**.
- 📈 **Dynamic Cash Flow Visualizer**: HTML5 Canvas rendering of monthly Income vs Expense bar comparisons.
- 🍩 **Category Spending Breakdown**: Progress bars and proportional distribution across spending categories (Rent, Groceries, Utilities, Shopping, etc.).
- 📝 **Full CRUD Ledger**: In-line creation, modal editing, and safe deletion of income and expense transactions.
- 🔍 **Instant Search & Filtering**: Multi-condition filtering by transaction type (Income/Expense), category dropdowns, and live keyword searches.
- 📥 **One-Click Multi-Format Export**: Direct download of transaction reports in both **CSV** and **Excel (`.xlsx`)** formats.
- 🌐 **Dual Storage Engine**: Automatically talks to the Flask REST API & SQLite database when running, and gracefully falls back to client-side storage if viewed statically!

---

## 🖥️ Two Ways to Use

### Mode 1: Interactive Web Dashboard (Recommended)

1. Launch the web server:
   ```bash
   python app.py
   ```
2. Your default web browser will automatically open:
   👉 **`http://127.0.0.1:5000`**

*(Alternatively, you can also double-click `index.html` to run the frontend directly in client-storage mode!)*

---

### Mode 2: Classic Terminal Interface

For terminal enthusiasts, launch the CLI by running:

```bash
python main.py
```

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

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | HTML5, Vanilla CSS3 (Glassmorphism), JavaScript (ES6+), HTML5 Canvas, FontAwesome |
| **Backend API** | Python 3, Flask, Flask-CORS |
| **Database** | SQLite3 relational database (`expense.db`) |
| **Data & Reports** | Pandas, Matplotlib, OpenpyXL, CSV standard library |

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8 or higher installed on your system:

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

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📂 Project Architecture

```text
EXPENSE-TRACKER-USING-PYTHON/
│
├── index.html          # High-performance glassmorphic Web Dashboard UI
├── app.py              # Flask Web API server syncing with SQLite database
├── main.py             # Interactive CLI entrypoint & terminal menu loop
├── database.py         # SQLite connection, schema definition & query handlers
├── crud.py             # Transaction CRUD and filtering business logic
├── charts.py           # Matplotlib visualization generator
├── export.py           # CSV and Excel export pipeline
├── reports.py          # Summary statistics & report generation
├── utils.py            # Input validation and formatting utilities
├── expense.db          # Pre-seeded SQLite database file
├── requirements.txt    # Python dependencies list
├── .gitignore          # Git ignore configuration
└── README.md           # Project documentation
```

---

## 👤 Author

**Sharad Sharma**
- GitHub: [@sharad1sharma](https://github.com/sharad1sharma)
- Email: [sharmasharad9531@gmail.com](mailto:sharmasharad9531@gmail.com)
- Organization: **SyntecXHub Technologies Pvt. Ltd.**

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).
