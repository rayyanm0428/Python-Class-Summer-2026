choice = 0

while choice !=5:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = int(input("Enter the choice: "))
    
    if choice == 1:
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Sum =", a+b)
    elif choice == 2:
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Difference =", a-b)    
    elif choice == 3:
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Product =", a*b)   
    elif choice == 4:
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Dividend =", a/b)
        
print("Program ended")
