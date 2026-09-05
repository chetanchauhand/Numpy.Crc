# Intersection between Two arrays

import numpy as np

a1 = np.array([10,20,30,40,100,103])
a2 = np.array([15,25,103,100,35,55])

print("iterating array1 :")

for n in a1:
    print(n)

print("iterating array2 :")

for n in a2:
    print(n)

rs = np.intersect1d(a1,a2)
print("\n Intersection \n :",rs)