#Reverse a list
numbers_input = input("Enter numbers: ").split(",")
numbers = [int(num) for num in numbers_input]
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)

