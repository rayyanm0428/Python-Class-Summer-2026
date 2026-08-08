def combination(nums, target):
    output = []
    max = len(nums)
    for i in range(max):
        for j in range(i+1, max):
            if nums[i] + nums[j] == target:
                output.append([nums[i],nums[j]])
    return output            
group = [1,2,3,4,5,6,7,8,9]
add = int(input("Whats the target number: "))
print(combination(group,add))