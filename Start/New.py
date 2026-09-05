# 1D array iterate in numpy
import numpy as np

# a = np.array([1,2,3,4,5,6,7,8]) 
# a = np.array([[1,2],[2,3],[4,5],[5,6]])
a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("Iteration")

for x in a:
    print(x)

print("type :",type(a))
print("Datatype :",a.dtype)
print("Dimension :",a.ndim)