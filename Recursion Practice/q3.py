
N = 10
counter = 0

def print_up_to_n(counter):

    if counter == N:
        return
    
    print(counter + 1)

    counter += 1

    print_up_to_n(counter)

print_up_to_n(counter)
