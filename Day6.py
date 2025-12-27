#Function = It is a block of reusable code 

'''def happy_birthday(name,age):
    print(f"Happy birthday {name}. Your are {age} years old.")


happy_birthday("Milan",24)'''
#----------------------------------
'''def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due date {due_date}")

display_invoice("Milan",455, "02/12")'''


#Return It is used to end a function and send a result to a caller

'''def add(x,y):
    z = x +y
    return z 

def sub(x,y):
    z = x-y
    return z 

def div(x,y):
    z = x/y
    return z 

print(add(2,3))
print(sub(6,2))
print(div(8,2))'''
#------------------------------
'''def capital(first,last):
    first_name = first.capitalize()
    last_name= last.capitalize()

    return first_name + " " + last_name

print(capital("milan","thapa"))'''


#Default argument = A default value  for certain parameter 

'''def net_price(amount, discount = 0 , tax = 0.05):
    return amount * (1-discount) *(1+tax)

#print(net_price(500))  
print(net_price(500,0.5))'''
#------------------------------------
'''import time
def count(start,end):
    for i in range(start,end):
        print(i)
        time.sleep(1)
    print("Done")

count(0,10)'''

#keyword argument  = an argument preceded  by an identifier

'''def hello (name, lastname, position, title):
    print(f"{name} {lastname} {position}, {title}")

hello("Milan",lastname="Thapa",position="Software engineer", title="awekening")'''

#print("1","2","3","4" ,sep="+")

'''def phone_number(country, area , first , last):
    return(f"+{country} {area} {first}{last}")
phone_num = phone_number(country=971,area=523,first=7573,last=67)

print(phone_num)'''

#====================*args and **kwargs=========================
#args allow you to pass multiple non=key argument
# kwargs allow you to pass multiple keyword argument 

'''def total(*nums):
    total = 0 
    for num in nums:
        total+=num
    return total

print(total(1,2,3,4))'''
#--------------------------------------
'''def display_name(*args):
    for name in args:
        print(name,end=" ")

display_name("Mila","shelby","shankar","meghraj")'''

#====kwargs=====

'''def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

    if "building" in kwargs:
        print(kwargs.get('building'))
    else:
        print(f"{kwargs.get('city')}")

print_address(street="moroccor", city= "dubai", state="UAE", zip="232332",building="i09")'''


#===========================================================================
#Iterable  = An  objects/ collection  that can  return  its elements  one at a time .
#            allowing    it to be. a iterale over a loop 

'''number = [1,2,3,4,5,6]

for num in number:
    print(num,end="-")'''

#----------------------------------
'''names= ("milan","shelby","shankar","megraj")

for name in names:
    print(name,end=" ")'''

#-----------------------------------

whats = {"name":"Milan",
        "age":12,
        "address":"Nepal"}
for key,value in whats.items():
    print(f"{key}:{value}")




