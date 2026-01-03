#====================Date-Time import==========================

'''import datetime

date = datetime.date(2026,1,3)
today = datetime.date.today()
print(date)
print(today)

time = datetime.time(12,30,0)
print(time)

now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m-%d-%y")
print(now)

targe_datetime = datetime.datetime(2020,1,2 ,12,30,1)
current_datetime = datetime.datetime.now()

if targe_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Targe date time hasnot passed")'''


#=======================Python alaram clock================================
'''import time
import datetime

def set_alarm(alarm_time):
    print(f"alarm set for {alarm_time}")
    is_running=True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time==alarm_time:
            print("Wake Up....!")
            is_running=False
        time.sleep(1)


if __name__ =="__main__":
    alarm_time=input("Enter the time(HH:MM:SS)")
    set_alarm(alarm_time)'''



#=================Multi Threading====================
#Multi-Threading is running multiple-task at the same time
#Good for I/O bound task like reading file while   fetching api in the background
#Threading.thread(target=my_function)

'''import threading
import time

def walk_dog(name,last):
    time.sleep(8)
    print(f"You are walking {name}{last}")

def take_out_trash():
    time.sleep(4)
    print("You take the trash to throw in bin ")

def get_mail():
    time.sleep(2)
    print("Your get the mail")


task1 = threading.Thread(target=walk_dog,args=("Tommy","shel"))
task1.start()

task2 = threading.Thread(target=take_out_trash)
task2.start()

task3 = threading.Thread(target=get_mail)
task3.start()

task1.join()
task2.join()
task3.join()
print("You complete all tasks")'''

#================how to connect to api=====================
import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    response= requests.get(url)
    
    if response.status_code==200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrive data {response.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name:{pokemon_info["name"].upper()}")
    print(f"Id:{pokemon_info["id"]}")
    print(f"Height:{pokemon_info["height"]}")
    print(f"Weight:{pokemon_info["weight"]}")



#==================Threading and API connect============
import threading
import requests
 
base_url = "https://jsonplaceholder.typicode.com"

def fetch_post():
    response = requests.get(f"{base_url}/posts")
    post = response.json()
    print(f"Posts:{len(post)}")

def fetch_user():
    response = requests.get(f"{base_url}/users")
    user = response.json()
    print(f"User:{len(user)}")

t1 = threading.Thread(target=fetch_post)
t2 = threading.Thread(target=fetch_user)
t1.start()
t2.start()

t1.join()
t2.join()

print("All finished")
