# average of items in list
numbers = []
str = input("Enter numbers: ").split(",")
for num in str:
    numbers.append(int(num))
average = sum(numbers) / len(numbers)
print("The average of the numbers is:", average)
