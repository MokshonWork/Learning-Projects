expenses = [] 

def add_expense(description, amount, category):
    try:
        amount = float(amount)
        if amount <= 0:
            print("Amount must be a positive number.")
            return
        expense = {'description': description, 'amount': amount, 'category': category}
        expenses.append(expense)
        print(f"Expense '{description}' (₹{amount:.2f}) added successfully.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses):
        # Using f-strings for formatted output
        print(f"{i+1}. Description: {expense['description']}, Amount: ₹{expense['amount']:.2f}, Category: {expense['category']}")
    print("--------------------")

def get_total_expenses():
    total = sum(map(lambda expense: expense['amount'], expenses))
    return total

def get_expenses_by_category(category):
    
    filtered_expenses = list(filter(lambda expense: expense['category'].lower() == category.lower(), expenses))
    return filtered_expenses

def summarize_expenses_by_category():
   
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
        print(f"{category.capitalize()}: ₹{total:.2f}")
    print("-----------------------------------")

def main_menu():
    
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
        elif choice == '6':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
