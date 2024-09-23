def multiplicar_matrices(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def matriz_potencia(mat, exp):
    n = len(mat)
    if exp == 0:
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    elif exp == 1:
        return mat
    
    half_pow = matriz_potencia(mat, exp // 2)
    
    if exp % 2 == 0:
        return multiplicar_matrices(half_pow, half_pow)
    else:
        return multiplicar_matrices(multiplicar_matrices(half_pow, half_pow), mat)

if __name__ == "__main__":
    matriz = [
        [1, 2],
        [3, 4]
    ]
    
    exponente = 3
    resultado = matriz_potencia(matriz, exponente)

    print(f"Matriz elevada a la potencia {exponente}:")
    for fila in resultado:
        print(fila)