# sort a list
numbers = []
input_str = input("Enter numbers: ")
for num in input_str.split(","):
    numbers.append(int(num))
sorted_list = sorted(numbers)
print("Sorted list:", sorted_list)
