def valor_maximo(lista):
    # Inicializamos el valor máximo con el primer elemento de la lista
    max_value = lista[0]

    # Recorremos la lista comparando cada elemento
    for num in lista:
        if num > max_value:
            max_value = num

    return max_value

# Ejemplo de lista
valores = [10, 25, 5, 60, 34, 90, 1]

# Llamada a la función para obtener el valor máximo
resultado = valor_maximo(valores)

# Imprimir el resultado
print("El valor máximo es:", resultado)
