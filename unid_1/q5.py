import numpy as np
from func import mapping_verify
from scipy.linalg import null_space

A = np.array([
    [-5,6,-5,-6],
    [-8,3,-3,8],
    [2,9,5,-12],
    [-3,2,7,-12]
])

mapeavel = mapping_verify(A)
print("É Injetora:", mapeavel)

A = np.array([
    [7,5,9,-9],
    [5,6,4,-4],
    [4,8,0,7],
    [-6,-6,6,5]
])

mapeavel = mapping_verify(A)
print("É Injetora:", mapeavel)