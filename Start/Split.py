# Split in array 

import numpy as np

a = np.array([10,20,30,11,22,33])

print("Spliting :")

for n in a:
    print(n)

print("Array after spliting return 2 arrays ")
resarr = np.array_split(a,2)
for n in resarr:

    print("Splited array is :",n)