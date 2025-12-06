x = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
y = input("Enter the number: ")
for i in y:
    if i=="-":
        print("Minus",end=" ")
    else:
        print(x[int(i)], end =" ")
