def act8():
    password = input("Enter your password: ")

    if password.lower() == "bsit":
        print("Acces granted")
        print("Enjoy using the system")

    elif password.lower() == "it":
        print("Enjoy using the system")

    else:
        print("Access denied")

act8()