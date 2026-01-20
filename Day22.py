# selection sort
#It is the sorting way by selecting smallest number from unsorted part
#place them at the beginning

#Python code of Selection sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i 

        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j 
        arr[i],arr[min_index]= arr[min_index] ,arr[i]
    return arr

print(selection_sort([2,1,4,7,3]))