import json
from datetime import datetime

# add expenses with amount date and category
# view total expenses 
# filter expenses by category and date 
# save/load data from a file 

class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime("%Y-%m-%d")
        }

class Expense_calculator:
    def __init__(self):
        self.expenses = []

    def add_expenses(self, amount, category, date):
        date = datetime.strptime(date, "%Y-%m-%d")
        expense = Expense(amount, category, date)
        self.expenses.append(expense)
        print("Expense Added")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to show.")
        for e in self.expenses:
            print(f"On Date: {e.date.strftime('%Y-%m-%d')} you spent Rupees {e.amount} on {e.category}")

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"The total amount of money you have spent: {total}")

    def save_to_file(self, filename="expenses.json"):
        with open(filename, "w") as f:
            json.dump([e.to_dict() for e in self.expenses], f)
        print("Saved to file.")

    def load_from_file(self, filename="expenses.json"):
        try:
            with open(filename, "r") as f:
                content = f.read().strip()
                if not content:
                    print("No saved data found.")
                    return
                data = json.loads(content)
                self.expenses = []  # Clear existing expenses to avoid duplicates
                for item in data:
                    date_obj = datetime.strptime(item["date"], "%Y-%m-%d")
                    expense = Expense(float(item["amount"]), item["category"], date_obj)
                    self.expenses.append(expense)
            print("Loaded from file.")
        except FileNotFoundError:
            print("No saved data found.")
        except json.JSONDecodeError:
            print("Corrupted data file. Please delete or fix expenses.json.")

tracker = Expense_calculator()
tracker.load_from_file()

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Total Spent\n4. Save & Exit")
    choice = input("Choose: ")

    if choice == '1':
        try:
            amt = float(input("Amount: ₹"))
            cat = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            tracker.add_expenses(amt, cat, date)
        except ValueError:
            print("Invalid input. Please enter the correct data types.")
    elif choice == '2':
        tracker.view_expenses()
    elif choice == '3':
        tracker.total_spent()
    elif choice == '4':
        tracker.save_to_file()
        break
    else:
        print("Invalid option!")