numbers = [1, 2, 3, 5, 6]

length = len(numbers) - 1

for i in range(length):
    if numbers[i+1] - numbers[i] != 1:
        print("The missing number is", i+2)