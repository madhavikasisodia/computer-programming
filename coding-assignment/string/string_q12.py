# count the frequency of word in sentence
sentence = input("Enter string: ")
word = input("Enter the word you want to find frequency: ")

words = sentence.lower().split()
count = 0
for w in words:
    if w.strip(".,!?") == word.lower(): 
        count += 1

print(f"The word '{word}' occurs {count} times in the sentence.")