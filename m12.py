#Perfect Number

x = int(input("Enter a number "))
ls=[]
for i in range(1,x):
    if x % i == 0:
        ls.append(i)
total_sum = sum(ls)
if x == total_sum:
    print("Perfect Number")
else:
    print("Not Perfect Number")