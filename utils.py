# utils.py

from datetime import datetime


# -----------------------------
# Validate Date
# -----------------------------

def validate_date(date_string):

    try:

        datetime.strptime(
            date_string,
            "%Y-%m-%d"
        )

        return True

    except ValueError:

        return False


# -----------------------------
# Validate Amount
# -----------------------------

def validate_amount(amount):

    try:

        amount = float(amount)

        if amount < 0:
            return False

        return True

    except ValueError:

        return False


# -----------------------------
# Currency Format
# -----------------------------

def format_currency(amount):

    return f"₹{amount:,.2f}"


# -----------------------------
# Input Integer
# -----------------------------

def input_integer(message):

    while True:

        try:

            return int(input(message))

        except ValueError:

            print("❌ Enter a valid integer.")


# -----------------------------
# Input Float
# -----------------------------

def input_float(message):

    while True:

        try:

            value = float(input(message))

            if value < 0:
                print("❌ Amount cannot be negative.")
                continue

            return value

        except ValueError:

            print("❌ Enter a valid number.")


# -----------------------------
# Pause
# -----------------------------

def pause():

    input("\nPress Enter to continue...")


# -----------------------------
# Header
# -----------------------------

def header(title):

    print("\n" + "=" * 60)

    print(title.center(60))

    print("=" * 60)


# -----------------------------
# Line
# -----------------------------

def line():

    print("-" * 60)


# -----------------------------
# Current Date
# -----------------------------

def today():

    return datetime.now().strftime("%Y-%m-%d")


# -----------------------------
# Month
# -----------------------------

def current_month():

    return datetime.now().strftime("%Y-%m")


# -----------------------------
# Exit Message
# -----------------------------

def goodbye():

    print("\nThank you for using Expense Tracker.")