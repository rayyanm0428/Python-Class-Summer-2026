num = int(input("Enter a number to reverse: "))
reverse = 0

while num!=0:
    digit=num%10
    print("digit extracted:", digit)
    reverse=(reverse * 10) + digit
    num=num//10
print("reverse =", reverse)