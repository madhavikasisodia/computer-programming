# find a value by its key
dict = {}
n = int(input("Enter the number of items in the dictionary: "))
for i in range(n):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value for {key}: ")
    dict[key] = value

# Search for a key
search_key = input("Enter the key to search for: ")
if search_key in dict:
    print(f"The value for '{search_key}' is:", dict[search_key])
else:
    print(f"The key '{search_key}' does not exist in the dictionary.")
