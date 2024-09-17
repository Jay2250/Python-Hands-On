import numpy as np

#1D Array
OneD_array = np.array([1,2,3,4])
print("One D Array : ",OneD_array)

#2D Array
twoD_Array = np.array([[1,2],[3,4]])
print("2D array : ",twoD_Array)

#3D Array
threeD_array = np.array([[1,2,3],[4,5,6],[7,8,9],[4,3,2]])
print("3D array : ",threeD_array)

# array of Zeros
zero_Array = np.zeros((3,4))  # (rows, columns)
print("Zero Array : ",zero_Array)

#array of ones
ones_array = np.ones((2,3))
print("Ones array : ", ones_array)

#2X2 array filled with the value 7
full_array = np.full((2,2),7)
print("Array filled with 7 : ", full_array)

# array with value from 0 to 9
range_array =  np.arange(0,10)
print("Array with range : \n ",range_array)

#array with specific step size
step_array = np.arange(0,10,2)
print("Array with step Size: \n", step_array)

#Array with linearly spaced values
linspace_array = np.linspace(0,1, 10 )  # 5 value from 0 to 1
print("Array with linear spaced value :\n ", linspace_array)

#2X2 with random integer between 1 and 10
random_int_array = np.random.randint(1, 10, size=(2,2))
print("Array with random Integers : \n ", random_int_array)

# 3X3 identity matrix
identity_matrix = np.eye(3)
print("Identity matrix : \n ", identity_matrix)

#diagonal matrix with specified diagonal values
diag_matrix = np.diag([1,2,3])
print("Diagonal Matrix : \n ", diag_matrix)

#reshaping array to 2X3
array = np.array([1,2,3,4,5,6])
reshaped_array = array.reshape((2,3))
print("Reshaped array : ", reshaped_array)

#empty 1D array of size 5
empty_id = np.empty(5)
print("1D empty array : ", empty_id)

#2X3 empty array
empty_2D = np.empty((2,3))
print("2D empty array ",empty_2D)

#3X3X2 empty array
empty_3D = np.empty((3,3,2))
print("3D empty array : \n", empty_3D)

# --------------------------------------------------------------

#Assignment 1 1D array with 20 elements
array = np.arange(0,20)
print(array)
print("reshaped array to 4X5\n",array.reshape(4,5))
array1 = np.random.randint(1, 10, size=(3,3))
print("random array 3X3\n",array1)
print("Transpose of array1 is : \n", np.transpose(array1))

# --------------------------------------------------------------

array_1D = np.array([1,2,3,4])
print(array_1D)
print(array_1D.ndim)
print(array_1D.shape)
print(array_1D.size)
print(array_1D.dtype)

array_2D = np.array([[1,2,3],[4,5,6]])
print(array_2D)
print(array_2D.ndim)
print(array_2D.shape)
print(array_2D.size)
print(array_2D.dtype)

array_3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[3,2,1]]])
print(array_3D)
print(array_3D.ndim)
print(array_3D.shape)
print(array_3D.size)
print(array_3D.dtype)

# --------------------------------------------------------------
#Assignment array dimension and shape

def describe_array(arr):
    print("Dimension of array : ", arr.ndim)
    print("shape of array : ", arr.shape)
    print("size of array : ",arr.size)
    print("type of array : ", arr.dtype)

array = np.array([[1,2,3],[4,5,6]])
describe_array(array)

# --------------------------------------------------------------

import numpy as np
array_Int = np.array([10,2,3,4,5,6])
print("Item Size is : ",array_Int.itemsize)
print("memory of array : ",array_Int.nbytes)

array_float = np.array([1.23,2.321,3.34,4.1,5.2])
print("Item Size is : ",array_float.itemsize)
print("memory of array : ",array_float.nbytes)

# -------------------------------------------------------------

import numpy as np

# 1. Create arrays with different data types: integers, floats, booleans
int_array = np.array([1, 2, 3, 4], dtype=np.int32)
float_array = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32)
bool_array = np.array([True, False, True, False], dtype=np.bool_)

# 2. Compare their itemsize and nbytes to understand memory requirements
print("Integer array:")
print("Item size (bytes):", int_array.itemsize)
print("Total memory (nbytes):", int_array.nbytes)

print("\nFloat array:")
print("Item size (bytes):", float_array.itemsize)
print("Total memory (nbytes):", float_array.nbytes)

print("\nBoolean array:")
print("Item size (bytes):", bool_array.itemsize)
print("Total memory (nbytes):", bool_array.nbytes)

# 3. Change the dtype of an existing array from int to float and verify changes
converted_array = int_array.astype(np.float32)

print("\nConverted integer array to float:")
print("Item size (bytes):", converted_array.itemsize)
print("Total memory (nbytes):", converted_array.nbytes)

# ------------------------------------------------------------------


