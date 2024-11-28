#remove duplicates from list
numbers_input = input("Enter numbers: ").split(",")
numbers = [int(num) for num in numbers_input]
unique_numbers = list(set(numbers))
print("List without duplicates:", unique_numbers)
