def cc11():

    for x in range(1,9,2):
        for z in range(x, 7, 2):
            print(" ", end = " ")
        for z in range(1,x+1): 
            print("*", end = " ")
        print()
        
    for x in range(5,0,-2):
        for z in range(x,7,2):
            print(" ", end = " ")
        for z in range(1,x+1): 
            print("*", end = " ")
        print() 

cc11()