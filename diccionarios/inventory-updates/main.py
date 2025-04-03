def run(movimientos: str) -> dict:
    inventario = {}

    for movimiento in movimientos.split(","):
        articulo = movimiento[0]  # Extrae la clave (artículo)
        cantidad = int(movimiento[1:])  # Convierte el número a entero

        inventario[articulo] = inventario.get(articulo, 0) + cantidad  # Actualiza el inventario
    
    return inventario  # Devuelve el diccionario completo

# Este bloque es para pruebas, fuera de vendor.launch
if __name__ == '__main__':
    # Aquí solo estamos llamando la función directamente
    print(run("A1,B4,A-2,A7,B1,C4"))
