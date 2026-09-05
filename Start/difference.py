# Find difference between two arrays
import numpy as np

a1 = ([10,20,30,40,50,60,11,22])
a2 = ([11,22,33,44,55,66,10,20])

print("iterating Array1 :")

for n in a1:
    print(n)

print("iterating Array2 :")

for n in a2:
    print(n)

differ = np.setdiff1d(a1,a2)
print(differ)