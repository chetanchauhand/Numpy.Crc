#check how many dimensions a numpy array has
import numpy as np
a1= np.array((1))
a2=np.array((10,20,30,40,50))
a3=np.array([[1,2,3,4,5],[2,4,6,8,9]])
print("Array1 ...\n",a1)
print("Array2....\n",a2)
print("array3...\n",a3)

print("\n Array1 dimension ...\n",a1.ndim)
print("\n Array2 dimension ...\n",a2.ndim)
print("\n Array3 dimension...\n",a3.ndim)
