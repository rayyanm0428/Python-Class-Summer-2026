def calc(n):

    while n !=5:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        n = int(input("Enter the choice: "))
        
        if n == 1:
            a = int(input("First number: "))
            b = int(input("Second number: "))
            print("Sum =", a+b)
        elif n == 2:
            a = int(input("First number: "))
            b = int(input("Second number: "))
            print("Difference =", a-b)    
        elif n == 3:
            a = int(input("First number: "))
            b = int(input("Second number: "))
            print("Product =", a*b)   
        elif n == 4:
            a = int(input("First number: "))
            b = int(input("Second number: "))
            print("Dividend =", a/b)
            
    print("Program ended")
choice = 0
calc(choice)