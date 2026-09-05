# Reshape Array
import numpy as np

# a = np.array([10,20,30,40,50,60,70,80])

# print("1D array is :",a)

# resarr = a.reshape(2,4)
# print("2D array is :",resarr)

a = np.array([[[1,2,3,4],[11,22,33,44]],[[12,13,14,15],[16,17,18,19]]])

print("3D array is :",a)

reshap = a.reshape(-1)
print("1D array is :",reshap)
