#Longest word in a list
word = input("Enter the items of the list: ").split(',')
list = word
longest_word = max(list, key=len)

print("The longest word is:", longest_word)
