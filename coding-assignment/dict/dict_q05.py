# add new key-value pair to dictionary
dict = {}
initial_count = int(input("Enter the number of items in the initial dictionary: "))
for i in range(initial_count):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value for {key}: ")
    dict[key] = value
n = int(input("Enter the number of new items to add to the dictionary: "))
for i in range(n):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value for {key}: ")
    dict[key] = value

# Print the updated dictionary
print("The updated dictionary is:", dict)

