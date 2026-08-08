def checkPrime(n):
    isPrime = True
    for i in range(2,n):
        if n % i == 0:
            isPrime = False
    return isPrime


num = 3
prime = []
num1 = 5000
prime2 = []

while num < 1000:
    
    if checkPrime(num):
        prime.append(num)
    num +=1
while num1 < 10000:
    
    if checkPrime(num1):
        prime2.append(num1)
    num1 +=1
    
print(prime)
print(prime2)