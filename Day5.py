#====================Random Number==================
'''import random
high = 100
low = 1
option = ("Rock", "Paper", "Scissor")
cards = ["2","3","4","5","6","7","8","9","A","K","Q"]
number = random.randint(low,high)
#number = random.random() # it will give random number between 0 to 1 
option = random.choice(option)
random.shuffle(cards)
print(cards)
print(number) 
print(option)'''

#=================Python number guessing game=======================
'''import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num,highest_num)
guesses = 0 
is_running = True

print("++++++++Python Number Guessing Game+++++")
print(f"Select the number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses+=1

        if guess<lowest_num or guess>100:
            print(f"{guess} is out of range")
            print(f"Select the number between {lowest_num} and {highest_num}")

        elif guess<answer:
            print("Too low ! Try again..")
        elif guess > answer:
            print("Too high! Try again..")
        else:
            print(f"Correct ! your guess {guess} is correct ")
            print(f"Number of guesses {guesses}")
    else:
        print(f"Invalid guess:{guess}")
        print(f"Select the number between {lowest_num} and {highest_num}")'''

#=================Rock,Papper,scissor===============
'''import random
option = ("rock","papper","scissor")
running = True
user_score = 0 
computer_score= 0 
while running:
    Player = None
    computer= random.choice(option)
    
    while Player not in  option:
        Player = input("Enter a choice (Rock , Paper, Scissor): ").lower()

        print(f"Computer:{computer}")
        print(f"Player:{Player}")

        if Player == computer:
            print("It's a Tie")

        elif Player=="rock" and computer=="scissor":
            print("You win!")
            user_score+=1
            
        elif Player =="paper" and computer =="rock":
            print("You win")
            user_score+=1
        elif Player =="scissor" and computer == "paper":
            print("You win!")
            user_score+=1
        else:
            print("You lose! ")
            computer_score+=1

    Player_again = input("Enter Y/N:").lower()
    if Player_again =="n":
        running = False
print("=======Score board======")
print(f"computer score {computer_score}")
print(f"user_score {user_score}")
if user_score>computer_score:
    print(f"you win in overall score ")
else:
    print(f"Computer win in overall score")
print("Thank You for Playing game...")'''


#===============Dice Roller Game===============

import random

#print("\u25CF \u250c \u2500 \u2510 \u2502 \u2514 \u2518")

#● ┌ ─ ┐ │ └ ┘


"┌─────────┐"
"│         │"
"│    ●    │"
"│         │"
"└─────────┘"

dice_art = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│      ●  │",
       "└─────────┘"),
   3: ("┌─────────┐",
       "│  ●      │",
       "│    ●    │",
       "│      ●  │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘"),

    
}
com_art = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│      ●  │",
       "└─────────┘"),
   3: ("┌─────────┐",
       "│  ●      │",
       "│    ●    │",
       "│      ●  │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘"),

    
}

dice = []
total = 0
player_amount = 0 
amount = int(input("Enter the amount you want to bet:$ "))
num_of_dice = int(input("Enter many dice: "))
computer_amount = 1000000000
com_dic = []
com_total=0
low = 1
high = 6


print("===========Your Luck=============")
for die in range(num_of_dice):
    dice.append(random.randint(1,6))

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end="")
    print()

for die in dice:
    total+=die
print(f"Total:{total}")
print("==========computer luck==========")
for com in range(num_of_dice):
    com_dic.append(random.randint(low,high))

for line in range(5):
    for die in com_dic:
        print(com_art.get(die)[line],end="")
    print()
for com in com_dic:
    com_total += com
print(f"Total: {com_total}")

if total> com_total:
    print("You Won")
    computer_amount-=amount
    player_amount +=amount *2
    

else:
    print("You lose")

print(f"You won: ${player_amount}")



