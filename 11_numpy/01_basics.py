import numpy as np

# Create arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Dot product
print(np.dot(a, b))   # 32

# Norm (magnitude)
print(np.linalg.norm(a))   # sqrt(1^2 + 2^2 + 3^2) = 3.741...


a = np.array([10, 20, 30, 40, 50])
print(a[0])   # 10
print(a[-1])  # 50

a = np.array([1, 2, 3])
b = 10

print(a + b)   # [11 12 13]

