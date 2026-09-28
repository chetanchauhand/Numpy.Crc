# Pixel Anaylezer
import numpy as np

image = np.array([
    [50, 100, 150],
    [200, 100, 50],
    [255, 180, 80]
])

print("Original Image:")
print(image)

# Increase brightness
bright_image = image + 30

# Values 255 se zyada nahi honi chahiye
bright_image = np.clip(bright_image, 0, 255)

print("Bright Image:")
print(bright_image)