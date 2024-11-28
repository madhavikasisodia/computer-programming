#reverse a dictionary
original_dict = {}
n = int(input("How many items do you want to add to the dictionary? "))
for i in range(n):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value for key '{key}': ")
    original_dict[key] = value
reversed_dict = {v: k for k, v in original_dict.items()}
print("Reversed dictionary:", reversed_dict)
