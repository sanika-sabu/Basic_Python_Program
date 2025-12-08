x = int(input("Enter a number: "))
y = x
print(y, end=" ")
while x % 2 == 0:
    print(2, end=" ")
    x = x // 2
i = 3
while i * i <= x:
    while x % i == 0:
        print(i, end=" ")
        x = x // i
    i += 2
if x > 1:
    print(x, end=" ")
print()