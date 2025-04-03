def encontar_repetido(lista: list, n: int) -> int:
    contador = {}

    for num in lista:
        if num in contador:
            contador[num] += 1
        else:
            contador[num] = 1

    for num in lista:
        if contador[num] == n:
            print(num)
            return num
    return -1        


def run(unsorted_items: list) -> int:
    # Llamamos a la función encontar_repetido con los datos proporcionados
    lista = unsorted_items[0]  # Lista de números
    n = unsorted_items[1]  # Número de repeticiones que estamos buscando
    return encontar_repetido(lista, n)  # Aquí se ha corregido el nombre de la función

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
