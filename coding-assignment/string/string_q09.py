#anagrams
string1 = input("Enter first word: ")
string2 = input("Enter second word: ")
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()
are_anagrams = sorted(string1) == sorted(string2)
if are_anagrams == True:
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")