def check_perfect(n):
    i = 1
    sumOfFactors = 0
    while i<n:
        if n % i == 0:
            sumOfFactors = sumOfFactors + i
        i = i+1
    
    if sumOfFactors == n:
        return True
    else:
        return False
        
for i in range(1, 5000):
    if check_perfect(i)==True:
        print(i)