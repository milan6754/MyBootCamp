#===============Python Banking Program=======================
#1.show balance
#2.deposit
#3.withdraw

'''def show_balance(balance):
    print("***********************************")
    print(f"Your balance is $: {balance:.2f}")
    print("***********************************")

def deposit():
    amount = float(input("Enter an amount to deposit:$ "))
    if amount<0:
        print("Not Valid Amount")
        return 0 
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the withdraw amount:$ "))
    if amount <0:
        print("Not valid Amount")
        return 0 
    elif balance<amount:
        print("Insufficent balance")
        return 0 
        
    else:
        return amount



def main():
    balance =  0 
    is_running=True

    while is_running:
        print("**************************")
        print("    Banking program")
        print("**************************")

        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("**************************")
        choice = input("Enter the choice(1-4): ")

        if choice =='1':
            show_balance(balance)
        elif choice =='2':
            balance+=deposit()
        elif choice =='3':
            balance-=withdraw(balance)

        elif choice =='4':
            is_running=False
        else:
            print("Invalid Input!")

    print("Thank you for using our banking system")

if __name__ =="__main__":
    main()'''


#============Python slot machine==============
import random
def spin_row():
    symbols = [ '🍒' ,'🍉' , '🍋', '🔔', '⭐️']
    result = []

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("*****************")
    print(" | ".join(row))
    print("*****************")

def get_payout(row, bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet * 3 
        elif row[0]=='🍉':
            return bet * 4
        elif row[0]=='🍋':
            return bet *5
        elif row[0]=='🔔':
            return bet*10
        elif row[0]=='⭐️':
            return bet *20
        
    return 0 

    

def main():
    balance = 100
    print("*****************************")
    print("Welcome to Python slot game ")
    print("Symbol: (🍒*3) (🍉*4) (🍋*5) (🔔*10) (⭐️*20)")
    print("*****************************")

    while balance> 0:
        print(f"Currrent balance: ${balance}")
        
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please Enter a valid number ")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficent balance")
            continue
        if bet<=0:
            print("Bet must be greater than 0")
            continue
        balance-=bet

        row = spin_row()
        print("Spinning......\n")
        print_row(row)
        payout= get_payout(row,bet)

        if payout > 0 :
            print(f"You won $: {payout}")
        else:
            print(f"Sorry you lost this time..")
        balance += payout

        play_again = input("Do you want to play again:(Y/N)").lower()
        if play_again != 'y':
            break


    print(f"Game over ! Your final balance is ${balance}")

if __name__ == "__main__":
    main()