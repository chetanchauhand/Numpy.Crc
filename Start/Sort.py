# Sorting using 1D array
import numpy as np

# a = ([10,20,1,9,45,31,11,12,15,55,43,22]) # 1D array
a = ([[70,50,30,10],[77,22,33,11]])

print("Iterating array is: ")
for n in a:
    print(n)

rs = np.sort(a)

print("Here is the following sorted array: ")
print(rs)