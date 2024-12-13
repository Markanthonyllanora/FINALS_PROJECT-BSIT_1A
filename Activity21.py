def act21():
    tuloy = True
    count = 0
    while tuloy == True:
        name =input("Please enter a name -->")

        if name.lower() == "stop":
            print("LOOP HAS NOW STOP")
            print(f"You have entered {count} number of names")
            break
            tuloy = False
        
        else:
            count += 1
            continue
act21()

