# Join 2 numpy array using DStack()
import numpy as np
# a1 = np.array([1,3,4,6,7,8])
# a2 = np.array([10,12,11,14,13,19])

# print("Iterating : ")

# for n in a1:
#     print(n)

# for n in a2:
#     print(n)

# ressar = np.dstack((a1,a2))
# print("Array along with :",ressar)

a1 = np.array([1,3,4,6,7,8])
a2 = np.array([10,12,11,14,13,19])

print("Iterating : ")

for n in a1:
    print(n)

for n in a2:
    print(n)

ressar = np.column_stack((a1,a2))
print("Array along with :",ressar)