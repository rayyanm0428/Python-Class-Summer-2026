contacts={}

def add_contact():
    name=input("Enter name: ")
    phone=input("Enter phone number: ")
    
    contacts[name]=phone
    
    print("Contact added!")
    
def search_contact():
    name=input("Enter name: ")
    
    if name in contacts:
        print("Phone: ", contacts[name])
    else:
        print("Contact not found.")
        
def delete_contact():
    name=input("Enter name: ")
    
    if name in contacts:
        del contacts[name]
        print("Contact Deleted!")
    else:
        print("Contact not found")

def view_contacts():
    
    if len(contacts)==0:
        print("No contacts found, the contact book is currently empty")
        
    for name, phone in contacts.items():
        print("Name: ", name,"Contact", phone)
        
def menu():
    
    while True:
        print("1. Add a Contact")
        print("2. Search Contact")
        print("3. Delete a contact")
        print("4. View all contacts")
        print("5. Exit")
        
        choice=input("Choice: ")
        
        if choice=="1":
            add_contact()
        elif choice=="2":
            search_contact()
        elif choice=="3":
            delete_contact()
        elif choice=="4":
            view_contacts()
        elif choice=="5":
            print("Quitting the contact book")
            break
        
menu()