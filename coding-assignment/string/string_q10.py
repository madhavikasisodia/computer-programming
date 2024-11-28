#count the number of vowels in a string
string = input("Enter the string: ")
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)