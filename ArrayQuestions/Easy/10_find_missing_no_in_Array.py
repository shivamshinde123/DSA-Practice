

def find_missing_no_in_array(N, arr):

    for i in range(N):
        if (i + 1) not in arr:
            return i + 1
        

if __name__ == "__main__":

    N = 5
    arr = [1, 2, 4, 5]

    print(find_missing_no_in_array(N, arr))

