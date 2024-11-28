# Replace the string vowel with a special character
string = input("Enter string: ")
replacement_char = input("Enter the sign you want to replace vowels with: ")
vowels = "aeiouAEIOU"

result = ""
for char in string:
    if char in vowels:
        result += replacement_char
    else:
        result += char

print("Modified string:", result)