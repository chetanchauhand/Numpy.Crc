#Random Number Simulator
import numpy as np

numbers = np.random.randint(1, 11, 20)

print("Generated Numbers:")
print(numbers)

even = numbers[numbers % 2 == 0]
odd = numbers[numbers % 2 != 0]

print("Even Numbers:", even)
print("Odd Numbers:", odd)

print("Even Count:", len(even))
print("Odd Count:", len(odd))