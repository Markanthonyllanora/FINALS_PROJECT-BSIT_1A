def cc16():
    class Account:
        def __init__(self, name, initial_deposit=0):
            self.name = name
            self.balance = initial_deposit
            print(f"\nAccount for {self.name} with an initial deposit of ₱{self.balance} has been created.")

        def deposit(self, amount):
            self.balance += amount
            print(f"\nYou deposited ₱{amount}. New balance is ₱{self.balance}.")

        def check_balance(self):
            print(f"Current balance for {self.name} is ₱{self.balance}.")

        def get_denomination(self):
            amount = self.balance
            denominations = {
                1000: "₱1000",
                500: "₱500",
                200: "₱200",
                100: "₱100",
                50: "₱50",
                20: "₱20",
                10: "₱10",
                5: "₱5",
                1: "₱1"
            }
            print(f"The breakdown for ₱{amount} is:")
            for denom, label in denominations.items():
                count = amount // denom
                amount %= denom
                print(f"{count} - {label}")

        def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
                print(f"\nWithdrew ₱{amount}. New balance is ₱{self.balance}.")
            else:
                print("Insufficient balance.")

    account = None
    while True:
        print("\nWELCOME TO MY BANK SIMULATION SYSTEM")
        print("====================================")
        print("1 --- CREATE ACCOUNT")
        print("2 --- DEPOSIT")
        print("3 --- CHECK BALANCE")
        print("4 --- WITHDRAW")
        print("5 --- EXIT")

        choice = input("Enter your choice here ---> ")

        if choice == "1":
            print("\nBANK APPLICATION FORM")
            name = input("Enter your full name: ")
            try:
                initial_deposit = float(input(f"Enter initial deposit for {name}: "))
                account = Account(name, initial_deposit)
            except ValueError:
                print("Invalid deposit amount. Please try again.")

        elif choice == "2":
            if account:
                try:
                    deposit = float(input("Enter the amount you want to deposit: "))
                    account.deposit(deposit)
                except ValueError:
                    print("Invalid deposit amount. Please try again.")
            else:
                print("No account found. Please create an account first.")

        elif choice == "3":
            if account:
                account.check_balance()
                account.get_denomination()
            else:
                print("No account found. Please create an account first.")

        elif choice == "4":
            if account:
                try:
                    withdraw = float(input("Enter the amount you want to withdraw: "))
                    account.withdraw(withdraw)
                except ValueError:
                    print("Invalid withdrawal amount. Please try again.")
            else:
                print("No account found. Please create an account first.")

        elif choice == "5":
            print("\nThank you for using our bank!")
            print("Please come again!")
            break

        else:
            print("Invalid choice. Please try again.")

        else:
            print("Invalid pick. Please try again.")
            continue

cc16()
