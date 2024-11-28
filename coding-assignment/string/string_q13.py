# Split the string into half such that if odd first half will have more and second half less
string = input("Enter the string: ")

split_index = (len(string) + 1) // 2  

first_half = string[:split_index]
second_half = string[split_index:]

print("First half:", first_half)
print("Second half:", second_half)
