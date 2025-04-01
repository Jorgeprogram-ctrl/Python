from args import Args

def run(u: list, v: list) -> float | None:
    # Comprobamos si los vectores tienen la misma longitud
    if len(u) != len(v):
        return None  # Si no tienen la misma longitud, devolvemos None
    
    # Calculamos el producto escalar usando zip
    dprod = sum(a * b for a, b in zip(u, v))
    
    return dprod


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    # Instanciamos la clase Args para parsear los argumentos
    args = Args()
    u, v = args.parse()  # Obtenemos los vectores u y v
    
    # Llamamos a la función run pasando los vectores u y v
    resultado = run(u, v)
    
    if resultado is None:
        print("Los vectores no tienen la misma longitud, no se puede calcular el producto escalar.")
    else:
        print(f"El producto escalar de los vectores u y v es: {resultado}")
