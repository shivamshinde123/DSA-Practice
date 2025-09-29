
# check if array is sorted in ascending order or not

def sorted_or_not(arr):

    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            pass
        else:
            return False
        
    return True


if __name__ == "__main__":
    arr = [10, 20, 40, 49, 1]
    print(sorted_or_not(arr))