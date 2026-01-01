#Polymorphisim = Poly -> many 
                 #Morphe -> faces or forms 
# Two ways to acheave  polymorphism
#1.Inhertance = 
#2."Duck typing"= 
from abc import ABC,abstractmethod
class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius
    
    def area(self):
        return 3.14 * (self.radius **2)



class Square(Shape):
    def __init__(self,side):
        self.side= side

    def area(self):
        return self.side **2
        

class Triangle(Shape):
    def __init__(self,base,height):
        self.base= base
        self.height = height    

    def area(self):
        return self.base * self.height * 0.5    


shapes = [Circle(4),Square(2),Triangle(2,2)]

for shape in shapes:
    print(shape.area())
    

#"Duck typing" = Another way to achieve  polymorphism besides Inhertance 
# Object  must have the minimum necessary attribute/methods
# If it looks  like  a duck  and quack  like  a duck , it must  be a duck.

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW") 

class Car(Animal):
    def speak(self):
        print("Honk")
    alive=False
animals = [Dog(),Cat() ,Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

#Static methods =  A method  that belong  to a class  rather than  any objects  from that class (instance)
#Instance method=.best for  operation  on instance  of class objects 
#static methods = Best  for utility  function  that do not access  to class data 

class Employee:
    def __init__(self,name,position,):
        self.name = name 
        self.position = position

    def get_info(self):
        return f"{self.name}|{self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["manager","cashier","cook","janitor"]

        return position in valid_position


emp1 = Employee("Milan","CEO")
emp2 = Employee("Roshan","manager")
emp3 = Employee("Manisha","HR")
print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())
print(Employee.is_valid_position("manager"))



#=====================Class method========================
#Allow operation  related  to the class itself
#Take (cls)  as the first parameter which represent  the class itself

class Student:
    count = 0 
    total_gpa = 0 
    def __init__(self,name,gpa):
        self.name = name 
        self.gpa = gpa
        Student.count +=1
        Student.total_gpa = gpa

    def get_info(self):
        return f"{self.name}|{self.gpa}"
    
    @classmethod

    def get_count(cls):
        return f"Total # of student:{cls.count}"
    
    @classmethod

    def get_average(cls):
        if cls.count ==0:
            return 0 
        else:
            return f"{cls.total_gpa/cls.count}"

std1 = Student("Milan",3.22)
std2 = Student("Roshan",2.22)

print(Student.get_count())
print(Student.get_average())

#=================================================================
#magic methods  = dunder  methods (double underscore) __init__,
#__str__,__eq__
#They are  automatically  called  by many python built-in operration 
#They allow  developer to define  or customizethe behaviour object 

class Student:
    def __init__(self,name,gpa):
        self.name = name 
        self.gpa = gpa 

    def __str__(self):
        return f"name:{self.name} gpa:{self.gpa}"
    
    def __eq__(self,other):
        return self.name == other.name
    
    def __gt__(self,other):
        return self.gpa>other.gpa
    
   
std1 = Student("Milan",3.22)
std2 = Student("Roshan",2.22)

print(std1)
print(std1==std2)
print(std1>std2)


class Book:

    def __init__(self,title,author,num_page):
        self.title = title 
        self.author = author
        self.num_page = num_page

    def __str__(self):
        return f"{self.title} by {self.author} "
    
    def __eq__(self, value):
        return self.title == value.title and self.author == value.author
    
    def __gt__(self,other):
        return self.num_page > other.num_page
    
    def __lt__(self,other):
        return self.num_page < other.num_page
    
    def __add__(self,other):
        return self.num_page + other.num_page
    
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key =="title":
            return  self.title
        
        elif key =="author":
            return self.author
        
        elif key=="num_page":
            return self.num_page

        else:
            return "Invalid Input"    

    

book1 = Book("Into the wild","william",145)
book2 = Book("Good will hunting","hary",145)
book3 = Book("Path Adams","wow",175)

print(book1)
print(book2)
print(book3)

print(book1==book2)
print(book3>book1)
print(book1+book2)
print("william" in book1)


print(book1['title'])
print(book1['author'])
print(book1['num_page'])
print(book1['what'])