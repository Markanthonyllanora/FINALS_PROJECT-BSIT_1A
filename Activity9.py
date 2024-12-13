def act9():
    age = eval(input("Please type your age: "))

    if age >= 1 and age<= 7:
        print("toddler")
    elif age >=8 and age<= 13:
        print("your age is cconsidered as pre teen")
    elif age >= 14 and age <= 18:
        print("your age is considered as a teenager")
    elif age  >= 19 and age <= 31:
        print("your age is considered as early adulthood")
    elif age >= 32 and age <= 45:
        print("your age is considered as a mid adulthood")
    elif age >= 46 and age <= 59:
        print("your age is considered as a post adulthood")
    elif age >= 60:
        print(" your agee is considered as a senior")

act9()