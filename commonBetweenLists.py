def common(nums1, nums2):
    commonL = []
    maxFirst = len(nums1)
    maxSecond = len(nums2)
    for i in range(maxFirst):
        for j in range(maxSecond):
            if nums1[i] == nums2[j] and nums1[i] not in commonL:
                commonL.append(nums1[i])
    return commonL
list1 = [2,3,4,2,3,4]
list2 = [1,2,3,5,2,3,1,7,8,7]
print(common(list1,list2))