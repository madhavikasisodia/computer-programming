# string endswith
string = input("Enter the string: ").casefold()
str = input("Enter the string you want the word to start with: ")
out = string.endswith(str)
if out==True:
    print(f"The {string} ends with {str}")
else:
    print(f"The {string} does not ends with {str}")