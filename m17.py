#PYRAMID

for i in range(5):
    for j in range(5): #column
        print(i, end=" ")
    print()

for i in range(1,6):
    for j in range(i): #column
        print("*", end=" ")
    print()

for i in range(1,6):
    for j in range(i): #column
        print(i, end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1): #column
        print(j, end=" ")
    print()

for i in range(5,0,-1):
    for j in range(i): #column
        print(i, end=" ")
    print()

for i in range(5,0,-1):
    for j in range(i): #column
        print(5, end=" ")
    print()

for i in range(0,6):
    for j in range(i+1): #column
        print(2*i+1, end=" ")
    print()