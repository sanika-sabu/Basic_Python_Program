x = 434
y =x
r=0
while x !=0:
    l =  x%10
    r = r*10+l
    x = x//10
print(r)
if r!=y:
    print("not palindrome")
else:
    print("palindrome")