#first occurence of a number
numbers = []
str = input("Enter numbers: ").split(",")
for num in str:
    numbers.append(int(num))  
search_num = int(input("Enter the number to find its first occurrence index: "))
if search_num in numbers:
    index = numbers.index(search_num)
    print(f"Index of first occurrence of {search_num}:", index)
else:
    print(f"{search_num} is not in the list.")
