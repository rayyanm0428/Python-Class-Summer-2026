products={}

def add_product():
    name = input("Type the new product: ")
    if name in products:
        print("Product already exists")
    
    quantity = int(input("Type the amount you'd like to add: "))
    products[name] = quantity
    print("Product added")

def update_quantity():
    name = input("Type the product whose quantity you are updating: ")
    if name not in products:
        print("Product doesn't exist")
    
    quantity = int(input("Type the amount you'd like to add: "))
    products[name] += quantity
    print("Quantity updated")
    
def view_inventory():
    if len(products) == 0:
        print("No products in inventory")
    
    for name, quantity in products.items():
        print("Name: ", name, "Quantity: ", quantity)
    
    
def menu():
    
    while True:
        print("1. Add a Product ")
        print("2. Update Quantity")
        print("3. View Inventory")
        print("4. Exit")
        
        choice=input("Choice: ")
        
        if choice=="1":
            add_product()
        elif choice=="2":
            update_quantity()
        elif choice=="3":
            view_inventory()
        elif choice=="4":
            print("Quitting the inventory management system")
            break
        
menu()