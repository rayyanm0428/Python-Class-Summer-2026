numbers = [2,4,4,3,9,1,9,8,7,3]
length = len(numbers)
unique=[]

for i in range(length):
    if numbers[i] in unique:
        print("Found a duplicate of", numbers[i])
    unique.append(numbers[i])