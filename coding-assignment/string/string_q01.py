#String is Palindrome or not
str = input("Enter the string: ").casefold()

reverse_str = str[::-1]
if str==reverse_str:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")