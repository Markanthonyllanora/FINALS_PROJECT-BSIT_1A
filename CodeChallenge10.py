def cc10():

    for x in range(6,0,-1):
        for y in range(1,x+1):
            print(" ", end = "")
        for z in range(6,x,-1):
            print("*", end = "")
        for i in range(6,x,-1):
            print("*", end = "")        
        print() 
        
    for a in range(1,6):
        for b in range(1,a+1):
            print(" ", end = "")
        for c in range(6,a,-1):
            print("*", end= "")
        for d in range(6,a,-1):
            print("*", end= "")
        print()   

cc10()