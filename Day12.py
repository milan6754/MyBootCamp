#@property 
#Decorator used to define  a method as a property (it can be accessed  like an attribute)
#Benefits - add additional logic when read write or deleted attribute 
#gives you getter setter, delter

class Rectangel:
    def __init__(self,width,height):
        self._width = width 
        self._height = height

    @property
    def height(self):

        return f"{self._height:.2f}CM"
    
    @property
    def width(self):
        return f"{self._width:.2f}CM"
    
    @height.setter
    def height(self,new_height):
        if new_height > 0 :
            self._height = new_height
        else:
            print("height must be great than zero..")

    @width.setter
    def width(self,new_width):
        if new_width > 0 :
            self._width = new_width
        else:
            print("height must be great than zero..")

    @height.deleter
    def height(self):
        del self._height
        print("height is deleted")
    
    @width.deleter
    def width(self):
        del self._width
        print("Width is delted ")

rectangle = Rectangel(1,2)


rectangle.height = 12
rectangle.width = 11

del rectangle.height
del rectangle.width
#print(rectangle.width)
#print(rectangle.height)


#=====================Decorator==============================
#A function that extend the behaviour of another function 
#pass the base function  as an argument. to the decorator

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("You add sprinkles")
        func(*args,**kwargs)
        

    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        
        print("You add fudge")
        func(*args, **kwargs)
        
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice-cream")

get_ice_cream("chocolate")



def starting(func):
    def wrapper():
        print("Function Starting...")
        func()
        print("Function Ending...")
    return wrapper
        
@starting
def task():
    print("Doing task")

task()


def loud(func):
    def wrapper():
        print("LOUD MODE ON.")
        print("LOUD MODE OFF")
        func()
    return wrapper

@loud
def dancing():
    print("he is dancing")

dancing()


def add_sauce(func):
    def wrapper():
        print("adding sauce...")
        func()
    return wrapper

def add_cheese(func):
    def wrapper():
        print("Adding cheese..")
        
    return wrapper

@add_sauce
@add_cheese

def make_pizza():
    print("Pizza is ready")

make_pizza()


def double_result(func):
    def wrapper(*args,**kwargs):
        print("The double result")
        result = func(*args,**kwargs)
        return result * 2

    return wrapper

@double_result
def add(a,b):
    return a+b

print(add(1,2))



#========================Error ~handling========================
# an event that interrupt the flow of a program 
#(zeroDivisionError,TypeError,valueError)
#try,except,finally

'''try:
    num = int(input("Enter the number: "))
    print(1/num)
except ZeroDivisionError:
    print("Num cannt be divisable by 0.")

except ValueError:
    print("Enter only number please")

finally:
    print("Done........")'''


#===============Python file detection=================

import os 

file_path = "/Users/milankumarthapa/Desktop/Book"

if os.path.exists(file_path):
    print(f"The location {file_path} exist")

    if os.path.isfile(file_path):
        print("That is file")
    elif os.path.isdir(file_path):
        print("That is directory")
else:
    print("It doesnt exist")


#=============Python writing files(.txt,.json,.csv)===============
'''import json 
import csv
employees = [
    ["Name", "Age", "Job"],
    ["Mian",24,"CEO"],
    ["Roshan",23,"Manager"],
    ["Manisha",23,"HR"]



]

file_path = "output.csv"


try:
    with open(file_path,"w" ,newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"json file  '{file_path} was created...")
except FileExistsError:
    print("That file already exist")



students = {
    "name":"Milan",
    "age":24,
    "level":"Elite"
}
file_path = "output.json"

try:
    with open(file_path,"w") as file:
        json.dump(students,file,indent=4)
        print(f"json file  '{file_path} was created...")
except FileExistsError:
    print("That file already exist")

employee =  ["Milan","Roshan","Dikshika","Barsha","Manisha"]
file_path = "output.txt"

try:
    with open(file_path,"w") as file:
        for employe in employee:
            file.write(("\n" + employe))
        print(f"txt file  '{file_path} is created...")
except FileExistsError:
    print("That file already exist")'''


#====================For reading file ===============================
import json
import csv
try:
    file_path="output.csv" #Change file here with exact path
    with open(file_path,"r") as file:
        #content = file.read()
        #content = json.load(file)
        content = csv.reader(file)
        for line in content:
            print(line[2])
        #print(content['name'])
        #print(content)

except FileNotFoundError:
    print("File is not found")
except PermissionError:
    print("You dont have permission to read a file")