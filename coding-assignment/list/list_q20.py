#Reverse each word in a list of strings
words = []
str = input("Enter words: ").split(",")
for word in str:
    words.append(word.strip())
reversed_words = [word[::-1] for word in words]
print("Reversed words:", reversed_words)
