from datetime import datetime
import json

class InsufficentFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass


class Transaction:
    def __init__(self, amount, type_):
        self.amount = amount
        self.type = type_
        self.time = datetime.now().strftime("%y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.time} | {self.type.upper()} | ₹{self.amount}"

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


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.transactions = []
        self.load_from_file()

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")

        self.__balance += amount
        self.transactions.append(Transaction(amount, "Deposit"))
        print(f"Deposit ₹{amount} successful")
        self.save_to_file()

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")

        if amount > self.__balance:
            raise InsufficentFundsError("Not enough balance")

        self.__balance -= amount
        self.transactions.append(Transaction(amount, "Withdraw"))
        print("Withdraw successful")
        self.save_to_file()

    def save_to_file(self):
        data = {
            "owner": self.owner,
            "balance": self.__balance,
            "transactions": [t.to_dict() for t in self.transactions]
        }

        with open("bank_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self):
        try:
            with open("bank_data.json", "r") as file:
                data = json.load(file)

                if data["owner"] != self.owner:
                    return  # prevent loading wrong account

                self.__balance = data["balance"]
                self.transactions = [
                    Transaction.from_dict(t)
                    for t in data["transactions"]
                ]

        except FileNotFoundError:
            pass

    def show_balance(self):
        print(f"Current balance: ₹{self.__balance}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet")
            return

        for t in self.transactions:
            print(t)


account = BankAccount("Barsha",5000)

while True:
    print("\n🏦 BANK MENU")
    print("1. Deposit")
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
        if choice ==1:
            amount = float(input("Enter the amount: "))
            account.deposit(amount)
        
        elif choice ==2:
            amount = float(input("Enter the amount: "))
            account.withdraw(amount)
        
        elif choice ==3:
            account.show_balance()
        
        elif choice ==4:
            account.show_transactions()
        
        elif choice==5:
            print("GoodBye..!")
            break

        else:
            print("Invalid choice")
    
    except (InsufficentFundsError,InvalidAmountError) as e:
        print("Error:", e)