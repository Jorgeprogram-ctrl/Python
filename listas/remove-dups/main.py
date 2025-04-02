def run(nums_dups: list) -> list:
    # Lista vacía para almacenar los valores únicos
    nums_unique = []
    
    # Usamos una lista por comprensión para agregar solo los valores que no estén duplicados
    [nums_unique.append(x) for x in nums_dups if x not in nums_unique]
    
    # Imprimir el resultado para ver qué se devuelve
    print(nums_unique)  # Esto imprimirá el resultado en la consola
    
    return nums_unique


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
