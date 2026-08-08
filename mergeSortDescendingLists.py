A=[7,5,5,3,1]
B=[10,6,4,3,2]

merged=[]
i=0
j=0

while i < len(A) and j < len(B):
    if A[i] < B[j]:
        merged.append(B[j])
        j+=1
    else:
        merged.append(A[i])
        i+=1
        
while i < len(A):
    merged.append(A[i])
    i+=1
        
while j < len(B):
    merged.append(B[j])
    j+=1
        
print(merged)