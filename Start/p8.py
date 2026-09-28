#Fitness tracker
import numpy as np

steps = np.array([5000, 7200, 8500, 4000, 10000, 9200, 6500])

print("Daily Steps:", steps)
print("Total Steps:", np.sum(steps))
print("Average Steps:", np.mean(steps))
print("Most Steps:", np.max(steps))

days = np.sum(steps >= 8000)
print("Days with 8000+ steps:", days)