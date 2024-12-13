def act5():
    print("FAHRENHEIT TO CELCIUS CONVERTER PROGRAM")
    print(" ==================================== ")

    fahrenheit = eval(input("Enter a number: "))
    celcius = ((fahrenheit - 32) * 5) / 9
    print(f"{fahrenheit} degree fahrenheit converter to celcius is {celcius} degrees.")

act5()