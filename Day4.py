#collection = single vaieable used to store multiple values 
#List = [] Ordered , changable , dublicate approve
#Tuple = () Ordered , unchangable , dublicate ok , faster 
#set = {}  unordered, immutable , add/remove ok , dublicate not ok 

#==============List==============================

#fruits = ["apple","orange","banana","grapes"]

#print(fruits)
#print(fruits[3]) #get element using index
#print(fruits[:2]) # slicing
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#fruits[0]= "coconut"

#fruits.append("pineapple")
#fruits.remove("banana")
#fruits.insert(0,"Papaya")
#print("apple" in fruits)
#fruits.sort()

#fruits.reverse()
#fruits.clear()

#print(fruits.index("apple"))
#print(fruits.count("banana"))
#print(fruits)

#==============SETs====================

#fruits = {"apple","orange","banana","grapes"}

#fruits.add("pineapple")
#fruits.remove("grapes")
#fruits.pop()
#fruits.clear()
#print(fruits)


#=================Tuples=====================
#fruits = ("apple","orange","banana","grapes")


#print(fruits.index("apple"))
#print(fruits.count("banana"))


#===============Shopping cart==================

'''foods = []
prices = []
total = 0 

while True: 
    food = input("Enter the food you to buy(q for quit): ")
    if food.lower() =="q":
        break
    else:
        price = float(input("Enter the price of {food}:$ "))
        foods.append(food)
        prices.append(price)

print(foods)


print("===========Your CART==============")

for food in foods:
    print(food,end=" ")
for price in prices:
    total +=price
print()
print(f"Your total is : ${total}")'''




#=============2D collection =================

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potato"],
             ["buffelo", "chicken", "mutton"]]

#print(groceries[0]) # to get fruits list 1 for vegetables, 3 for meats
#print(groceries[0][0]) # To get apple from fruits in 2d list 
#print(groceries[1][1]) # it will get 1 index 1 elememnt of the index which is carrots

#for collection in groceries:
    #print(collection)

#for collection in groceries:
#    for coll in collection:
#        print(coll).  # nested loop in groceries

'''num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*" ,0,"#"))


for row in num_pad:
    for ro in row:
        print(ro,end=" ")
    print()'''


#==============PYTHON QUIZ GAME=============

'''questions=("Which planet is known as the “Red Planet”?",
           "What is the capital of Japan?",
           "How many sides does a hexagon have?",
           "Which gas do plants absorb from the atmosphere?",
           "If 5 machines take 5 minutes to make 5 items, how long will 1 machine take to make 1 item?")
options = (("A. Venus", "B. Jupiter", "C. Mars", "D. Mercury"),
           ("A. Seoul", "B. Beijing", "C. Tokyo", "D. Bangkok"),
           ("A. 5", "B. 6", "C. 7", "D. 8"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon dioxid", "D. Hydrogen"),
           ("A. 1 min", "B. 5min", "C. 10min", "D. 25min"),)
answers = ("c","c","b","c","b")
guesses = []
score = 0 

question_no=0

for question in questions:
    print("-----------------------------------------------")
    print(question)
    for option in options[question_no]:
        print(option)

    guess = input("Enter (A, B, C, D): ").lower()
    guesses.append(guess)
    if guess == answers[question_no]:
        score+=1
        print("Correct")
    else: 
        print("Incorrect")
        print(f"{answers[question_no]} is the correct answer ")
    question_no +=1

print("-----------------------------")
print("           RESULT            ")
print("-----------------------------")
print("Correct answer: ",end=" ")
for answer in answers:
    print(answer,end=" | ")

print()
print("Your answer:   ", end=" ")
for gues in guesses:
    print(gues, end=" | ")

print()

score =  int(score /len(question) * 100)
print(f"Your  score is : {score}%")'''


#================Dictonary====================
# It is the collection of key and value pair data 
# Ordered and changable , no dublicate 

capitals = { 
    "nepal": "Kathmandu",
    "japan": "Tokyo",
    "china": "beijing",
    "Russia":"Moscow"
}
#print(capitals.get("nepal"))

#if capitals.get("japan"):
#    print("yes it exist")
#else:
#    print("It doesnt exist")

#capitals.update({"Germany":"Berlin"})
#capitals.pop("japan")
#capitals.popitem()
#capitals.clear()

'''for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

for overall in capitals.items():
    print(overall)'''

#Concession stand program

menu = {
    "pizza":5.6,
    "nachos":4.20,
    "fries":2.0,
    "chicken":5.55,
    "buff":6.54
}
cart = []
total = 0
print("-----------MENU-------------")
for key, value  in menu.items():
    print(f"{key:10}:{value:.2f}")

print("----------------------------")


while True:
    food= input("Enter the food you like to buy(q for quit): ").lower()
    if food =="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print()
print(f"Total is: {total:.2f}")