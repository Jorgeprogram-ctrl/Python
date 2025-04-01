def run(ids: list) -> int:
    # Ordenar la lista de identificadores
    ids.sort()
    
    # Empezamos a buscar el primer identificador sin usar
    expected_id = 1
    for id in ids:
        if id == expected_id:
            expected_id += 1  # Si encontramos el id esperado, incrementamos el siguiente id esperado
    print(expected_id)
    # Al finalizar, `expected_id` es el primer identificador sin usar
    return expected_id


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
