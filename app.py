import json
import os

FILE="expenses.json"

def load_expenses():
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            return json.load(f)
    return[]
    
def save_expenses(expenses):
    with open(FILE,"w") as f:
        json.dump(expenses,f,indent=4)
        
def add_expense(expenses):
    category=input("category(food/travel/other):")
    amount=float(input("Amount: "))
    note=input("Note: ")
    expenses.append({"category":category, "amount":amount,"note":note})
    save_expenses(expenses)
    print("Expense added!")
    
def view_expenses(expenses):
    for i,e in enumerate(expenses,1):
        print(f"{i},{e['category']}-₹{e['amount']}-{e['note']}")
        
def main():
    expenses=load_expenses()
    while True:
        print("\n--- Expense Tracker ---\n")
        print("1. Add Expense ")
        print("2. View Expenses ")
        print("3. Exit ")
        
        choice=input("choose: ")
        
        if choice=="1":
            add_expense(expenses)
        elif choice=="2":
            view_expenses(expenses)
        elif choice=="3":
            print("Bye!")
            break
        else:
            print("invalid choice!")
main()
        