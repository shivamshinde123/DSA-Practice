
# print something N times

counter = 0

def main(counter):

    if counter == 10:
        return
    
    print("Hey there!")

    main(counter + 1)

main(counter)

