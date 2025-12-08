#Parantheses

st = "({[]})"
stack = []
mapping = {")":"(", "]":"[", "}":"{"}
flag = 0
for i in st:
    if i in "{[(":
        stack.append(i)
    else:
        if not stack or mapping[i] != stack[-1]:
            print("Invalid")
            flag = 1
            break
        stack.pop()
if not stack or flag == 0:
    print("Valid")