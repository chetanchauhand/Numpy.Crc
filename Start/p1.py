#Matrix Calculator

import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Addition:")
print(A + B)

print("Subtraction:")
print(A - B)

print("Multiplication:")
print(A @ B)

print("Transpose of A:")
print(A.T)