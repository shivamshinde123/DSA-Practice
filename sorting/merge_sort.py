# Function to merge two sorted subarrays of arr
# arr: the main array
# low: starting index of the first subarray
# mid: ending index of the first subarray
# high: ending index of the second subarray

def merge(arr, low, mid, high):
    temp = list()  # Temporary list to store merged result
    left = low     # Pointer for the left subarray
    right = mid + 1  # Pointer for the right subarray

    # Merge elements from both subarrays in sorted order
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Copy any remaining elements from the left subarray
    while (left <= mid):
        temp.append(arr[left])
        left += 1

    # Copy any remaining elements from the right subarray
    while (right <= high):
        temp.append(arr[right])
        right +=1 

    # Copy the merged elements back into the original array
    for i in range(low, high+1):
        arr[i] = temp[i-low]

# Recursive merge sort function
# arr: the main array
# low: starting index of the subarray to sort
# high: ending index of the subarray to sort

def mergesort(arr, low, high):
    mid = (low + high) // 2  # Find the middle index
    # Base case: if the subarray has one or zero elements, it's already sorted
    if (low >= high):
        return
    # Recursively sort the left half
    mergesort(arr, low, mid)
    # Recursively sort the right half
    mergesort(arr, mid+1, high)
    # Merge the two sorted halves
    merge(arr, low, mid, high)

# Example usage
if __name__ == "__main__":
    arr = [10, 20, 9, 17, 35, 2, 25]
    # arr1 = [1,2,3,4,5]
    mergesort(arr, 0, 6)  # Sort the entire array
    print(arr)
