#Time complexity 
'''Time complexity described how the number of operation of algorithm grows
as input size grow
'''

#Big O-notion
'''
Big O notion described  how algorithm running time grow as the input
size grow 

'''

# 3 big core of Big-O notion 

'''
O(1) -constant
e.g arr[3]

O(n)- linear
e.g for i in range(n):
      print(i)

O(n^2) - Quadratic
e.g for i in range(n):
       for j in range(n)
          print(i,j)
'''
# Space complexity 

'''
how much extra memory uses as the input size grow
O(1) - Constant space

Uses a fixed amount of memory.

def sum(a, b):
    return a + b




Linear space

Extra memory grows with input size.

def copy_array(arr):
    new_arr = []
    for x in arr:
        new_arr.append(x)
    return new_arr


O(n²) -Quadratic space

Mostly from 2D arrays / matrices

matrix = [[0]*n for _ in range(n)]

'''

# Recursion 
'''
It is a way of solving small problem by calling function itself
it always need a base case to stop 

e.g

def countdown(n):
    if n == 0:
        print("Go!")
        return
    print(n)
    countdown(n-1)

countdown(3)

'''
