import numpy as np


array_1D = np.arange(10)
print("1D Array : ", array_1D)

print("3rd ele : ", array_1D[2])
print("4th ele : ", array_1D[3])
print("last ele : ", array_1D[-1])
print("2nd last ele : ", array_1D[-2])# second last ele
print("3rd last ele : ", array_1D[-3])

print("first 5 ele : ", array_1D[:5]) # ele from start to index 4
print("every 2nd ele : ", array_1D[::2])  # every 2nd ele
print("Array revesed  : ", array_1D[::-1])

array_2d = np.arange(10,22).reshape(3,4)
print("2 d array : ", array_2d)

# accessing entire rows and columns
print("Enitre 1st row : ", array_2d[0, :]) # first row)
print("Entire 2nd column : ", array_2d[:,1])  # second column

# Slicing to extract a subarray
subarray = array_2d[:2, -2:] # first 2 row and last 2 col
print("Subarray (first 2 rows, last 2 col): ", subarray)

# Extracting every other element
sliced_array = array_1D[::2] # Every other element along rows and col
print("Sliced array (every other element): ", sliced_array)


# Extracting every other element along rows and columns
sliced_array = array_2d[::2, ::2]  # Every other element along rows and columns
print("Every Other Element of 2D Array:\n", sliced_array)

# Create a 3D array
array_3d = np.random.randint(1, 21, (2, 3, 4))
print("3D Array:\n", array_3d)

# Access a specific element
print("Element in 1st Matrix, 2nd Row, 3rd Column:", array_3d[0, 1, 2])

# Access the entire 2nd "matrix"
print("Entire 2nd Matrix:\n", array_3d[1, :, :])

# Extract a subarray
subarray_3d = array_3d[:, :2, :3]  # All matrices, first 2 rows, first 3 columns
print("Subarray (First 2 Rows, First 3 Columns of All Matrices):\n", subarray_3d)

# -------------------------------------------------------------------

