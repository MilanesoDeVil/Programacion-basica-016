def multiplicar_matrices(A, B):
    n = len(A)
    
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    A11 = [fila[:mid] for fila in A[:mid]]
    A12 = [fila[mid:] for fila in A[:mid]]
    A21 = [fila[:mid] for fila in A[mid:]]
    A22 = [fila[mid:] for fila in A[mid:]]

    B11 = [fila[:mid] for fila in B[:mid]]
    B12 = [fila[mid:] for fila in B[:mid]]
    B21 = [fila[:mid] for fila in B[mid:]]
    B22 = [fila[mid:] for fila in B[mid:]]

    C11 = sumar_matrices(multiplicar_matrices(A11, B11), multiplicar_matrices(A12, B21))
    C12 = sumar_matrices(multiplicar_matrices(A11, B12), multiplicar_matrices(A12, B22))
    C21 = sumar_matrices(multiplicar_matrices(A21, B11), multiplicar_matrices(A22, B21))
    C22 = sumar_matrices(multiplicar_matrices(A21, B12), multiplicar_matrices(A22, B22))

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C

def sumar_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

if __name__ == "__main__":
    A = [
        [1, 2],
        [3, 4]
    ]

    B = [
        [5, 6],
        [7, 8]
    ]

    resultado = multiplicar_matrices(A, B)

    print("Resultado de la multiplicación de matrices:")
    for fila in resultado:
        print(fila)