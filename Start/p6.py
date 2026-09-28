# temprature Analyzer
import numpy as np

temperature = np.array([32, 35, 31, 29, 36, 38, 34, 33, 30, 37])

print("Temperature:", temperature)
print("Average:", np.mean(temperature))
print("Highest:", np.max(temperature))
print("Lowest:", np.min(temperature))

hot_days = temperature[temperature > 35]

print("Temperature above 35:", hot_days)