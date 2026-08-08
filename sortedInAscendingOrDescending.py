numbers=[12,45,7,89,45,23]
numbersA=[2,5,7,9,12]
numbersD=[12,7,6,4,1]

length=len(numbers)-1
ascend = 0
descend = 0

for i in range(length):
    if numbers[i] <= numbers[i+1]:
        ascend += 1
    elif numbers[i] >= numbers[i+1]:
        descend += 1
if ascend == length:
    print("List is sorted in ascending order")
elif descend == length:
    print("List is sorted in descending order")
else:
    print("List isn't sorted")