# Bubble Sort function
# unsorted_arr: list to be sorted in place

def bubble_sort(unsorted_arr):
    n = len(unsorted_arr)
    # Outer loop: controls the number of passes
    # After each pass, the largest unsorted element moves to its correct position at the end
    for i in range(n-1, 0, -1):
        array_swapped = False  # Track if any swaps happen in this pass
        # Inner loop: compare adjacent elements up to the i-th index
        for j in range(i):
            # If the current element is greater than the next, swap them
            if unsorted_arr[j] > unsorted_arr[j+1]:
                temp = unsorted_arr[j]
                unsorted_arr[j] = unsorted_arr[j+1]
                unsorted_arr[j+1] = temp
                array_swapped = True  # Mark that a swap occurred
        # If no swaps occurred in this pass, the array is already sorted
        if not array_swapped:
            break
    return unsorted_arr

# Example usage
if __name__ == "__main__":
    arr = [10, 20, 9, 17, 35, 2, 25]
    # arr1 = [1,2,3,4,5]
    print(bubble_sort(arr))
