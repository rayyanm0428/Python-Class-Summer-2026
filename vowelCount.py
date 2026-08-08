sentence = "Something is fishy. Andy loves fishing"

count = 0

for letter in sentence:
    if letter in "aeiouAEIOU":
        print(letter)
        count = count+1
print("The total number of vowels in this sentence is:", count)