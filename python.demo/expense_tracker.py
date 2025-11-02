"""A simple Command Line Expense tracker in Python for personal expenses."""

import json
from datetime import datetime
from pathlib import Path

# Store data alongside this script
DATA_FILE = Path(__file__).with_suffix(".json")


def load_expenses():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        # If the file exists but is corrupted, start fresh
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(amount, category, description=""):
    expenses = load_expenses()
    new_entry = {
        "amount": float(amount),
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    expenses.append(new_entry)
    save_expenses(expenses)
    print(f"✅ Added: ${amount} for {category}")


def calculate_total_by_category(category):
    expenses = load_expenses()
    return round(sum(e.get("amount", 0) for e in expenses if e.get("category") == category), 2)


def get_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = round(sum(e.get("amount", 0) for e in expenses), 2)
    categories = sorted(set(e.get("category") for e in expenses if e.get("category")))

    print("\n📊 Expense Summary")
    print(f"Total spent: ${total}")
    for c in categories:
        print(f" - {c}: ${calculate_total_by_category(c)}")


if __name__ == "__main__":
    # Demo usage
    add_expense(15.75, "Food", "Lunch at cafe")
    add_expense(100.40, "Groceries", "Weekly groceries")
    add_expense(50.69, "Entertainment", "Streaming service")
    get_summary()
