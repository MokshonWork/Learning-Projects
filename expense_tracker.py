# expense_tracker.py

# A list to store our expenses. Each expense will be a dictionary.
# Example: {'description': 'Groceries', 'amount': 50.0, 'category': 'Food'}
expenses = [] 

def add_expense(description, amount, category):
    """
    Adds a new expense to the tracker.

    Args:
        description (str): A brief description of the expense.
        amount (float): The monetary amount of the expense.
        category (str): The category of the expense (e.g., 'Food', 'Transport', 'Utilities').
    """
    try:
        amount = float(amount)
        if amount <= 0:
            print("Amount must be a positive number.")
            return
        expense = {'description': description, 'amount': amount, 'category': category}
        expenses.append(expense)
        print(f"Expense '{description}' (${amount:.2f}) added successfully.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses():
    """
    Displays all recorded expenses.
    """
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses):
        # Using f-strings for formatted output
        print(f"{i+1}. Description: {expense['description']}, Amount: ${expense['amount']:.2f}, Category: {expense['category']}")
    print("--------------------")

def get_total_expenses():
    """
    Calculates the total sum of all expenses using a lambda function.
    """
    # Lambda function to extract the 'amount' from each expense dictionary
    # and then sum them up.
    # sum() expects an iterable of numbers. map() applies the lambda to each item.
    total = sum(map(lambda expense: expense['amount'], expenses))
    return total

def get_expenses_by_category(category):
    """
    Filters expenses by a specific category using a lambda function.

    Args:
        category (str): The category to filter by.

    Returns:
        list: A list of expenses belonging to the specified category.
    """
    # Lambda function to check if an expense's category matches the given category.
    # filter() applies the lambda to each item and returns items for which the lambda is true.
    filtered_expenses = list(filter(lambda expense: expense['category'].lower() == category.lower(), expenses))
    return filtered_expenses

def summarize_expenses_by_category():
    """
    Summarizes total expenses for each category.
    """
    if not expenses:
        print("No expenses to summarize.")
        return

    category_totals = {}
    for expense in expenses:
        category = expense['category'].lower()
        amount = expense['amount']
        # If the category is not in the dictionary, initialize it to 0, then add the amount.
        category_totals[category] = category_totals.get(category, 0) + amount

    print("\n--- Expense Summary by Category ---")
    for category, total in category_totals.items():
        print(f"{category.capitalize()}: ${total:.2f}")
    print("-----------------------------------")

def main_menu():
    """
    Displays the main menu and handles user input.
    """
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. Summarize Expenses by Category")
        print("6. Exit")
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
            print(f"\nTotal expenses: ${total:.2f}")
        elif choice == '4':
            category_filter = input("Enter category to filter by: ")
            filtered = get_expenses_by_category(category_filter)
            if filtered:
                print(f"\n--- Expenses in Category: {category_filter.capitalize()} ---")
                for expense in filtered:
                    print(f"Description: {expense['description']}, Amount: ${expense['amount']:.2f}")
                print("---------------------------------------------")
            else:
                print(f"No expenses found for category '{category_filter}'.")
        elif choice == '5':
            summarize_expenses_by_category()
        elif choice == '6':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
