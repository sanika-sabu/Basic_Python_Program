#Smallest number in the list

x = [12,5,7,3,8]
y = x[0]
for i in x:
    if i < y:
        y = i
print(y)