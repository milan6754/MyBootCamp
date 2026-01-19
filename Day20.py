#Linear_Search 
def linear_search(arr,target):
    found= False
    for num in arr:
        if num == target:
            print("found")
            found = True
            break
        
    if not found:
     print("Not found")

linear_search([10,20,30,40,50],40)
#Binary Search 

def binary_search(arr,target):
   low = 0 
   high = len(arr)
   while low<=high:
      mid = high//2
      if arr[mid]==target:
         return arr[mid]
      elif arr[mid]>target:
         low = mid +1
      else:
         high = mid-1
   return -1
print(binary_search([10,20,30,40,50,60,70,80,90,100],60))
