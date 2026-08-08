sentence = "I went on a run"

count = 0

for letter in sentence:
    if letter not in "aeiouAEIOU ":
        count = count+1
    
print("The total number of consonants in this sentence is:", count)