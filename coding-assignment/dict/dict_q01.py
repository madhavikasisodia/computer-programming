#Find the max frequency character in a string
str = input("Enter the sentence: ")
str = str.replace(" ","").lower()
frequency ={}
for char in str:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
max_char = []
max_freq = 0
for char in frequency:
    if frequency[char] > max_freq:
        max_freq = frequency[char]
        max_char = [char]
    elif frequency[char] == max_freq:  
        max_char.append(char)
print(f"The Minimum Frequency character is {max_char} with frequency of {max_freq}")