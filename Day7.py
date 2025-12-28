#Membership operation  = used to test whether a value  or variable
                         #found in a sequence 
# in 
# Not in 

'''words = "apple"
letter = input("Enter the letter to check: ")

if letter in words:
        print(f"The letter is found : {letter}")
else:
        print(f"The letter {letter} is not found")'''
#------------------------------------------------
'''if letter not in words:
    print(f"The letter is not found {letter}")
else:
    print(f"The letter is found: {letter}")'''

#-------------------------------------------------
'''students = {"milan","roshan","mohan","manisha"}

student = input("Enter the student name: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} is not a student")'''

#--------------------------------------------
'''if student not in students:
    print(f"{student} is not a student")
else:
    print(f"{student} is a student")'''

grades = {
    "milan":"D+",
    "roshan":"B+",
    "manisha":"A",
    "barsha":"A+"
}

'''student = input("Enter the student name: ")
if student in grades:
    print(f"{student} grade is {grades[student]}")
else:
    print(f"{student} is not found ")'''

#----------------------------------------------
email = "thapamilankumar211@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invaild email")


#===================List Comprehension======================
#A concise  way to create  lists in python 
# It is easy to  read the traditional loops 


'''double = [x*2 for x in range(1,11)]
print(double)
triple = [x*3 for x in range(1,11)]
print(triple)
square = [x**2 for x in range(1,11)]
print(square)

fruits = [ "apple","orange", "grapes","pineappple"]

fruits = [fruit.upper() for fruit in fruits]

names = [ name.title() for name in ["milan","roshan","manisha"]]
print(fruits)
print(names)

first_char = [fruit[0] for fruit in fruits]
print(first_char)

number = [1,2,3,4,5,6,7,8,9]
even_number = [num for num in number if num%2==0]
print(even_number)

grades = [25,12,56,30,65,39,35,67,99,66]

passed_grade = [grade for grade in grades if grade>=30]
print(passed_grade)'''

#=================Match case statement=======================

def day_of_week(day):
    match day:
        case 1:
            return " Its sunday"
        case 2:
            return "Its monday"
        case 3:
            return "Its tuesday"
        case 4:
            return "Its wednesday"
        case 5:
            return "Its thursday"
        case 6:
            return "Its friday"
        case 7:
            return "Its saturday"
        case _:
            return "Not a valid day "
        
print(day_of_week("pizza"))


#===================Module =============================
# a file containing code  you want to  include  in your program
# use "import "  to include a module (built in  or your own)
#useful  to break up a large program resuable seprate files

#print(help("modules"))
'''import math
import math as m 
from math import e 
pi = 3.14159

def square(x):
    return x**2

def cube(x):
    return x**3

def circumference(radius):
    return 2 * pi * radius 

def area(radius):
    return  pi *  radius **2


#result = Example.pi
result = square(2)
result = area(4)
result = circumference(6)
result = cube(2)
print(result)'''


#=====================Varaible scope==========================
#where  a varaible  is visible  and accessible 
#Scope resoultion (LEGB) Local -> Encolse -> Global -> Built-in
#----Local----
'''def func1():
    a = 1
    print(a)

def func2():
    b=2
    print(b)

func1()
func2()'''
#---Enclose---

'''def func1():
    x = 2
    def func2():
        print(x)
    func2()
func1()'''

#----Global----

'''x = 10 

def func1():
    print(x)

def func2():
    print(x)

func1()
func2()'''

#===================if __name__ == __main__:====================
#This script can be imported  or run standalone 
# Function and class in this module can be reusable 
# without the main block of code executing 

def fav_food(food):
    print(f"Your favorite food is {food}")
def main():
    print("This is script")
    fav_food("pizza")

if __name__ == '__main__':
    main()


