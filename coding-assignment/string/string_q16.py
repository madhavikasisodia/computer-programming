# string startswith
string = input("Enter the string: ").casefold()
str = input("Enter the string you want the word to start with: ")
out = string.startswith(str)
if out==True:
    print(f"The {string} starts with {str}")
else:
    print(f"The {string} does not starts with {str}")