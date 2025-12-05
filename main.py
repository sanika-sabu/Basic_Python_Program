x = int(input("enter a num "))
if x % 2 != 0:
    print ("Weird")
elif x in range(2,6):
    print ("Not weird")
elif x in range(6,21):
    print ("Weird")
else:
    print ("Not Weird")