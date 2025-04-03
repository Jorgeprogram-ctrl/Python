def extraer_claves(diccionario: dict, claves: tuple) -> dict:
    # Retorna las claves que existen en el diccionario
    return {clave: diccionario[clave] for clave in claves if clave in diccionario}

def run(unsorted_items: tuple) -> dict:
    # Extrae el diccionario y las claves desde la tupla
    diccionario = unsorted_items[0]
    claves = unsorted_items[1]
    
    # Llamamos a la función y devolvemos el resultado
    resultado = extraer_claves(diccionario, claves)
    
    # Imprimir el resultado para ver la salida
    print(resultado)
    
    return resultado

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
