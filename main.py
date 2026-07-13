
                      # EXPENSE TRACKER Made By :- SHARAD SHARMA
            #TASK-4: EXPENSE TRACKER USING PYTHON COMPLETED ON 12-07-2026
                           # BY Syntecxhub Technologies Pvt. Ltd.       


from database import initialize_database
from crud import (
    add_income,
    add_expense,
    view_transactions,
    update_transaction,
    delete_transaction,
    search_by_category,
    search_by_month,
    monthly_summary
)

from export import export_all
from charts import generate_all_charts
from reports import generate_all_reports

from utils import (
    validate_date,
    input_float,
    input_integer,
    pause,
    header
)


# ==========================================
# Initialize Database
# ==========================================

initialize_database()


# ==========================================
# Menu
# ==========================================

def menu():

    header("Expense Tracker")

    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Update Transaction")
    print("5. Delete Transaction")
    print("6. Search by Category")
    print("7. Monthly Summary")
    print("8. Export CSV & Excel")
    print("9. Generate Charts")
    print("10. Generate Reports")
    print("11. Exit")

    choice = input("\nEnter your choice : ")

    return choice


# ==========================================
# Add Income
# ==========================================

def add_income_menu():

    print("\n------ Add Income ------")

    date = input("Date (YYYY-MM-DD): ")

    if not validate_date(date):
        print("Invalid Date.")
        return

    category = input("Category : ")

    amount = input_float("Amount : ")

    description = input("Description : ")

    add_income(
        date,
        category,
        amount,
        description
    )

    pause()


# ==========================================
# Add Expense
# ==========================================

def add_expense_menu():

    print("\n------ Add Expense ------")

    date = input("Date (YYYY-MM-DD): ")

    if not validate_date(date):
        print("Invalid Date.")
        return

    category = input("Category : ")

    amount = input_float("Amount : ")

    description = input("Description : ")

    add_expense(
        date,
        category,
        amount,
        description
    )

    pause()


# ==========================================
# View Transactions
# ==========================================

def view_menu():

    view_transactions()

    pause()


# ==========================================
# Search Category
# ==========================================

def search_menu():

    category = input("\nEnter Category : ")

    rows = search_by_category(category)

    if not rows:
        print("\nNo Record Found.\n")

    else:

        print("\n")

        print("-" * 80)

        for row in rows:

            print(
                f"{row['id']} | "
                f"{row['date']} | "
                f"{row['type']} | "
                f"{row['category']} | "
                f"₹{row['amount']} | "
                f"{row['description']}"
            )

        print("-" * 80)

    pause()
    

# ==========================================
# Update Transaction
# ==========================================

def update_menu():

    print("\n------ Update Transaction ------")

    transaction_id = input_integer("Transaction ID : ")

    date = input("New Date (YYYY-MM-DD): ")

    if not validate_date(date):
        print("❌ Invalid Date.")
        pause()
        return

    category = input("New Category : ")

    amount = input_float("New Amount : ")

    description = input("New Description : ")

    update_transaction(
        transaction_id,
        date,
        category,
        amount,
        description
    )

    pause()


# ==========================================
# Delete Transaction
# ==========================================

def delete_menu():

    print("\n------ Delete Transaction ------")

    transaction_id = input_integer("Transaction ID : ")

    delete_transaction(transaction_id)

    pause()


# ==========================================
# Monthly Summary
# ==========================================

def summary_menu():

    print("\n------ Monthly Summary ------")

    month = input("Enter Month (YYYY-MM): ")

    result = monthly_summary(month)

    print("\n==============================")
    print("Monthly Summary")
    print("==============================")
    print(f"Month   : {result['month']}")
    print(f"Income  : ₹{result['income']:.2f}")
    print(f"Expense : ₹{result['expense']:.2f}")
    print(f"Saving  : ₹{result['saving']:.2f}")

    pause()


# ==========================================
# Export Files
# ==========================================

def export_menu():

    print("\nGenerating CSV & Excel...")

    export_all()

    pause()


# ==========================================
# Generate Charts
# ==========================================

def charts_menu():

    print("\nGenerating Charts...")

    generate_all_charts()

    pause()


# ==========================================
# Generate Reports
# ==========================================

def reports_menu():

    print("\nGenerating Reports...")

    generate_all_reports()

    pause()


# ==========================================
# Exit Program
# ==========================================

def exit_program():

    print("\nGenerating Final Reports...")

    export_all()

    generate_all_charts()

    generate_all_reports()

    print("\n===================================")
    print(" Thank You For Using Expense Tracker")
    print("===================================")
    print("Reports Saved Inside reports/ Folder")
    print("Goodbye 👋")
    

# ==========================================
# Main Program
# ==========================================

def main():

    while True:

        try:

            choice = menu()

            if choice == "1":
                add_income_menu()

            elif choice == "2":
                add_expense_menu()

            elif choice == "3":
                view_menu()

            elif choice == "4":
                update_menu()

            elif choice == "5":
                delete_menu()

            elif choice == "6":
                search_menu()

            elif choice == "7":
                summary_menu()

            elif choice == "8":
                export_menu()

            elif choice == "9":
                charts_menu()

            elif choice == "10":
                reports_menu()

            elif choice == "11":

                exit_program()

                break

            else:

                print("\n❌ Invalid Choice. Please try again.")

                pause()

        except KeyboardInterrupt:

            print("\n\nProgram Interrupted by User.")

            break

        except Exception as e:

            print(f"\n❌ Error : {e}")

            pause()


# ==========================================
# Run Application
# ==========================================

if __name__ == "__main__":

    main()