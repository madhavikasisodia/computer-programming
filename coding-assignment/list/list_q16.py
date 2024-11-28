# product of list elements
numbers = []
str = input("Enter numbers: ").split(",")
for num in str:
    numbers.append(int(num))
product = 1
for num in numbers:
    product *= num
print("The product of all numbers in the list is:", product)
