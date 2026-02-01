#recursive 
def func(n):
    if n == 1:
        return 1
    return n * func(n-1)

print(func(4))

"""
4 * fun(4-1)
4 * 3 * fun(3-1)
4 * 3 * 2 * fun(2-1)
4 * 3 * 2 * 1
24

"""
#Print numbers from N to 1 using recursion
def less(n):
    if n == 0:
        return 1
    print(n)
    less(n-1)
    

less(4)
    

#Find power(x, n) using recursion

def pow(x,n):
    if n ==0:
        return 1
    return  x * pow(x,n-1)
print(pow(2,5))