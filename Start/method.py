# concatenate method and stack and Vstack method

import numpy as np

# a1 = np.array([10,20,30,40,50,60])
# a2 = np.array([11,22,33,44,55,66])
# print("itreating Array 1:")
# for n in a1:
#     print(n)

# print("itreating Array 2:")
# for n in a2:
#     print(n)

# resarr = np.concatenate((a1,a2))

# print(resarr)

# using Stack method

# a1 = np.array([10,20,30,40,50,60])
# a2 = np.array([11,22,33,44,55,66])
# print("itreating Array 1:")
# for n in a1:
#     print(n)

# print("itreating Array 2:")
# for n in a2:
#     print(n)

# resarr = np.stack((a1,a2),axis=1)

# print(resarr)


a1 = np.array([10,20,30,40,50,60])
a2 = np.array([11,22,33,44,55,66])
print("itreating Array 1:")
for n in a1:
    print(n)

print("itreating Array 2:")
for n in a2:
    print(n)

resarr = np.vstack((a1,a2))

print("Joining in column \n:", resarr)



