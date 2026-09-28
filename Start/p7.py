#Train seat anaylezer
import numpy as np

# 0 = Available
# 1 = Booked

seats = np.array([
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1]
])

print("Seat Arrangement:")
print(seats)

print("Total Seats:", seats.size)
print("Booked Seats:", np.sum(seats))
print("Available Seats:", np.sum(seats == 0))