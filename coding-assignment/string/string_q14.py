#Balancing paranthesis with '*'
st = input("Enter string: ")
count = 0
astrk = 0
for i in st:
    if i == '(':
        count += 1
        astrk += 1
    elif i == ')':
        count -= 1
        astrk -= 1     
    else:
        count -= 1
        astrk += 1 

    if count < 0 or count>0:
        count = 0
    if astrk < 0 or astrk>0:
        print(False)
        break
else:
    if count == 0:
        print(True)