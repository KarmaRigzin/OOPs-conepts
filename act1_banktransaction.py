#Write a python program to simulate bank transactions for two clients in procedural programming.

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if balance >= amount:
        return balance - amount
    else:
        return "Insufficient balance"

def check_balance(balance):
    return balance

def transaction(balance, client_name):
    print("Welcome to Bank of Bhutan\n" + client_name)
    print("Current balance: Nu." + str(balance))
    print("What would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = float(input("Enter amount to be deposited: "))
        balance = deposit(balance, amount)
        print("Your updated balance is: Nu." + str(balance))
    elif choice == 2:
        amount = float(input("Enter amount to be withdrawn: "))
        balance = withdraw(balance, amount)
        if type(balance) == str:
            print(balance)
        else:
            print("Your updated balance is: Nu." + str(balance))
    elif choice == 3:
        balance = check_balance(balance)
        print("Your current balance is: Nu." + str(balance))
    elif choice == 4:
        print("Thank you for using BoB. Have a nice day!")
    else:
        print("Invalid choice. Please try again.")
    return balance
    
# initial balances for two clients
balance1 = 1000
balance2 = 2000

# transactions for client 1
balance1 = transaction(balance1,"Dorji")

# transactions for client 2
balance2 = transaction(balance2, "Dechen")
