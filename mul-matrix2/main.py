def multiplicar_matrices(A, B):
    # Inicializar la matriz resultado 2x2 con ceros
    resultado = [[0, 0], [0, 0]]

    # Multiplicación de matrices
    for i in range(2):  # Filas de A
        for j in range(2):  # Columnas de B
            resultado[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j]

    return resultado

# Ejemplo de matrices 2x2
A = [[6, 4], [8, 9]]
B = [[3, 2], [1, 7]]

# Multiplicación
resultado = multiplicar_matrices(A, B)

# Imprimir resultado
for fila in resultado:
    print(fila)
