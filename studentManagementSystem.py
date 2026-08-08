students = []

def add_student():
    name=input("Enter student's name: ")
    marks=int(input("Enter Marks: "))

    students.append([name,marks])
    print("*********************************")
    print("Student added successfully")
    print("*********************************")
    
def view_students():
    if len(students)==0:
        print("*********************************")
        print("No students found")
        print("*********************************")
        return

    for i in students:
        print("*********************************")
        print("Name: ",i[0],"Marks: ",i[1])    
        print("*********************************")

def find_topper():
    if len(students)==0:
        print("*********************************")
        print("No students found")
        print("*********************************")
        return
    
    topper=students[0]

    for i in students:
        if i[1]>topper[1]:
            topper=i
    print("*********************************")
    print("Topper: ",topper[0],"Marks: ",topper[1])
    print("*********************************")

def calculate_average():
    if len(students)==0:
        print("*********************************")
        print("No students found")
        print("*********************************")
        return
    
    total=0
    
    for i in students:
        total += i[1]
        
    average=total/len(students)
    print("*********************************")
    print("Average Marks =",average)
    print("*********************************")

def delete_students():
    if len(students)==0:
        print("*********************************")
        print("No students found")
        print("*********************************")
        return
    name = input("Enter student's name: ")
    for i in students:
        if i[0] == name:
            students.remove(i)
            print("*********************************")
            print("Student has been removed succesfully")
            print("*********************************")
            return
    print("*********************************")
    print("Please type in a valid student name")
    print("*********************************")
            
def search_students():
    if len(students)==0:
        print("*********************************")
        print("No students found")
        print("*********************************")
        return
    name = input("Enter student's name: ")
    for i in students:
        if i[0] == name:
            print("*********************************")
            print("Name:",i[0],"Marks:",i[1])
            print("*********************************")
            return
    print("*********************************")    
    print("Student not found")
    print("*********************************")

def total_students():
    count = len(students)
    print("The amount of students are:",count)
    
def update_marks():
    if len(students)==0:
        print("*********************************")
        print("No students found")
        print("*********************************")
        return

    name = input("Which student's marks would you like to change: ")
    print("*********************************")
    for i in students:
        if i[0] == name:

            update = int(input("Type the updated marks: "))
            print("*********************************")
            i[1] = update
            return
    print("*********************************")    
    print("Student not found")
    print("*********************************")

def within_eighty():
    eightyPlus = []
    for i in students:
        if i[1] > 80:
            eightyPlus.append(i[0])
    
    if eightyPlus != []:
        print(eightyPlus)
    else:
        print("No students found")
            
def letter_grade():
    if len(students)==0:
        print("*********************************")
        print("No students found")
        print("*********************************")
        return
    for i in students:
        if i[1] > 89:
            i.append("A")
        elif i[1] > 79:
            i.append("B")
        elif i[1] > 69:
            i.append("C")
        elif i[1] > 59:
            i.append("D")
        else:
            i.append("F")
    print(students)
        


def menu():
    print("Welcome to the Student Management System")
    while True:
        print("1. Add Students")
        print("2. View Students")
        print("3. Find Topper")
        print("4. Calculate Average")
        print("5. Exit")
        print("6. Remove Students")
        print("7. Search Students")
        print("8. Total Students")
        print("9. Update Marks")
        print("10. Within 80")
        print("11. Letter Grade")
        print("*********************************")
        choice=input("Enter Choice: ")
        print("*********************************")

        if choice=="1":
            add_student()
            
        elif choice=="2":
            view_students()
            
        elif choice=="3":
            find_topper()
            
        elif choice=="4":
            calculate_average()
            
        elif choice=="5":
            print("Closing Student Management System, Thank you! ")
            break
        elif choice=="6":
            delete_students()
            
        elif choice=="7":
            search_students()
            
        elif choice=="8":
            total_students()
            
        elif choice=="9":
            update_marks()
            
        elif choice=="10":
            within_eighty()
        
        elif choice=="11":
            letter_grade()
        
        else:
            print("Invalid option. Possible options are only 1,2,3,4 and 5")
        
menu()