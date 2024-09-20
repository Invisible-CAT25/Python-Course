def showbalance(balance):
    print(f"Your balance is ${balance}")

def deposit():
    amount = int(input("Enter your amount : "))
    if amount <= 0:
        print("Enter a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = int(input("Enter your amount : "))
    if amount > balance:
        print("Insuffcient Funds!!")
        return 0
    else:
        return amount

def main():
    balance = 0
    running = True

    print("---------------------------------")
    print("     Bank Management System")
    print("     Press 1 - To Show Balance")
    print("     Press 2 - To Deposit")
    print("     Press 3 - To Withdraw")
    print("     Press 4 - To Exit")
    print("---------------------------------")
    print()

    while running:
        choice = int(input("Enter your choice : "))

        if choice==1:
            showbalance(balance)
        elif choice==2:
            balance += deposit()
        elif choice==3:
            balance -= withdraw(balance)
        elif choice==4:
            running = False
        else:
            print("Enter a valid choice")

    print("Thank you for using our banking management system!!!")

if __name__ == "__main__":
    main()