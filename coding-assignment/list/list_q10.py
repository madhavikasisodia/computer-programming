#occurance of string in list
numbers = []
str = input("Enter numbers separated by commas: ").split(",")
for num in str:
    numbers.append(int(num))
num = input("Enter the number you want to find occurence: ")
count = numbers.count(num)
print("Count of 1:", count)

