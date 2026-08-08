numbers=[12,45,7,89,45,23]

largest=numbers[0]
second=numbers[0]
for num in numbers:
    if num > largest:
        second=largest
        largest=num
    elif num > second and num != largest:
        second=num

print(second,"is the second largest number of the list")