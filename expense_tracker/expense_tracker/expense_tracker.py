import json
import os

# Global list to store expenses
expenses = []
# Define the filename for saving/loading expenses
EXPENSE_FILE = 'expenses.json'

def load_expenses():
    """Loads expenses from the JSON file into the global expenses list."""
    global expenses
    if os.path.exists(EXPENSE_FILE):
        try:
            with open(EXPENSE_FILE, 'r') as f:
                expenses = json.load(f)
            print(f"Loaded {len(expenses)} expenses from '{EXPENSE_FILE}'.")
        except json.JSONDecodeError:
            print(f"Error reading '{EXPENSE_FILE}'. Starting with an empty list.")
            expenses = []
        except Exception as e:
            print(f"An unexpected error occurred while loading expenses: {e}")
            expenses = []
    else:
        print("No existing expense file found. Starting with an empty list.")

def save_expenses():
    """Saves the current expenses list to the JSON file."""
    try:
        with open(EXPENSE_FILE, 'w') as f:
            json.dump(expenses, f, indent=4) # indent for pretty printing JSON
        print(f"Saved {len(expenses)} expenses to '{EXPENSE_FILE}'.")
    except Exception as e:
        print(f"Error saving expenses to '{EXPENSE_FILE}': {e}")

def add_expense(description, amount, category):
    """Adds a new expense to the list."""
    try:
        amount = float(amount)
        if amount <= 0:
            print("Amount must be a positive number.")
            return
        expense = {'description': description, 'amount': amount, 'category': category}
        expenses.append(expense)
        print(f"Expense '{description}' (₹{amount:.2f}) added successfully.")
        save_expenses() # Save after adding
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses():
    """Displays all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses):
        print(f"{i+1}. Description: {expense['description']}, Amount: ₹{expense['amount']:.2f}, Category: {expense['category']}")
    print("--------------------")

def get_total_expenses():
    """Calculates and returns the total of all expenses."""
    total = sum(map(lambda expense: expense['amount'], expenses))
    return total

def get_expenses_by_category(category):
    """Filters expenses by a given category and returns them."""
    filtered_expenses = list(filter(lambda expense: expense['category'].lower() == category.lower(), expenses))
    return filtered_expenses

def summarize_expenses_by_category():
    """Summarizes expenses, showing total amount per category."""
    if not expenses:
        print("No expenses to summarize.")
        return

    category_totals = {}
    for expense in expenses:
        category = expense['category'].lower()
        amount = expense['amount']
        category_totals[category] = category_totals.get(category, 0) + amount

    print("\n--- Expense Summary by Category ---")
    for category, total in category_totals.items():
        print(f"{category.capitalize()}: ₹{total:.2f}")
    print("-----------------------------------")

def delete_expense():
    """Deletes an expense based on its index."""
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses() # Show expenses with their numbers
    try:
        index_to_delete = int(input("Enter the number of the expense to delete: "))
        if 1 <= index_to_delete <= len(expenses):
            deleted_expense = expenses.pop(index_to_delete - 1)
            print(f"Expense '{deleted_expense['description']}' (₹{deleted_expense['amount']:.2f}) deleted successfully.")
            save_expenses() # Save after deleting
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred while deleting the expense: {e}")

def edit_expense():
    """Edits an existing expense based on its index."""
    if not expenses:
        print("No expenses to edit.")
        return

    view_expenses() # Show expenses with their numbers
    try:
        index_to_edit = int(input("Enter the number of the expense to edit: "))
        if 1 <= index_to_edit <= len(expenses):
            expense = expenses[index_to_edit - 1]
            print(f"Editing expense: {expense['description']}, Amount: ₹{expense['amount']:.2f}, Category: {expense['category']}")

            new_description = input(f"Enter new description (current: {expense['description']}): ") or expense['description']
            new_amount_str = input(f"Enter new amount (current: {expense['amount']:.2f}): ")
            new_category = input(f"Enter new category (current: {expense['category']}): ") or expense['category']

            # Validate new amount
            if new_amount_str:
                try:
                    new_amount = float(new_amount_str)
                    if new_amount <= 0:
                        print("Amount must be a positive number. Expense not updated.")
                        return
                    expense['amount'] = new_amount
                except ValueError:
                    print("Invalid amount. Expense amount not updated.")
                    return
            
            expense['description'] = new_description
            expense['category'] = new_category
            
            print("Expense updated successfully.")
            save_expenses() # Save after editing
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred while editing the expense: {e}")

def main_menu():
    """Displays the main menu and handles user interaction."""
    load_expenses() # Load expenses when the program starts

    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. Summarize Expenses by Category")
        print("6. Edit Expense")    # New feature
        print("7. Delete Expense")  # New feature
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            add_expense(description, amount, category)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total = get_total_expenses()
            print(f"\nTotal expenses: ₹{total:.2f}")
        elif choice == '4':
            category_filter = input("Enter category to filter by: ")
            filtered = get_expenses_by_category(category_filter)
            if filtered:
                print(f"\n--- Expenses in Category: {category_filter.capitalize()} ---")
                for expense in filtered:
                    print(f"Description: {expense['description']}, Amount: ₹{expense['amount']:.2f}")
                print("---------------------------------------------")
            else:
                print(f"No expenses found for category '{category_filter}'.")
        elif choice == '5':
            summarize_expenses_by_category()
        elif choice == '6': # Call the new edit function
            edit_expense()
        elif choice == '7': # Call the new delete function
            delete_expense()
        elif choice == '8':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
