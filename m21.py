x = int(input("Enter the number "))
y = x**2
len = len(str(x))
if y%(10**len)==x:
    print("The number is automorphic")
else:
    print("The number is not automorphic")
