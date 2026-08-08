a = str(input("Enter username: "))
if a != "rayyan0428":
    print("This user does not exist")
else:
    b = str(input("Enter password: "))

if a == "rayyan0428" and b == "password":
    print("Login successful")
    print("Welcome", a)
elif a == "rayyan0428" and b != "password":
    print("Incorrect password, please try again")
    