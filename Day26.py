#Quick_Sort 
# It is a sorting algorithms which rearrange the element around the 
# pivot element ,swap the lesser than pivot in left side and swap the greater than pivot 
# in right side. 


def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    left = []
    right = []

    for i in range(1,len(arr)):
        if arr[i]<pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [3,5,2,9,1,4]
quick = quick_sort(arr)
print(quick)