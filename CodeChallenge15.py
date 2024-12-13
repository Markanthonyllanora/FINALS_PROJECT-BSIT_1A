def cc15():


    import os

    tuloy = True
    num = 0
    while tuloy:
        ask =input("Do you want to create new triangle (yes or no) --> ")
        
        if ask.lower() == "no":
            print("loop terminated")
            break
        elif ask.lower() == "yes":
            num += 1
            for x in range(1,6):
                for y in range(1, num+1): 
                    for z in range(1,x+1):
                        print("*", end = " ")                    
                    for a in range(6,x,-1):
                        print(" ", end= " ")
                print() 
                continue
        else:
            os.system("cls")
            print("invalid answer, please only answer 'yes' or 'no'")
            continue

cc15()