sentence = "I am going on a run today"
words = sentence.split()
longest = ""

i=0

print(len(words))
while i<len(words):
    if len(words[i]) > len(longest):
        longest = words[i]
    i += 1

print("Longest word:", longest)