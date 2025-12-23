#Math Module 
import math 

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b,2))
print(round(c,2))

#if - Do some code only if some condition is true 
#elif - check code in if , if its true execute if not check elif 
#else - Do something 

#checking for eligable or not 
age= int(input("Enter your age: "))
if age>= 18:
    print("You are eligable for Vote")
elif age<0:
    print("you are not born yet ")
elif age>=100:
    print("You are very old")
else:
    print("You are not eligable")

#Asking for coffee===
response = input("Would you like to buy some coffe(Y/N)").lower()

if response =="y":
    print("oh Thank you for the coffee")
elif response =="n":
    print("You are so mean..")

else:
    print("Invalid response")

#Asking for name =================
name = input("Enter your name: ")

if name =="":
    print("you didn't write the name")

else:
    print(f"hello {name}")

    
#is it for sales or not ============
for_sale = True

if for_sale:
    print("this item is for sale ")
else:
    print("This item is not for sale")

#is friend online or not 

is_online = False

if is_online:
    print("He is onine ")
else:
    print("He is offline ")


#Python simple calculator


operator = input("Enter the operator (+,-,*,/)")
num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))

if operator == "+":
    print(num1+num2)
elif operator =="-":
    print(num1-num2)
elif operator =="*":
    print(num1*num2)

elif operator =="/":
    print(num1/num2)

else:
    print("invalid operator...")

#Python weight converter 

weight = float(input("Enter your weight: "))
unit = input("Kilogram or pound (K or L): ").upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs" 
elif unit =="L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"your weigth is: {round(weight,2)} {unit}")
else:
    print(f"{unit} is not valid ")

#Python tempereture 

unit = input("Is this temperature  in Celsius or Fahrenheit(C or F): ").lower()
temp = float(input("Enter the temperature: "))

if unit =="c":
    temp = round((9*temp)/5 +32,1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit =="f":
    temp =round((temp - 32) * 5/9,1)
    print(f"The temperature in Celcius is: {temp}°C")
else:
    print(f"{unit} is invalid ")

#Logical operators = evaluate multiple condition ( Or, And , Not)
# Or = at least one condition must be true
temp = 20 
is_raining = True

if temp > 30 or temp<0 or is_raining:
    print("The outdoor plan is canceled ")
else:
    print("The outdoor events happens in dec 25")

# And = both condition must be True 
temp = 30
is_sunny = True

if temp >=28 and is_sunny:
    print("The weather is lieky to be sunny")
else: 
    print("The weather is might be rainy today")
# Not = invert the condition (not True, not False)
is_sunny = True
if not is_sunny:
    print("Oh , its not sunny ")
else:
    print("Oh its sunny ")

#conditional express = A one line  shortcuts  for  the if- else statement(ternary operator)
num = -1
num2 = 4
age = 19
temp = 20
print("positive" if num>0 else "Negative")

result = "Odd" if num2 %2 ==0 else "Even"
print(result)

status = "adult" if age>=18 else "boy"
weather = "hot " if temp>30 else "cold"
print(weather)

name =  input("Enter your full name: ")
# some build-in function 
# len(name)
result = len(name)
result = name.find(" ")
result = name .rfind("w")
result = name.capitalize()
result = name.upper()
result = name.lower()
result = name.isdigit()
result = name.isalpha()
result = name.count("-")
result = name.replace(" " ,"/")


print(result)


user_name = input("Enter the username: ")

if len(user_name)>12:
    print("Your username is longer than 12 char")

elif  not user_name.find(" ")==-1:
    print("Your username should not include space")

elif not user_name.isdigit():
    print("Your username should not contain number")
else:
    print("Valid username")















