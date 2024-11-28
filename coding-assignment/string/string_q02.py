#Reverse words in a given string in python
str = input("Enter the sentence: ").split()
reverse_word = ' '.join(word[::-1]for word in str)
print(reverse_word)