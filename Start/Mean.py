# Find mean , median value in numpy array
import numpy as np
a1 = np.array([10,20,30,40,50])
a2 = np.array([15,25,35,45,55])

print("Array 1 is :",a1)
print("Array 2 is :",a2)

# asarr1 = np.mean(a1)
# asarr2 = np.mean(a2)
asarr1 = np.median(a1)
asarr2 = np.median(a2)

print("\n Mean of Array 1 is :",asarr1)
print("\n Mean of Array 2 is :",asarr2)
