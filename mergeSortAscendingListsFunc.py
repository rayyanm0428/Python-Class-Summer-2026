def mergeArrays(list1, list2):
    
    
    merged=[]
    i=0
    j=0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i+=1
        else:
            merged.append(list2[j])
            j+=1
            
    while i < len(list1):
        merged.append(list1[i])
        i+=1
            
    while j < len(list2):
        merged.append(list2[j])
        j+=1
            
    return merged
A=[1,2,3,4,5]
B=[2,3,4,6,10]
C=[1,3,6,7,8]
D=[2,3,7,9,11]
E=[1,4,6,8,9]
F=[2,3,4,6,7]
result = mergeArrays(A,B)
print(result)
result = mergeArrays(C,D)
print(result)
result = mergeArrays(E,F)
print(result)