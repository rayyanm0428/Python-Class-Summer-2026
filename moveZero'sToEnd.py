numbers=[2,0,4,0,6,1,0]
count=0

for num in numbers:
    if num == 0:
        numbers.remove(num)
        count += 1
    
for i in range(count):
    numbers.append(0)
    
print(numbers)