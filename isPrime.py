num = 3
prime = []


while num < 1000:
    isPrime = True
    for i in range(2,num):
        if num % i == 0:
            isPrime = False
    if isPrime == True:
        prime.append(num)
    num +=1

print(prime)