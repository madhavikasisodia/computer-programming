# merge list
list1 = []
list2 = []
str1 = input("Enter numbers for the first list: ").split(",")
for num in str1:
    list1.append(int(num))
str2 = input("Enter numbers for the second list: ").split(",")
for num in str2:
    list2.append(int(num))
merged_list = list1 + list2
print("The merged list is:", merged_list)
