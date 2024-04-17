import numpy as np

## Função para encontrar o vetor X da T(x) = Ax ou Ax = b
solve_x = lambda A,b: np.linalg.solve(A,b)
## Função para encontrar o vetor X de Ax = b, mas com a inversa de A => x = b * A^(-1)
invert_x = lambda A,b: np.dot(np.linalg.inv(A), b)

## Verificar se existe solução única ou não para aquela função linear. 
def solution_verify(A,b):
    ## Verifica se existe UMA solução
    try:
        r = solve_x(A,b)
        return r
    except np.linalg.LinAlgError:
        ## Matriz transformada
        T_x = np.column_stack((A,b))
        ## Matriz resultante
        b_x = 0
        ## Zerando os valores de b e encontrando multiplicadores para zerar todas as linhas
        for key, value in enumerate(b):
            zerador = value/b[key-1]

            b_x = (T_x[key]/zerador - T_x[key-1])
            if np.all(b_x == 0):
                return "Sistema com Infinitas Soluções"
        return "Sistema Impossível"

def mapping_verify(matrix):
    # Verificando se o número de colunas é menor ou igual ao número de colunas
    if matrix.shape[0] > matrix.shape[1]:
        return False
    # Rank é o número de vetores linearmente independentes na matriz
    rank = np.linalg.matrix_rank(matrix)
    #Se o Rank for igual ao número de linhas, então o mapeamento é um-para-um (injetora)
    if rank == matrix.shape[0]:
        return True
    return False

def r_to_r_verify(matrix, R):    
    # Verificando se o número de colunas é igual ao número de linhas
    if matrix.shape[0] != matrix.shape[1]:
        return False
    # Rank é o número de vetores linearmente independentes na matriz
    rank = np.linalg.matrix_rank(matrix)
    # Se o número de vetores LI for igual ao R da transformação da matriz, então é verdadeiro que a matriz Ax = b é de R^n -> R^n
    if rank == R:
        return True
    return False