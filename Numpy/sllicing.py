import numpy as np

# create 2d arrey
arr = np.array([[1,3,5,8],[7,8,9,5],[7,2,3,0]])

print(arr)
print(np.size(arr))
print(np.shape(arr))
print(np.ndim(arr))

print(arr[0:2,0:2])
print(arr[0,0:3])