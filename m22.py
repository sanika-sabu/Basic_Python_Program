n = int(input("Enter the number "))
ans = 0
x = n
while x != 0:
    ans = ans+((x%10)**3)
    x = x//10
if ans == n:
    print("The number is armstrong")
else:
    print("The number is not armstrong")