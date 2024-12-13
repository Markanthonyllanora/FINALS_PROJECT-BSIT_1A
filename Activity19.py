def act19():
    tuloy = True
    while tuloy == True:
        name = input("Enter your name: ")
        if name.lower() == "stop":
            print("PROGRAM TERMINATED")
            break
            tuloy = False
        else:
            continue
act19()