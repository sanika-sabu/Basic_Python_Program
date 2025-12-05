#Leap year or not

x = int(input("Enter the year "))
if x%4 != 0:
    print("It is not a Leap Year")
elif x%100 != 0:
    print("It is a Leap Year")
elif x%400 != 0:
    print("It is not a Leap Year")
else:
    print("It is a Leap Year")