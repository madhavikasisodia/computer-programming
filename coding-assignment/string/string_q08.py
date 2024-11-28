#Reverse the sort of a string
st = input("Enter the string: ").casefold()
rev = ''.join(sorted(st, reverse = True)) 
print("The original string : " + str(st)) 
print("String after reverse sorting : " + str(rev)) 