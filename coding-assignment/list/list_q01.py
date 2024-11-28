#To find longest word in a string
lst = []
while True:
    word = input("Enter a word (or press space to stop): ")
    if word == " ":
        break
    lst.append(word)
longest = ""
length = 0
for word in lst:
    if len(word) > length:
        longest = word
        length = len(word)
print(f"The longest word is '{longest}' with length {length}.")