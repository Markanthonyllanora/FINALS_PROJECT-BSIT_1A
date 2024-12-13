def cc5():
    fahrenheit = eval(input("Enter temperature in fahrenheit: "))
    celcius = ((fahrenheit - 32) * 5) / 9

    print(f"{fahrenheit} degree fahrenheit covert to celcius is {round(celcius ,2)} degree")

cc5()