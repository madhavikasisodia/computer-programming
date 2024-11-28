#left rotation of a string
str = input("Enter the string: ")
n = int(input("Enter the number of position to rotate: "))
rotated_left = str[n:] + str[:n]
print(f"The {str} left rotation by {n} gives {rotated_left}")

#right rotation of a string
rotated_right = str[-n:] + str[:-n]
print(f"The {str} right rotation by {n} gives {rotated_right}")