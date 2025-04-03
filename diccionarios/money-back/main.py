def devolver_cambio(pagado: float, precio: float, disponibles: list) -> dict:
    cambio = round(pagado - precio, 2)  # Calculamos el cambio a devolver

    if cambio == 0:  # Si no hay que devolver cambio
        return {}
    
    if cambio < 0:  # Si el pagado es menor que el precio, no podemos devolver el cambio
        return None
    
    disponibles.sort(reverse=True)  # Ordenamos las monedas/billetes de mayor a menor

    resultado = {}  # Inicializamos el diccionario de resultado
    
    for valor in disponibles:
        cantidad = int(cambio // valor)  # Cuántas veces cabe esta moneda/billete en el cambio
        if cantidad > 0:
            resultado[valor] = cantidad
            cambio -= valor * cantidad  # Restamos el valor del cambio

        if cambio == 0:  # Si ya hemos dado el cambio completo, terminamos
            break

    if cambio > 0:  # Si después de usar todas las monedas/billetes no hemos devuelto el cambio, no es posible
        return None
    print(resultado)
    return resultado  # Devolvemos el resultado con las monedas/billetes utilizados


# Definimos la función `run` que usará `devolver_cambio` con los parámetros proporcionados.
def run(pagado: float, precio: float, disponibles: list) -> dict:
    return devolver_cambio(pagado, precio, disponibles)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    vendor.launch(run)
