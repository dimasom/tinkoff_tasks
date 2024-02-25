import numpy as np
numbers = input().split()
A = int(numbers[0])
B = int(numbers[1])
C = int(numbers[2])
D = B**2 - 4*A*C
if D > 0:
    x1 = (-B + np.sqrt(D))/(2*A)
    x2 = (-B - np.sqrt(D)) / (2 * A)
    print(min(x1, x2),max(x1,x2))
if D == 0:
    x = -B/(2*A)
    print(x)