accounts = {}

def register():
    user = input("Type in a username: ")
    pin = int(input("Type in a pin: "))

    if user in accounts or len(str(pin)) != 4:
        print("Username is taken and/or PIN isn't the right length")
    else:
        accounts[user] = {"Balance": 0, "Pin": pin}
        print("Account registered")

def login():
    global logged
    user = input("Type in your username: ")
    pin = int(input("Type in your PIN: "))
    
    if user in accounts and accounts[user]["Pin"] == pin:
        print("Welcome",user)
        logged = user
        print(logged)
    else:
        print("Username or PIN was wrong")

def deposit():
    global logged
    if logged == "":
        print("Please login")
        return
    
    amount = int(input("Enter the amount you'd like to deposit: "))
    if amount <= 0:
        print("Invalid amount")
    else:
        accounts[logged]["Balance"] += amount
        print(amount,"dollars has been deposited")

def withdraw():
    global logged
    if logged == "":
        print("Please login")
        return
    
    amount = int(input("Enter the amount you'd like to withdraw: "))
    if amount <= 0 or accounts[logged]["Balance"] < amount:
        print("Invalid amount")
    else:
        accounts[logged]["Balance"] -= amount
        print(amount,"dollars has been withdrawn")

def check_balance():
    global logged
    if logged == "":
        print("Please login")
        return
    
    print("You have",accounts[logged]["Balance"],"dollars")
    
def change_pin():
    global logged
    if logged == "":
        print("Please login")
        return
    
    old = int(input("Type in your old pin"))
    new = int(input("Type in your new pin"))
    if old != accounts[logged]["Pin"] or len(str(new)) != 4:
        print("Either your password don't match or your new password isn't the right length")
    else:
        accounts[logged]["Pin"] = new
        print("Pin has been changed")
    
def delete_account():
    global logged
    user = input("Type in user: ")
    pin = int(input("Type in PIN: "))
    
    if user in accounts and accounts[user]["Pin"] == pin:
        del accounts[user]
        print("Account deleted")
    else:
        print("User doesn't exist and/or user's pin is wrong")
    
def logout():
    global logged
    if logged == "":
        print("You aren't logged in")
    else:
        logged = ""
    
def transfer():
    if logged == "":
        print("Please login")
        return

    user = input("Type the user you would like to transfer money to: ")
    amount = int(input("Type the amount you would like to transfer: "))
    if user in accounts and accounts[logged]["Balance"] >= amount:
        accounts[user]["Balance"] += amount
        accounts[logged]["Balance"] -= amount
        print("Money has been transferred")
    else:
        print("User doesn't exist and/or you don't have enough balance")

def menu():
    print("Welcome to this bank")
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Change PIN")
        print("7. Delete Account")
        print("8. Logout")
        print("9. Transfer")
        print("10. Exit")
        
        choice = input("Enter choice: ")
        
        if choice=="1":
            register()
        elif choice=="2":
            login()
        elif choice=="3":
            deposit()
        elif choice=="4":
            withdraw()
        elif choice=="5":
            check_balance()
        elif choice=="6":
            change_pin()
        elif choice=="7":
            delete_account()
        elif choice=="8":
            logout()
        elif choice=="9":
            transfer()
        elif choice=="10":
            print("Closing bank system")
            break
        else:
            print("Invalid option, possible options are 1-10")
menu()