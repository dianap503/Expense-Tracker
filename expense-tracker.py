import argparse
import os
import json
import datetime

file_name = "expenses.json"

def initialize_file():
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump([], file)

def load_expenses():
    with open(file_name, 'r') as file:
        return json.load(file)

def save_expense(expenses):
    with open(file_name, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(description, amount, expenses):
    new_id = max((e['ID'] for e in expenses), default=0) + 1 #daca expenses e goala va da eroare, valoarea de default este 0
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    new_expense = {
        "ID": new_id ,
        "Date": now ,
        "Description": description ,
        "Amount": amount 
    }
    expenses.append(new_expense)
    save_expense(expenses)
    print(f"Expense added successfully (ID: {new_id})")

def delete_expense(id, expenses):
    expenses = [e for e in expenses if e['ID'] != id]
    save_expense(expenses)
    print("Expense deleted successfully!")

def get_month_name(month_number):
    months_name = [
        "", "January", "February", "March", "April", 
        "May", "June", "July", "August", "September", 
        "October", "November", "December"
    ]
    return months_name[month_number]

def summarize_expenses(expenses, month):
    total = 0
    if month is None:
        total = sum(e['Amount'] for e in expenses)
        print(f"Total expenses: ${total}")
    else:
        for e in expenses:
            data = e['Date'].split("-")
            if str(month).zfill(2) == data[1]:
                total += e['Amount']
        month_number = int(month)
        if 1 <= month_number <= 12:
            month_name = get_month_name(month_number)
            print(f"Total expenses for {month_name}: ${total}")
        else:
            print("Error: Invalid month.")

def list_expenses(expenses):
    print(f"{'ID':<4} {'Date':<12} {'Description':<15} {'Amount':<10}")
    for e in expenses:
        # :<4 înseamnă "align la stânga, lățime 4 caractere"
        print(f"{e['ID']:<4} {e['Date']:<12} {e['Description']:<15} ${e['Amount']:<10}")
    

def main():
    initialize_file()
    expenses = load_expenses()

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", type=float, required=True)

    subparsers.add_parser("list")
    
    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=str, required=False)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount, expenses)
    elif args.command == "list":
        list_expenses(expenses)
    elif args.command == "summary":
        summarize_expenses(expenses, args.month)
    elif args.command == "delete":
        delete_expense(args.id, expenses)

if __name__ == "__main__":
        main()

