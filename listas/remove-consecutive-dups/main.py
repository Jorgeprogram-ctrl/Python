def run(items: list) -> list:
    # Lista para almacenar los elementos sin duplicados consecutivos
    result = []
    
    # Recorremos los elementos de la lista
    for item in items:
        # Si la lista está vacía o el último elemento agregado es diferente al actual
        if not result or result[-1] != item:
            result.append(item)
    
    print(result)

    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
