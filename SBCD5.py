l1 = [int(input("Enter a number: ")) for _ in range(5)]
while True:
    choice = input("2 - for add, 1 - for Naa, 0 - for Wala. Select number: ")
    
    if choice == "2":
        num = int(input("Enter a number to add: "))
        l1.append(num)
    elif choice == "1": #queue implementation
        if l1:
            l1.pop(0)
        else:
            print("")
    elif choice == "0": #stack implementation
        if l1:
            l1.pop()
        else:
            print("")
    else:
        print("Invalid, try again.")
    
    print(l1)
