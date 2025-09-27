# Partition function for quicksort
# arr: the array to partition
# low: starting index of the subarray
# high: ending index of the subarray
def partition(arr, low, high):
    # Choose the first element as the pivot
    pivot = arr[low]
    i = low
    j = high

    # Rearrange elements so that those less than pivot are left, greater are right
    while (i < j):
        # Move i right until an element greater than pivot is found or end is reached
        # i should not go out of bounds (i <= high - 1)
        while (arr[i] <= pivot and i <= high - 1):
            i += 1
        # Move j left until an element less than or equal to pivot is found
        # j should not go out of bounds (j >= low)
        while (arr[j] > pivot and j >= low):
            j -= 1
        # Swap arr[i] and arr[j] if i < j
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
    # Place the pivot in its correct position
    arr[low], arr[j] = arr[j], arr[low]
    return j

# Recursive quicksort function
# arr: the array to sort
# low: starting index of the subarray
# high: ending index of the subarray
def quicksort(arr, low, high):
    # Only sort if the subarray has more than one element
    if (low < high):
        # Partition the array and get the pivot index
        pIndex = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quicksort(arr, low, pIndex-1)
        quicksort(arr, pIndex+1, high)

# Example usage
if __name__ == "__main__":
    arr = [10, 20, 9, 17, 35, 2, 25]
    # arr1 = [1,2,3,4,5]
    quicksort(arr, 0, len(arr)-1)
    print(arr)
