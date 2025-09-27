

# reverse an array
arr = [1, 2, 3, 4, 5]
b = list()
i = len(arr) - 1

def reverse_arr(i):

    if i < 0:
        return b
    
    b.append(arr[i])

    return reverse_arr(i-1)

print(reverse_arr(i))
