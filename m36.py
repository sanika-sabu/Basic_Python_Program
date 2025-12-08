x = [1, 2, 3]
n = len(x)
p = []
for i in range(2**n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(x[j])
    p.append(subset)
print(p)