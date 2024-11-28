# check for key existence
dict = {}
n = int(input("Enter the number of items in the dictionary: "))
for i in range(n):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value for {key}: ")
    dict[key] = value
search_key = input("Enter the key to check: ")
if search_key in dict:
    print(f"The key '{search_key}' exists in the dictionary.")
else:
    print(f"The key '{search_key}' does not exist in the dictionary.")
