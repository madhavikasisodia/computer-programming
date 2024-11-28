#Find the min frequency character in a string
str = input("Enter the sentence: ")
str = str.replace(" ","").lower()
frequency ={}
for char in str:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
min_char = []
min_freq = len(str)
for char in frequency:
    if frequency[char] < min_freq:
        min_freq = frequency[char]
        min_char = [char]
    elif frequency[char] == min_freq:  
        min_char.append(char)
print(f"The Minimum Frequency character is {min_char} with frequency of {min_freq}")