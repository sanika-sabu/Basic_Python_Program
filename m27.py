a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
d = b**2 - 4*a*c
if d > 0:
    root1 = (-b + (d ** 0.5)) / (2 * a)
    root2 = (-b - (d ** 0.5)) / (2 * a)
    print(f"Two distinct real roots: {root1} and {root2}")
elif d == 0:
    root = -b / (2 * a)
    print(f"One real root (repeated): {root}")
else:
    real_part = -b / (2 * a)
    imag_part = (abs(d) ** 0.5) / (2 * a)
    print(f"Two complex roots: {real_part} + {imag_part}i and {real_part} - {imag_part}i")