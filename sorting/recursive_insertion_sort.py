# Recursive insertion sort function
# arr: list to be sorted
# current_length: current index to insert into sorted portion
def sort_arr(arr, current_length=1):
    # Base case: if we've reached the end of the array, stop recursion
    if current_length == len(arr):
        return

    # Insert arr[current_length] into the sorted portion arr[0..current_length-1]
    for i in range(current_length, 0, -1):
        # If the current element is less than its left neighbor, swap them
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        else:
            # If not, the element is in the correct position; stop early
            break

    # Recursively sort the next element
    sort_arr(arr, current_length+1)

# Example usage
if __name__ == "__main__":
    arr = [10, 20, 9, 17, 35, 2, 25]
    # Start sorting from index 2 (first two elements are considered sorted)
    sort_arr(arr, current_length=2)
    print(arr)
