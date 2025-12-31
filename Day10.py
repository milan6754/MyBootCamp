#==============Python Object oriented program ==================
# Class= It is a blueprint used to design  the structure 
# and and layout of an object 
# object= It is the collection of related attributes  and methods 
'''

class Car:
    def __init__(self,model,color,year,is_for_sale):
        self.model = model 
        self.color = color
        self.year = year 
        self.is_for_sale = is_for_sale
    
    def drive(self):
        print(f"You drive the {self.color} {self.model}")
    
    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car1 = Car("Porsche", "black",2021,False)
car2 = Car("BMW","purple",1998,True)

print(car1.model)
print(car1.color)
print(car1.year)
print(car1.is_for_sale)

car1.drive()
car1.stop()
car1.describe()
print("========================")
car2.drive()
car2.stop()
car2.describe()'''

#==========class Variable ====================
#share among all instance of classs
#Defined outside the constructor
#Allow  you to share data among all object  created from that class

'''
class Student:
    class_year = 2021
    student_no= 0 
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        Student.student_no +=1
        
    

std1 = Student("mialn",24)
std2 = Student("roshan",25)
std3 = Student("Barsha",21)

print(std1.name)
print(std1.age)
print(std1.class_year)

print(std2.name)
print(std2.age)
print(std2.class_year)


print(Student.student_no)

print(f"The badge No.{Student.class_year} has {Student.student_no} Student: ")
print(std1.name)
print(std2.name)
print(std3.name)'''


#===================Inheritance======================
#All class to inherit methods and attributes  from another class
#Helps with code reusability and extensibility 
#child class parent 

'''class Animal:
    def __init__(self,name):
        self.name = name 
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")
class Tiger(Animal):
    def speak(self):
        print("Ghowrrrrr")


dog = Dog("tommy")
cat = Cat("dummy")
tiger = Tiger("commy")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()
print("------------------")
print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()
print("------------------")
print(tiger.name)
print(tiger.is_alive)
tiger.eat()
tiger.sleep()
tiger.speak()'''

#===============Multiple Inheritance====================
#C(A,B)
# Inherit from more than one parent class


#==============Multilevel inheritance====================
#Inherit from parent which inherit from another parent 
#C(B)<-B(A)<-A

class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"This {self.name} is eating")
    def sleep(self):
        print(f"This {self.name} is sleeping")
class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")

class Rabit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass


rabit = Rabit("Buggy")
hwak = Hawk("Luffy")
fish = Fish("zoro")

rabit.flee()
hwak.hunt()
fish.flee()
fish.hunt()

rabit.eat()
rabit.sleep()

#================Super()========================
#Functions  used  in a child  class  to call  methods  from  a parent class
#Allows  you to extend  the functionality  of the  inherited  methods
class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is  {self.color} and {'filled' if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
       super().__init__(color,is_filled)
       self.radius = radius
    
    def describe(self):
        print(f"Is is a cicle with the area of {3.14* self.radius * self.radius}cm")
        super().describe()

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width
    
    def describe(self):
        print(f"It is a square with the area of {self.width * self.width}Cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self,color,is_filled,width, height):
       super().__init__(color,is_filled)
       self.width =width
       self.height = height

    def describe(self):
        print(f"It is the  triangle with the area of {self.width * self.height/2}CM^2")
        return super().describe()


circle = Circle(color="red",is_filled=True,radius=5)
print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")
circle.describe()
print("***********************************")
square = Square(color="black",is_filled=True,width=25)
print(square.color)
print(square.is_filled)
print(f"{square.width}cm")
square.describe()
print("************************************")
triangle = Triangle("purple",is_filled=False,height=12,width=32)
print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")
triangle.describe()