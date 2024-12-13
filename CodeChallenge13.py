def cc13():

    for x in range(1,6):
        for y in range(6,x,-1):
            print(" ", end= " ")
        for z in range(x,1,-1): 
            print(z, end = " ")
        for a in range(1,x+1):
            print(a, end= " ")
        print()  
    for a in range(4,0,-1):
        for b in range(6,a,-1):
            print(" ", end= " ") 
        for c in range(a,1,-1):
            print(c, end= " ")  
        for d in range(1,a+1):
            print(d, end= " ")
        print()    

cc13() 