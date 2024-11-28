#remove last element from list
numbers = []
str = input("Enter numbers: ").split(",")
for num in str:
    numbers.append(int(num))
    numbers.pop()
print("The list after removing the last element is:", numbers)
