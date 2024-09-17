import numpy as np

#Assignment Manipulating 2D array of shape (5,5) filled with random int between 50 t 100, replace the central 3x3 subarray with zeros

a = np.random.randint(50,100,size=(5,5))
print(a)
# b=np.zeros(3)
# print(b)
a[1:4,1:4]=0
print(a)

# ---------------------------------------------------------------

#Assignmet 7 Transposition and mean calculation
a = np.random.randint(10,100, size=(5,3))
print(a)
aTransposed = a.T
print(aTransposed)
print(a.mean())
print(aTransposed.mean())

# ---------------------------------------------------------------

# Square root calculation

a = np.arange(1,17)
print(a)
b = np.sqrt(a)
print(b)
np.savetxt('square_root_result.csv',b,delimiter=',')

# ---------------------------------------------------------------

# Assignment 10 Matrix multiplication and transpose

matrix1 = np.array([[1,2],[3,4],[5,6],[7,8]])
matrix2 = np.array([[3,4,2],[7,5,2]])
print(matrix1)
print(matrix2)

multi_matrix = np.matmul(matrix1,matrix2)
print(multi_matrix)
print(multi_matrix.T)

# ---------------------------------------------------------------

