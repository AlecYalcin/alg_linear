import numpy as np
from func import r_to_r_verify, solution_verify
from scipy.linalg import null_space

A = np.array([
    [4,-7,3,7,5],
    [6,-8,5,12,-8],
    [-7,10,-8,-9,14],
    [3,-5,4,2,-6],
    [-5,6,-6,-7,3],
])

# Verificando se a matrix A pertence a R^5
answer = r_to_r_verify(A, 5)
print("É sobrejetora: ", answer)

A = np.array([
    [9,43,5,6,-1],
    [14,15,-7,-5,4],
    [-8,-6,12,-5,-9],
    [-5,-6,-4,9,8],
    [13,14,15,3,11],
])

# Verificando se a matrix A pertence a R^5
answer = r_to_r_verify(A, 5)
print("É sobrejetora: ", answer)
