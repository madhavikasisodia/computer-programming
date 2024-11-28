#Flatten a list
nested_list = []
num_of_sublists = int(input("How many sublists do you want to enter? "))
for _ in range(num_of_sublists):
    str = input("Enter numbers for the sublist: ").split(",")
    sublist = [int(num) for num in str]
    nested_list.append(sublist)  
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened_list)
