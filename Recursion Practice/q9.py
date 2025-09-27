

# fibonacci number

def f(n):
    i = 0
    j = 1

    print(i, end=" ")
    print(j, end=" ")

    for _ in range(n-2):
        k = i + j
        print(k, end=" ")
        i = j
        j = k

n = 10
f(10)