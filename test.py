import numpy as np

A = np.array([[2, 2], [3, 4]])

mean = A.mean(axis = 1)
std = A.std(axis = 1)

print(mean)
print((A - mean)/std)
