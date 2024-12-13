def cc12():

    for x in range(6,0,-1):
        for y in range(1,x+1):
            print(" ", end= "")
        for z in range(5,x,-1):
            print("*", end= "")
        for z in range(5,x,-1):
            print("*", end= "")
        print()
    for x in range(4,0,-1):
        for y in range(1,5-2):
            print(" ",end= " ")
        for z in range(6,x,-5): 
            print("*",end= "")
        for z in range(6,x,-5): 
            print("*",end= "")    
        print()  

cc12()  