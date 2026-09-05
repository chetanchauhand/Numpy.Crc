# find Intersection between two unsorted 

import numpy as np

a1 = np.array([13,12,11,15,10])
a2 = np.array([22,25,21,20,18])

print("Iterated Array1 :")

for n in a1:
    print(n)

print("Iterated Array2 :")

for n in a2:
    print(n)

rs = np.intersect1d(a1,a2)
print("\n intersection of  array is = \n",rs)
