# Recursive Bubble Sort function
# arr: list to be sorted
# current_length: number of elements to consider in this pass

def find_max(arr, current_length):
    # Base case: if only one element left, array is sorted
    if current_length == 1:
        return 

    # Perform one pass of bubble sort: move the largest element to the end
    for i in range(current_length-1):
        # If current element is greater than the next, swap them
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    # Recursively sort the first (current_length-1) elements
    find_max(arr, current_length-1)

# Example usage
if __name__ == "__main__":
    arr = [10, 20, 9, 17, 35, 2, 25]
    # Start with the full length of the array
    find_max(arr, len(arr))
    print(arr)
