def cc16():

    balance = 0

    def create_account(name, initial_deposit = 0):
        Account_name = name
        b = 0
        b = initial_deposit
        balance = b
        print(f"\nAccount for {Account_name} with a initial deposit of {balance} has been created.")

    def deposit_amount(amount):
        global balance
        balance += amount
        print(f"\nYou deposited ₱{amount}. New balance is ₱{balance}")

    def check_balance():
        global balance
        print(f"Current balance is {balance}")

    def get_denomination(amount):
        isang_libo = amount // 1000
        libo_sukli = amount % 1000

        limangdaan = libo_sukli // 500
        fiveh_sukli = libo_sukli % 500

        dalwangdaan =  fiveh_sukli // 200
        two_sukli =  fiveh_sukli % 200

        isangdaan = two_sukli // 100
        oneh_sukli = two_sukli % 100

        limampo = oneh_sukli // 50
        fifty_sukli = oneh_sukli % 50

        bente = fifty_sukli // 20
        twenty_sukli = fifty_sukli % 20

        sampo = twenty_sukli // 10
        ten_sukli = twenty_sukli % 10

        lima = ten_sukli // 5
        five_sukli = ten_sukli % 5

        piso = five_sukli // 1
        one_sukli = five_sukli % 1



        print(f"The Breakdown based on the Philippines Denominationn for the amount of {amount}. ")
        print(f"{isang_libo} - 1000")
        print(f"{limangdaan} - 500")
        print(f"{dalwangdaan} - 200")
        print(f"{isangdaan} - 100")
        print(f"{limampo} - 50")
        print(f"{bente} - 20")
        print(f"{sampo} - 10")
        print(f"{lima} -5")
        print(f"{piso} - 1")

    def withdrawmoney(amount):
        global balance
        if amount <= balance:
            balance -= amount
            print(f"Withdrew {amount}. New balance is {balance}")
        else:
            print("Insufficient balance")


    isCont = True
    while isCont == True:
        print("WELCOME TO MY BANK STIMULATION SYSTEM")
        print("================================")
        print("ENTER FROM THE OPTIONS BELOW")
        print("1 --- CREATE ACCOUNT")
        print("2 --- DEPOSIT")
        print("3 --- CHECK BALANCE")
        print("4 --- WITHDRAW")
        print("5 --- EXIT")


        choice = input("Enter your choice here ---> ")

        if choice == "1":
            print("BANK APPLICATION FORM")
            name = input("Enter your full name: ")
            amount = eval(input(f"Enter initial deposit for {name}: "))
            create_account(name, amount)
            continue

        elif choice == "2":
            deposit = eval(input("Enter the amount you want to deposit: "))
            deposit_amount(deposit)
            
            
        
            
        elif choice == "3":
            check_balance()
            get_denomination(balance)
            continue

        elif choice == "4":
            withdraw = eval(input("Enter the amount you want to withdraw: "))
            amount -= withdraw
            withdrawmoney(withdraw)
            continue 

        elif choice == "5":
            print("Program stopped")
            print(f"\nThank you for using our bank!")
            print("Please come again!")
            break

        else:
            print("Invalid pick. Please try again.")
            continue

cc16()