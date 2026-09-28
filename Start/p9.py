#Student marks anaylezer
import numpy as np

marks = np.array([78, 65, 89, 45, 92, 56, 71, 84])

print("Marks:", marks)
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Average:", np.mean(marks))

passed = marks[marks >= 40]
print("Passed Students:", passed)