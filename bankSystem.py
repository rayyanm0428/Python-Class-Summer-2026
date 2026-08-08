users = []
current = []
transactions = []

def register():
    user = str(input("Enter a username: "))
    password = str(input("Enter a password: "))
    users.append([user,password,0])
    
    for user in users:
        if user == users:
            print("Username is already taken")
            users.remove([user,password,0])
            return
        else:
            print("***************************")
            print("User has been added")
            print("***************************")
            return
    
def login():
    global current
    global users
    user = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    
    if current != []:
            for j in users:
                if current[0] == j[0]:
                    j = current
    
    for i in users:
        if i[0]==user and i[1]==password:
            current=i
            print("***************************")
            print("Welcome",user,"to my bank!")
            print("***************************")
            return
    print("***************************")
    print("Username or password is wrong")
    print("***************************")
    
def deposit():
    global current
    global transactions
    if current == []:
        print("Please login")
        return
    add = int(input("Enter the amount you would like to deposit: "))
    current[2] += add
    print("$",add,"has been deposited")
    transactions.append([current[0],"deposited $",add])

def withdraw():
    global current
    global transactions
    if current == []:
        print("Please login")
        return
    subtract = int(input("Enter the amount you'd like to withdraw: "))
    print("***************************")
    if subtract > current[2]:
        print("There's not enough in your account")
    else:
        current[2] -= subtract
        print(subtract,"has been withdrawn")
        transactions.append([current[0],"withdrew $",subtract])
    
def transfer():
    global current
    global transactions
    if current == []:
        print("Please login")
        return
    
    person = input("Type in the user's username: ")
    amount = int(input("Type the amount you would like to transfer: "))
    for i in users:
        if person == i[0] and person != current[0] and amount <= current[2]:
            current[2] -= amount
            i[2] += amount
            print("***************************")
            print("Money has been transfered")
            print("***************************")
            transactions.append([current[0],"transferred $",amount,"to",person])
            return
    print("Invalid username or did not have enough funds")
            
    
def check_balance():
    if current == []:
        print("Please login")
        return
    print("You have",current[2],"dollars in your account")
    
def show_transactions():
    if transactions == []:
        print("There are no transactions")
    else:
        print(transactions)

    
def menu():
    print("Welcome to this bank")
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Check Balance")
        print("7. Show Transactions")
        print("*********************************")
        choice=input("Enter Choice: ")
        print("*********************************")

        if choice=="1":
            register()
            
        elif choice=="2":
            login()
            
        elif choice=="3":
            deposit()
            
        elif choice=="4":
            withdraw()
            
        elif choice=="5":
            transfer()
            
        elif choice=="6":
            check_balance()
            
        elif choice=="7":
            show_transactions()
        
        else:
            print("Invalid option, possible options are 1-7")
            
menu()