#existance in list
numbers = []
input_str = input("Enter numbers: ")
for num in input_str.split(","):
    numbers.append(int(num))
exists = 3 in numbers
print(exists)
