A=[1,2,3,4,5,6,7,8,9,10]
B=[]

amt = int(input("Enter num: "))


length=len(A)


for i in range(length-amt, length):
    B.append(A[i])
    count=i
for i in range(0,length-amt):
    B.append(A[i])

print(B)