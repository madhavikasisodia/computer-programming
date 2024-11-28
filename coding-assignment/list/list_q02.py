# To find all permutations of string
string = input("Enter the string: ")
n = len(string)
result = [""]


while len(result[0]) != n:  
    current = result.pop(0)
    for char in string:
        if char not in current:
            result.append(current + char)

print("All permutations:", result)