num = int(input("Enter The Number: "))

i = 1
sumOfFactors = 0
while i<num:
    if num % i == 0:
        sumOfFactors = sumOfFactors + i
    i = i+1
    
if sumOfFactors == num:
    print("Its a perfect number")
else:
    print("Its not a perfect number")