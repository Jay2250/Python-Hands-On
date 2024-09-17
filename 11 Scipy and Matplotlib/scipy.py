from scipy.linalg import inv
from scipy.interpolate import interp1d
import numpy as np
from scipy.linalg import inv, det
from scipy.integrate import quad
from scipy.optimize import minimize

# objective function


def objective_function(x):
    return x**2 + 3*x + 2


# perform optimization
result = minimize(objective_function, x0=0)
print(result.x)  # optimal value of x

# -------------------------------------------------------------------

# define the integrand


def integrand(x):
    return x**2
# compute the integral -(curve of x2)
result, error = quad(integrand,0,1)
print(result)  # integral result

# -------------------------------------------------------------------


# define a matrix
matrix = np.array([[1, 2], [3, 4]])

# compute the determinant of the matrix
matrix_det = det(matrix)
print(matrix_det)

# compute the inverse of the matrix
matrix_inv = inv(matrix)
print(matrix_inv)

# --------------------------------------------------------------------


# konwing data points
x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 4, 9])

# create a interpolate function
f = interp1d(x, y, kind='linear')

# interpolate a new value
new_x = 2.5
interpolated_value = f(new_x)
print(interpolated_value)  # interpolated value

# --------------------------------------------------------

# Assignment 1 finding the inverse of matrix


matrix = np.array([[4, 7], [2, 6]])
print(matrix)
matrix_inv = inv(matrix)
print(matrix_inv)
