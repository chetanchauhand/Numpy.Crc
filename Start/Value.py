# Search numpy array for value

import numpy as np

a = np.array([10,20,30,440,50,30])

print("Iterating :")
for n in a:
    print(n)

res = np.where(a == 30)
print("\n Element founf at following index: ")
print(res)