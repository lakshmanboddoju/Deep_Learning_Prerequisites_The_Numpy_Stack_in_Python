import numpy as np

a = np.array([1, 2])
b = np.array([2, 1])

# Calculating dot product using the formula
dot = 0
for e, f in zip(a, b):
    dot += e * f
print("Dot Product: " + str(dot))

# Try it using numpy arrays
print(a*b)
print("This doesn't provide a dot product but rather an element wise multiplication of the two arrays as the result.")
print("Other ways to do this is to just sum the result here as long as the sizes of the arrays are the same.")
print(np.sum(a*b))
print((a*b).sum())

# Using the dot method/function
print("Dot Product using numpy: " + str(np.dot(a, b)))
print(a.dot(b))

# Now the cosine and angle
aMagnitude = np.sqrt((a*a).sum())
print(aMagnitude)
print("Magnitude using the np.linalg module: " + str(np.linalg.norm(a)))
cosAngle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print("Cosine of Angle is: " + str(cosAngle))
angle = np.arccos(cosAngle)
print("Angle is: " + str(angle) + " radians.")
