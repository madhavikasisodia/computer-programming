#Removing duplicates and sort the result alphabetically 
str = input("Enter the string: ").casefold()
result = ""
for char in str:
    if char not in result:
        result += char
sort_result = ''.join(sorted(result))
print(f"The result of \"{str}\" after removing all duplicates is \"{result}\"")
print(f"The result of \"{str}\" after removing all duplicates and sort the alphabets is \"{sort_result}\"")