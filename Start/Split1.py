# Access element from splited array

import numpy as np

# a = ([1,2,3,6,7,8]) # 1D array
a = ([[1,2,3,4],[5,6,7,8]])

print("After iteration")

for n in a:
    print(n)

print("Spliting array :")

resarr = np.array_split(a,2)
print(resarr)

print("Access Splited array is: ")
print("Array 1 :",resarr[0])
print("Array 2 :",resarr[1])