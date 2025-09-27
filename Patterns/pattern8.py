n = 5
for i in range(n):
    
    for j in range(i):
        print(" ", end="")
    
    for k in range(2*n - 1 - 2*i):
        print("*", end="")
    
    for l in range(i):
        print(" ", end="")
    
    print()