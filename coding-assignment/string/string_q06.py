#Frequency of each character
str = input("Enter the string")
frequency = {}
for char in str:
    if char in frequency:
        frequency[char] += 1  
    else:
        frequency[char] = 1   
for char, count in frequency.items():
    print(f"'{char}': {count}")