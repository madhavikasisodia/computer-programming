# even numbers of a list
numbers = []
str = input("Enter numbers separated by commas: ").split(",")
for num in str:
    numbers.append(int(num))
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)
