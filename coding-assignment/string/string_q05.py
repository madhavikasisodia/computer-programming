#check rotation
st1 = input("Enter the first string: ")
st2 = input("Enter the second string: ")
txt = st1 + st1
if st2 in txt:
    print(f"{st2} is rotation of {st1}")
else:
    print(f"{st2} is not rotation of {st1}")