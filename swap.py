numbers=[12,76,94,55,32,45,10]

start=0
end=len(numbers)-1

while start < end:
    numbers[start]=numbers[start]+numbers[end]
    numbers[end]=numbers[start]-numbers[end]
    numbers[start]=numbers[start]-numbers[end]
    
    start += 1
    end -= 1
    
print(numbers)