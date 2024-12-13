def act7():
    gold = 0
    miner = input("Hi, what is your name : " )

    isGold = input(" is the mineral gold? ")

    if isGold == "yes":
        gold += 1
        print(f"Hi, {miner}, your total number of gold is {gold}")

    else:
        print(f"Hi {miner} your total number of gold is {gold}")

act7()