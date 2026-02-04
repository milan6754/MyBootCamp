arr = [3, 1, 4, 1, 5, 9]

#print(arr[0])
#print(arr[1])
#print(arr[2])

#for i in range(len(arr),-1,-1):
    #print(arr[i-1])

max = arr[0]
min = arr[0]
for i in range(1,len(arr)):
    if arr[i]>max:
        max = arr[i]
    if arr[i]<min:
        min = arr[i]
print(max)
print(min)

count = 0 

for i in range(len(arr)):
    if arr[i] %2 == 0:
        count+=1

print(count)


def is_paldrome(s):
    l ,r = 0,len(s)
    while l<r:
        if s[l] ==s[l]:
            return True
        l+=1
        r-=1
        return False

print(is_paldrome("racecar"))        

def remove_duplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
            return nums
        
    return i + 1
    
print(remove_duplicates([1,1,2,2,3,3,4,5,5]))

def pair_sum(arr, target):
    l, r = 0, len(arr)-1
    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            return True
        elif s < target:
            l += 1
        else:
            r -= 1
    return False
print(pair_sum([1,2,3,4,5,6,],1))