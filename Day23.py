#Insertion array takes one element at a time and place them in a sorted part
#[2,1,4,6,5]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

    return arr
print(insertion_sort([5,2,1,7,9,3]))