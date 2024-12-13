def act20():
    import os

    isContinue = True
    nt = 0

    while isContinue == True:
        ask = input("Do youu wish to create more triangle? (yes or no) -->")

        if ask.lower() == "no":
            print("Program Terminated")
            break
            isContinue = False

        else:
            nt += 1
            for x in range(1,6):
                for r in range(1,nt+1):
                    for y in range(1,x+1):
                        print("*", end= " ")
                    for z in range(6,x,-1):
                        print(" ", end= " ")
                    
                print()
            continue
act20()
