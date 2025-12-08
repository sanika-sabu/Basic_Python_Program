n = int(input("Enter array size n: "))
arr = list(map(int, input(f"Enter {n} numbers: ").split()))
result = 0
i = 0
while i <= n:
    result = result ^ i
    j = 0
    while j < n:
        if arr[j] == i:
            result = result ^ arr[j]
            break
        j += 1
    i += 1
print(result)