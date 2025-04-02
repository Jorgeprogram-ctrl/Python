from functools import reduce

def run(values: list, operator: str) -> bool:
    # Se aplica el operador lógico entre todos los valores de la lista
    if operator == 'and':
        print(reduce(lambda x, y: x and y, values))
        return reduce(lambda x, y: x and y, values)
    elif operator == 'or':
        print(lambda x, y: x or y, values)
        return reduce(lambda x, y: x or y, values)
    else:
        return False  # Si el operador no es válido (aunque el problema asegura que solo serán 'and' y 'or')

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
