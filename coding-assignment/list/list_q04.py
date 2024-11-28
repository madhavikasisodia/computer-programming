#Sum of list elements
number = input("Enter the numbers: ").split(",")
numbers = [int(num) for num in number]  # Convert each string to an integer
total = sum(numbers)
print("Sum of elements:", total)


