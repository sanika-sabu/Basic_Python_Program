#Anagram

x = input("enter the first string ")
y = input("enter the second string ")
if sorted(x.lower()) == sorted(y.lower()):
    print("Anagram")
else:
    print("Not Anagram")