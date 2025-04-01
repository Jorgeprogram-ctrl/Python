def run(matrix: list) -> int:
    # Verificar si la matriz es cuadrada
    if len(matrix) != len(matrix[0]):
        return None
    
    # Calcular la suma de la diagonal principal
    diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
    
    print(diagonal_sum)

    return diagonal_sum


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
