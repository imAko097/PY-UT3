from hucha import Hucha

def main():
    my_piggy_bank = Hucha()
    print("Money in the piggy bank: ", my_piggy_bank.getMoney(), " euros")

    print("------------------------------------")

    # Put money
    print("Put 150 euros in the piggy bank")
    my_piggy_bank.putMoney(150)
    print("Money in the piggy bank: ", my_piggy_bank.getMoney(), " euros")

    print("------------------------------------")

    # Take money
    print("Take 35 euros from the piggy bank")
    my_piggy_bank.takeMoney(35)
    print("Money in the piggy bank: ", my_piggy_bank.getMoney(), " euros")

    print("------------------------------------")

    # Print how much money is in the piggy bank
    my_piggy_bank.takeMoney(15)
    my_piggy_bank.putMoney(20)
    my_piggy_bank.putMoney(50)
    my_piggy_bank.printMoney() # print

main()