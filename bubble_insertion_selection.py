import time
import random
def bubblesort(arr):
    start = time.time()
    n = len(arr)

    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    end = time.time()

    return (end-start)* 10**3

def selectionsort(arr):
    start = time.time()

    for i in range(len(arr)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                
        # Swap the found minimum element with  
        # the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    end = time.time()
    return (end-start)* 10**3

def Insertionsort(arr):
    start = time.time()

    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

    end = time.time()

    return (end-start)* 10**3




Array = [random.randint(1, 100) for _ in range(100000)]
print(f"\n The time taken for bubble sort is {bubblesort(Array)} ms")
print(f"\n The time taken for Selection sort is {selectionsort(Array)} ms")
print(f"\n The time taken for Insertion sort is {Insertionsort(Array)} ms")


