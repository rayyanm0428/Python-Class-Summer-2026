n = int(input("Enter number: "))

isprime = True

for i in range(2, n):
    if n % i == 0:
        isprime = False
        
if isprime == False:
    print("Number isn't prime")
else:
    print("Number is prime")