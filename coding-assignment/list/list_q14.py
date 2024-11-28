# whether the list is sorted or not
numbers = []
str = input("Enter numbers: ").split(",")
for num in str:
    numbers.append(int(num))
if numbers == sorted(numbers):
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted.")
