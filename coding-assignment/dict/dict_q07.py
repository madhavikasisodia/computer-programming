# count word in sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word frequency:", word_count)
