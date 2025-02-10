def partition(arr, low, high, pivot): ## Partition function to move the pivot to correct position (sorts the array)
    pivot_index = arr.index(pivot)  # Get the pivot's index
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot to end to start the sorting
    store_index = low

    for i in range(low, high): # sprt through the array
        if arr[i] < pivot:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1

    arr[store_index], arr[high] = arr[high], arr[store_index]  # Place pivot in correct position
    return store_index

def find_median(arr):
    arr.sort()
    return arr[len(arr) // 2]

def select_pivot(arr): # Method to select a pivot using median of medians method
    if len(arr) <= 5:
        return find_median(arr)

    # Divide into groups of 5, find median of each
    medians = [find_median(arr[i:i + 5]) for i in range(0, len(arr), 5)]

    # Find median of medians iteratively
    return find_kth_smallest(medians, len(medians) // 2)

def find_kth_smallest(arr, k): # method to find the kth smallest element in the array
    low, high = 0, len(arr) - 1

    while low <= high:
        pivot = select_pivot(arr[low:high + 1])  # choose pivot
        pivot_index = partition(arr, low, high, pivot)  # partition around pivot

        if k == pivot_index:
            return arr[k]  # Found the kth smallest element
        elif k < pivot_index:
            high = pivot_index - 1  # Move to the left partition
        else:
            low = pivot_index + 1  # Move to the right partition

    return None # If this is reached, then k is greater that the max index, or smaller than 0
