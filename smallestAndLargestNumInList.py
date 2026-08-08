numbers=[12,45,7,89,23]

largest=numbers[0]
smallest=numbers[0]

for num in numbers:
    if num > largest:
        largest=num
    elif num < smallest:
        smallest=num
        
print("Largest number of the array is",largest)
print("Smallest number of the array is",smallest)