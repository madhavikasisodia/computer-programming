#list of squares
numbers = []
input_str = input("Enter numbers: ")
for num in input_str.split(","):
    numbers.append(int(num))
squares = [num ** 2 for num in numbers]
print("List of squares:", squares)

