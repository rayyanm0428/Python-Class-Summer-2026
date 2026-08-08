A=[1,3,5,5,7]
B=[2,3,4,6,10]

merged=[]
i=0
j=0

while i < len(A) and j < len(B):
    if A[i] < B[j]:
        merged.append(A[i])
        i+=1
    else:
        merged.append(B[j])
        j+=1
        
while i < len(A):
    merged.append(A[i])
    i+=1
        
while j < len(B):
    merged.append(B[j])
    j+=1
        
print(merged)