# Selection Sort function
# unsorted_arr: list to be sorted in place

def selection_sort(unsorted_arr):
    n = len(unsorted_arr)
    # Traverse through all array elements
    for i in range(n):
        # Assume the current position holds the minimum element
        min_index = i
        # Find the index of the minimum element in the unsorted portion
        for j in range(i, n):
            if unsorted_arr[j] < unsorted_arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted portion
        temp = unsorted_arr[min_index]
        unsorted_arr[min_index] = unsorted_arr[i]
        unsorted_arr[i] = temp
    return unsorted_arr

# Example usage
if __name__ == "__main__":
    arr = [2, 2, 1, 523, 23, 63]
    print(selection_sort(arr))
