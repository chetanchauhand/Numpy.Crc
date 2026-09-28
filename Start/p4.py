# Cricket Score Anaylezer
import numpy as np

scores = np.array([45, 72, 10, 89, 56, 34, 91, 25, 67, 40])

print("Player Scores:", scores)

print("Highest Score:", np.max(scores))
print("Lowest Score:", np.min(scores))
print("Average Score:", np.mean(scores))
print("Total Runs:", np.sum(scores))

fifties = scores[scores >= 50]

print("50+ Scores:", fifties)