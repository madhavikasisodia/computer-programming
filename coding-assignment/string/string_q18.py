# Remove vowel
input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
output_string = ''.join([char for char in input_string if char not in vowels])

print("String after removing vowels:", output_string)