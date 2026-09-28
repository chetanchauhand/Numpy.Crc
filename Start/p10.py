# Random number anaylezer
import numpy as np

numbers = np.random.randint(1, 101, 10)

print("Numbers:", numbers)
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Average:", np.mean(numbers))
print("Total:", np.sum(numbers))