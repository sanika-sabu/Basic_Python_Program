x = input("Enter the string ").lower()
for i in x:
    if i not in "aeiou":
        print(i, end="")