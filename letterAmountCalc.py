text = input("Enter text: ")

size = len(text)

i=0
checked=""
while i < size:
    ch=text[i]
    
    if ch not in checked:
        j=0
        count=0
        
        while j < size:
            if text[j] == ch:
                count += 1
            j += 1
            
        print(ch, ":", count)
        checked +=ch
    i +=1