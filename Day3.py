#================Indexing ============== 
# accessing element of sequence using []
#[start:stop:step]

credit_number= '1234-567-890-123'
last_digit = credit_number[-3:]
reverse = credit_number[::-1]
'''print(credit_number[2])
print(credit_number[0:4])
print(credit_number[5:8])
print(credit_number[-1])
print(credit_number[::2])
print(last_digit)

print(f"XXX-XXX-XXX-{last_digit}")
print(reverse)'''


#===============Format-specifiers ============
# {:flags} format a value based on what flags  are inserted 

price1 = 3000.223153
price2 = 84300.33
price3 = 12000.55

'''print(f"Price 1 is : {price1:,.2f}")
print(f"Price 1 is : {price2:,.2f}")
print(f"Price 1 is : {price3:,.2f}")'''


#================while loops =====================
#Execute code until some condition remains true

'''name = input("Enter your name: ")
 
while name =="":
    print("You didnt enter your name")
    name = input("Enter your name: ")
print(f"Hello, {name}")'''


'''age = int(input("Enter your age: "))

while age<0:
    print("Age cannt be negative ")
    age = int(input("Enter your age: "))

print(f"so you are {age} year old ")'''

'''food = input("Enter the food you like (q  to quit): ")

while not food=="q":
    print(f"You like {food}")
    food = input("Enter the food you like (q  to quit): ")

print("SAYONARA")'''

'''num = int(input("~Enter the number: "))

while num<1 or num>10:
    print("Invaid Number")
    num = int(input("enter the number between 1 to 10: "))

print(f"Your number is {num}")'''

#Python compound interest calculator 
'''principle = 0 
rate = 0 
time = 0 

while principle <= 0:
    principle = int(input("Enter the value of Principle: "))
    if principle <=0:
        print("Principle cannot be less  or equal to zero ")
while rate<= 0:
    rate = int(input("Enter the value of Interest rate : "))
    if principle <=0:
        print("Interest rate cannot be less  or equal to zero ")
while time<= 0:
    time= int(input("Enter the time: "))
    if principle <=0:
        print("time cannot be less  or equal to zero ")
total = principle * pow((1+rate/100),time)

print(f"Amount after {time} years : ${total:,.2f}")'''


#=============For Loops======================
#execute a block of code a fixed number of times 
#You can iterate over a range , string sequence etc

'''for i in range(1,10,2):
    print(i)

for i in range(1,10):
    if i%2==0:
        print(f"{i} is Odd")
    else:
        print(f"{i} is Even")'''


#countdown timer 

'''import time 

my_time = int(input("Enter the time in sec: "))

for i in reversed(range(0,my_time)):
    seconds =  i % 60
    minutes = int(i/60) % 60 
    hours = int(i/3600) %24



    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Happy birthday ")'''

#=================Nested Loop ====================
#A loop within another loop (outer loop and inner loop )

'''for x in range(3):
    for y in range(1,5):
        print(y,end="")'''

'''rows = int(input("Enter the # rows : "))
columns = int(input("Enter the # columns: "))

symbol = "*"

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()'''
row = 4

for i in range(1,row+1):
    for space in range(row-i):
        print(" ", end="")
    for star in range(i):
        print("*",end=" ")
    print()








