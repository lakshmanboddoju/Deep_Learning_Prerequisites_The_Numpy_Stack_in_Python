import numpy as np

L = [1, 2, 3]
A = np.array([1, 2, 3])

for e in L:
    print(e)

for e in A:
    print(e)

# Works
L.append(4)

# Doesn't work
try:
    A.append(4)
except:
    print("Can't append to numpy array.")

# Works
L = L + [5, 6]

# Dosn't work
try:
    A = A + [4, 5, 6]
except:
    print("Can't append list to numpy array.")

L2 = []

# To add each element to itself
for e in L:
    L2.append(e + e)
print(L2)

# Same thing in numpy i.e. Vector Addition
A2 = A + A
print(A2)

# Vector Multiplication in numpy
print(2*A)

# Trying the same thing in lists
print(2*L)
print("Not what we expected.")

L2 = []
for e in L:
    L2.append(e * 2)
print(L2)

# Element wise squaring
try:
    print(L**2)
except:
    print("Can't square list elements using **.")

L2 = []
for e in L:
    L2.append(e*e)
print(L2)

# Same in Numpy
print(A**2)

# Other common functions
print(np.sqrt(A))
print(np.log(A))
print(np.exp(A))
