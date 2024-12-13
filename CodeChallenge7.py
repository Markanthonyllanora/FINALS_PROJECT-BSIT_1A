def cc7():

    grocery = input("Did you buy a grocery? (Yes/No):")

    if grocery.lower() == "yes":
            itemname = input("Name of the Item: ")
            price = float(input("What's the price of the item: "))
            age = int(input("Age: "))
            amountgiven = float(input("Amount given: "))
            
            taxrate = .123
            senior_discount = .052
            
            
            if age >= 60:
                discount = price * senior_discount
                totalamountwithtax = price + discount
                print(f"With senior discount {totalamountwithtax:.2f} in php")
                print(f"Hi customers you purchase a {itemname} with the price of {price} plus (5.2%) tax of {discount:.2f}")
                print(f"total price with tax is {totalamountwithtax:.2f}")
                
            elif age <= 59:
                taxamount = price * taxrate
                totalamountwithtax = price + taxamount
                print("NO senior discount")    
                print(f"Hi customers you purchase a {itemname} with the price of {price} plus (12.3%) tax of {taxamount}")
                print(f"total price with tax is {totalamountwithtax:.2f}")
            
                
                    
            
            change = amountgiven - totalamountwithtax
            
            if change >= 0:
                print(f"your change is {change:.2f}")  
            else:
                print("insufficient funds")    
    else:
        print("No purchase made") 

cc7()       