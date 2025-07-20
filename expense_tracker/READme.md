# 💸 Expense Tracker

A simple, interactive command-line **Expense Tracker** built with Python!  
Track your daily spending, categorize your expenses, and get instant summaries—right from your terminal.

---

## ✨ Features

- **➕ Add Expense:** Quickly log a new expense with details.
- **📋 View All Expenses:** See all your expense entries in a neat list.
- **🧮 View Total Expenses:** Instantly know your total spending.
- **🔍 Filter by Category:** Focus on specific categories (e.g., Food, Travel).
- **📊 Expense Summary:** View spending breakdowns by category.
- **🚪 Exit:** Quit the tracker anytime.

---

## 🚀 Getting Started

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/expense-tracker.git
    cd expense-tracker
    ```
2. **Run the Tracker:**
    ```bash
    python expense_tracker.py
    ```

---

## 📖 How to Use

You'll be greeted with a menu:

```
--- Expense Tracker Menu ---
1. Add Expense
2. View All Expenses
3. View Total Expenses
4. View Expenses by Category
5. Summarize Expenses by Category
6. Exit
```
- **Choose an option** (1-6) and follow the prompts.
- **Amounts** should be positive numbers.
- **Categories** are case-insensitive (e.g., "food" and "Food" are treated the same).

---

## 🛠️ Main Functions

- `add_expense(description, amount, category)`  
  Add a new expense with a description, amount (₹), and category.
- `view_expenses()`  
  Show all logged expenses.
- `get_total_expenses()`  
  Calculate and display your total spending.
- `get_expenses_by_category(category)`  
  Show expenses only for a chosen category.
- `summarize_expenses_by_category()`  
  Get totals for each category.
- `main_menu()`  
  The interactive menu loop—your starting point!

---

## 🔎 Example

```text
Enter your choice: 1
Enter description: Coffee
Enter amount: 50
Enter category: Food
Expense 'Coffee' (₹50.00) added successfully.

Enter your choice: 5

--- Expense Summary by Category ---
Food: ₹50.00
-----------------------------------
```

---

## 📦 Requirements

- Python 3.x

---

## 📢 Notes & Tips

- All data is stored **in memory**—it resets every time you exit.
- Make sure to enter valid, positive amounts.
- Get creative with categories: "Books", "Groceries", "Entertainment", etc.

---

## 🪪 License

This project is open-source and free to use.

---

> **Made with ❤️ in Python**

