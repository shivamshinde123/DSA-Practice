
# sum of first n numbers

N = 10
counter = 1

def firstn_sum(counter, total = 0):

    if counter > 10:
        return total
    
    total += counter 

    return firstn_sum(counter + 1, total)


total = firstn_sum(counter)
print(total)
