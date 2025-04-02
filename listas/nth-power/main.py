def run(items: list, n: int) -> int:
    # Verificar si n está dentro del rango de la lista
    if n < 0 or n >= len(items):
        return -1
    
    # Obtener el valor en la posición n y elevarlo a la potencia n
    value = items[n] ** n
    print(value)
    return value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
