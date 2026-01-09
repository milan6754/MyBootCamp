#==================Expenses Traker================
import json 
from datetime import date 

class ExpensesTracker:
    def __init__(self, file_name="expenses.json"):
        self.file_name= file_name
        self.expenses = self.load_expenses()
    
    def load_expenses(self):
        try:
            with open(self.file_name,"r") as file:
                return json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
            return []
    
    def save_expenses(self):
        with open(self.file_name,"w") as file:
            json.dump(self.expenses,file,indent=4)
            
    def add_task(self,amount,category,note=""):
        expenses={
            'amount':amount,
            'category':category,
            'note':note,
            'date':date.today().isoformat()
        }
        self.expenses.append(expenses)
        self.save_expenses()
        print("Expenses Added!")
    
    def show_expenses(self):
        if not self.expenses:
            print("No expenses found!")
            return
        for i,exp in enumerate(self.expenses,1):
            print(f"{i}. ${exp['amount']} | {exp['category']} | {exp['date']} | {exp['note']}")
    
    def total_spending(self):
        total = sum(exp['amount'] for exp in self.expenses)
        print(f"Total spend:{total}")
    

    def filter_by_category(self,category):
        found = False

        for exp in self.expenses:
            if exp['category'].lower()==category.lower():
                print(f"${enumerate({exp['amount']} | {exp['date']} | {exp['note']})}")
            
                found = True
        if not found:
            print("No expenses Found.")
    
    def delete_expenses(self,index):
       
            if 1<=index <=len(self.expenses):
                del self.expenses[index-1]
                self.save_expenses()
                print(f"{self.expenses[index]} is deleted.")
            else:
                print("Invalid index")
       
        
        


def menu():
    print("\n📊 EXPENSE TRACKER")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Total spent")
    print("4. Filter by category")
    print("5. Delete Expenses")
    print("6. Exit")
    
tracker = ExpensesTracker()

while True:
    menu()
    try:
        choice = int(input("Enter the choice: "))
    
    except ValueError:
        print("Enter a number")
        continue

    if choice ==1:
        try:
            amount = float(input("Amount: "))
            category = input("Category: ")
            note = input("Note (optional): ")
            tracker.add_task(amount,category,note)
        except ValueError:
            print("Amount must be number")

    elif choice==2:
        tracker.show_expenses()
    elif choice ==3:
        tracker.total_spending()
    
    elif choice ==4:
        category = input("Enter the category: ")
        tracker.filter_by_category(category)
    
    elif choice ==5:
        tracker.show_expenses()
        try:
          index = int(input("Enter the number: "))
          tracker.delete_expenses(index)
        except ValueError:
            print("index must be number.")

    elif choice ==6:
        print("GoodBye")
        break
    else:
        print("Invald choice")


