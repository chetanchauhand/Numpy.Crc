# Get minimum value with axes in nummpy
import numpy as np

a = np.array([[1,4,2,6,5],[30,10,30,12,50],[300,100,200,500,600]])

print("Iterative value : ")

for n in a:
    print(n)

print("\n Minimum value is : ", a.min())
print("\n Minimum value at 0 axis(Verticle Axes) :"),a.min(axis = 0)
print("\n Minimum value at 1 axis(Horizontal Axes) :",a.min(axis = 1))