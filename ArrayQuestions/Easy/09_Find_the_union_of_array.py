
from collections import OrderedDict
# both array are sorted

def union_of_arrays(arr1, arr2):

    # Approach 1
    # union = OrderedDict()

    # for item in arr1:
    #     if item in union:
    #         union[item] += 1
    #     else:
    #         union[item] = 1

    # for item in arr2:
    #     if item in union:
    #         union[item] += 1
    #     else:
    #         union[item] = 1

    # return list(union.keys())

    # Approach 2
    # s = set()
    # union = []
    
    # for num in arr1:
    #     s.add(num)
    
    # for num in arr2:
    #     s.add(num)
    
    # for num in s:
    #     union.append(num)
    
    # return union.sort()

    # Approach 3
    i, j = 0, 0
    union = list()

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1


        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])

            j += 1

    while i < len(arr1):
        if union[-1] != arr1[i]:
            union.append(arr1[i])

    while j < len(arr2):
        if union[-1] != arr2[j]:
            union.append(arr2[j])

    return union

                        

if __name__ == "__main__":

    arr1 = [1, 2, 3, 4, 5, 10, 11]
    arr2 = [2, 3, 4, 4, 5, 9, 11, 11, 11, 11]
    print(union_of_arrays(arr1, arr2))