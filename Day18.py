from datetime import datetime
import json

# ---------------- Custom Exceptions ----------------
class InsufficentAmountError(Exception):
    pass

class InvaliAmountError(Exception):
    pass

# ---------------- Transaction Class ----------------
class Transaction:
    def __init__(self, amount, type_):
        self.amount = amount
        self.type = type_
        self.time = datetime.now().strftime("%y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.time} | ₹{self.amount} | {self.type}"

    def to_dict(self):
        return {
            "amount": self.amount,
            "type": self.type,
            "time": self.time
        }

    @staticmethod
    def from_dict(data):
        t = Transaction(data["amount"], data["type"])
        t.time = data["time"]
        return t

# ---------------- BankAccount Class ----------------
class BankAccount:
    def __init__(self, owner, initialAmount=0):
        self.owner = owner
        self.file_name = f"{owner.lower()}.json"  # each account has its own file
        self.__balance = initialAmount
        self.transactions = []
        self.load_from_file()

    # Save account data to JSON
    def save_to_file(self):
        data = {
            "owner": self.owner,
            "balance": self.__balance,
            "transactions": [t.to_dict() for t in self.transactions]
        }
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    # Load account data from JSON
    def load_from_file(self):
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)
                self.__balance = data["balance"]
                self.transactions = [Transaction.from_dict(t) for t in data["transactions"]]
        except FileNotFoundError:
            pass  # file doesn't exist, start fresh

    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            raise InvaliAmountError("Amount must be positive")
        self.__balance += amount
        self.transactions.append(Transaction(amount, "Deposit"))
        print("Deposit successful!")
        self.save_to_file()

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            raise InvaliAmountError("Amount must be positive")
        if amount > self.__balance:
            raise InsufficentAmountError("Not enough balance")
        self.__balance -= amount
        self.transactions.append(Transaction(amount, "Withdraw"))
        print("Withdraw successful!")
        self.save_to_file()

    # Show current balance
    def show_balance(self):
        print(f"Current balance: ₹{self.__balance}")

    # Show transaction history
    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        for t in self.transactions:
            print(t)

# ---------------- Main Program ----------------
# Create multiple accounts (predefined)
accounts = {
    "Barsha": BankAccount("Barsha", 5000),
    "Milan": BankAccount("Milan", 1000000)
}

# Choose account once
print("Available accounts:", ", ".join(accounts.keys()))
current_account_name = input("Choose account to operate: ")

if current_account_name not in accounts:
    print("Account not found! Exiting...")
    exit()

account = accounts[current_account_name]
print(f"Using account: {current_account_name}")

while True:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Show Transactions")
    print("5. Exit")

    try:
        choice = int(input("Enter the choice: "))
    except ValueError:
        print("Enter a number")
        continue

    try:
        if choice == 1:
            amount = float(input("Enter the amount: "))
            account.deposit(amount)
        
        elif choice == 2:
            amount = float(input("Enter the amount: "))
            account.withdraw(amount)
        
        elif choice == 3:
            account.show_balance()
        
        elif choice == 4:
            account.show_transactions()
        
        elif choice == 5:
            print("GoodBye..!")
            break

        else:
            print("Invalid choice")
    
    except (InsufficentAmountError, InvaliAmountError) as e:
        print("Error:", e)
