#Doc string====
'''def add(a,b):
    This is a additional between two number
    return a+b

print(add(2,3))
print(add.__doc__)'''


#==============Recursion==============

'''def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(4))

def fabonacci(n):
    if n==0 or n==1:
        return n 
    else:
        return fabonacci(n-1) + fabonacci(n-2)'''

#for i in range(10):
    #print(fabonacci(i))


#import os

#if not os.path.exists("data"):
   # os.mkdir("data")

#for i in range(10):
    #os.mkdir(f"data/day{i+1}")
    #os.rename(f"data/day{i+1}",f"data/tutorial{i+1}")

#folders = os.listdir("data")
#print(folders)

#for folder in folders:
    #print(os.listdir(f"data/{folder}"))
import json
file_name = "output.json"

def read_task():
    with open(file_name,"r") as file:
        return json.load(file)
    

def save_task(tasks):
    with open(file_name,"w") as file:
        json.dump(tasks,file,indent=4)


def add_task(task_name):
    tasks = read_task()
    tasks.append({"task":task_name,"done":False})
    save_task(tasks)
    print("Task Added")

def show_task():
    tasks = read_task()
    for i , task in enumerate(tasks,1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} {status}")
       

def mark_done(index):
    tasks = read_task()
    tasks[index-1]["done"] = True
    save_task(tasks)
    print("Task marked as done.")

        



while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Mark task as done")
    print("4. Exit")

    choice = input("Choose: ")

    if choice =="1":
        task = input("Enter the task: ")
        add_task(task)
    
    elif choice =="2":
        show_task()
    
    elif choice =="3":
        show_task()
        num = int(input("Enter task number: "))
        mark_done(num)
    elif choice=="4":
        break
    else:
        print("Invalid choice ")
