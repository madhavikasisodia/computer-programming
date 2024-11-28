# remove specific element from list
numbers = []
str = input("Enter numbers: ").split(",")
for num in str:
    numbers.append(int(num))
remove_num = int(input("Enter the number to remove from the list: "))
if remove_num in numbers:
    numbers.remove(remove_num)
    print(f"The list after removing {remove_num}:", numbers)
else:
    print(f"{remove_num} is not in the list.")
