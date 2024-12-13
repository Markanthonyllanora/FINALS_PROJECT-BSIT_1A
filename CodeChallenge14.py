def cc14():

    A = True
    number = 0

    while A == True:
        num = eval(input("Please Enter a number --> "))
        number += num
        if num == 0:
            print("Loop has terminated")
            print(f"The sum of all number you entered is {number}. ")
            break
        else:
            number += 0
            continue    

cc14()  