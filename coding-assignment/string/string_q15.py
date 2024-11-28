#Append new string in the middle of a given string
original_string = input("Enter the string: ")
new_string = input("Enter the change: ")

middle_index = len(original_string) // 2

result = original_string[:middle_index] + new_string + original_string[middle_index:]

print(result)
