def devolver_cambio(pagado: float, precio: float, disponibles: dict) -> dict:
    cambio = round(pagado - precio, 2)

    if cambio == 0:
        return {}

    if cambio < 0:
        return None

    disponibles = sorted(disponibles.items(), reverse=True, key=lambda x: x[0])

    resultado = {}

    for valor, cantidad_disponible in disponibles:
        cantidad_a_dar = min(int(cambio // valor), cantidad_disponible)

        if cantidad_a_dar > 0:
            resultado[valor] = cantidad_a_dar
            cambio -= valor * cantidad_a_dar
            cambio = round(cambio, 2)

        if cambio == 0:
            break

    if cambio > 0:
        return None
    print(resultado)
    return resultado


# Definir la función 'run' que es llamada por vendor
def run(pagado: float, precio: float, disponibles: dict) -> dict:
    return devolver_cambio(pagado, precio, disponibles)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
