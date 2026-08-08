num = int(input("Enter a number to reverse: "))
reverse = 0
original = num

while num!=0:
    digit=num%10
    print("digit extracted:", digit)
    reverse=(reverse * 10) + digit
    num=num//10
print("reverse =", reverse)
if reverse == original:
    print("Number is palindrome")
else:
    print("Number is not a palindrome")