import random

def partition(arr, low, high): # partition function to place the pivot in correct position and sort the array
    pivot_index = random.randint(low, high)  # get a random pivot index
    pivot = arr[pivot_index] # get the pivot value
    
    # Move pivot to the end as part of quicksort step
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    store_index = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1

    # Move pivot to its correct position
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def find_kth_smallest(arr, k): # find the kth smallest element in the array
    low, high = 0, len(arr) - 1

    while low <= high:
        pivot_index = partition(arr, low, high)  # sort array and get the pivot index

        if pivot_index == k: # if pivot is in kth position, return the value
            return arr[pivot_index]  
        elif pivot_index > k: # pivot is greater than k, search the left sub-array
            high = pivot_index - 1 
        else: # pivot is smaller, search right sub-array
            low = pivot_index + 1 

    return None # If this is reached, then k is greater that the max index, or smaller than 0
