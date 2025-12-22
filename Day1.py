'''#This is my first programming 
print("Hi, This is my first code,")
print("Today is day 1 of learning of python")

#Variable = It is a container that store value like(integer, float, string, boolean)
#String 
first_name = "Milan"
programming ="Python"
goal = "coder"

#Integer
age= 24
quantiy = 33
num_of_student = 21

#Float
price = 22.1
distance = 33.2
percentage = 25.6

#Boolean 

is_student = True 
is_present = False 

#TypeCasting = The process of converting the variable from one data type to another 
# str() , int(), float(), bool()
name = "Milan"
age = 24
cgpa = 2.7
is_student = True

age = str(age) # changing int into str 
name = bool(name) # change str into bool 


# input  = It is a built-in function which lets the user  t0 enter the data 
# It return the entered data into string 

name = input("Enter the your name: ")
age = int(input("Enter the age: "))
print(f"Hello how are yout {name}")
print("Happy birthday.....")
print("You are {age} years old")


#Exercise 1  Rectangle  Area  Cal

length = int(input("Enter the length of rec: "))
width = int(input("Enter the width of rec: "))

area = length * width
print(f"The area of rec is {area}")

#Exercise 2 Shopping cart...

product = input("Which product would you like to but...?")
quantity = int(input("Enter the quantity: "))
price  = float(input("Enter the price: "))

Total =  price *  quantity

print(f" your total price for {product} is {Total}")


#Arithmetic and Math 

friends = 10 

friends = friends + 1 
friends += 1

friends = friends - 1 
friends -= 1

friends = friends * 1 
friends *= 1

friends = friends /1 
friends /= 1

friends = friends //1 
friends //= 1

friends = friends ** 1 
friends **= 1

x = 3.14
y = -2
z =4

result = round(x)
result = abs(y)
result = pow(2,2)
result = max(x,y,z)
result = min(x,y,z)
print(result)

 # Module Math
import math 

print(math.pi)
print(math.e)
x = 9.2

result = math.sqrt(x)
result1 = math.ceil(x)
result2= math.floor(x)

print(result2)'''

import math 

r = float(input("Enter the value of radius: "))

cir = 2 * math.pi * math.pow(r,2)
print(f"The cirumference of a circle is {round(cir,2)}Cm")







