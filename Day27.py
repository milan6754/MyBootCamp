arr = [3, 7, 1, 9, 4]
for i in range(len(arr)):
    print(arr[i])

'''Exercise 2 — Find Sum & Max
Find sum of array
Find maximum element
(Do it manually first, then code)'''
total = 0 
for i in range(len(arr)):
    total+=arr[i]

print(total)

maximum = max(arr)
print(maximum)

matrix = [
    [2, 4, 6],
    [1, 3, 5]
]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end="")
        
    print()

for j in range(cols):
    for i in range(rows):
        print(matrix[i][j],end="")
    print()

row_sum = []
for i in range(rows):
    total = 0 
    for j in range(cols):
        total +=matrix[i][j]
        row_sum.append(total)



print(row_sum)

string = "Milan"

print(string[::-1])


vowel = "aeiouAEIOU"
operation = 0 
for i in range(len(string)):
    if string[i] in vowel:
        operation+=1

print(operation)
length=0
for ch in string:
    if ch in string:
        length+=1

print(length)

def is_paldrome(s):
    left = 0 
    right = len(s)-1

    while left<right:
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True

words = ["madam", "racecar","hello"]

for word in words:
    print(f"{word}:{is_paldrome(word)}")