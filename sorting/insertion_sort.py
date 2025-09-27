# Insertion Sort function
# unsorted_arr: list to be sorted in place

def insertion_sort(unsorted_arr):
    n = len(unsorted_arr)
    # Start from the second element (index 1), as the first element is considered sorted
    for i in range(1, n):
        # Move the current element leftward into its correct position in the sorted portion
        for j in range(i, 0, -1):
            # If the current element is less than its left neighbor, swap them
            if unsorted_arr[j] < unsorted_arr[j-1]:
                temp = unsorted_arr[j-1]
                unsorted_arr[j-1] = unsorted_arr[j]
                unsorted_arr[j] = temp
            else:
                # If not, the element is in the correct position; stop early
                break
    return unsorted_arr

# Example usage
if __name__ == "__main__":
    arr = [10, 20, 9, 17, 35, 2, 25]
    # arr1 = [1,2,3,4,5]
    print(insertion_sort(arr))
