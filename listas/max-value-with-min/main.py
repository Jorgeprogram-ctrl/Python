import args  # Importa los valores desde args.py

def run() -> int:
    # Usa los valores de args.py
    values = args.values
    
    # Usamos listas por comprensión para invertir el signo de los elementos
    lista_invertida = [-x for x in values]
    
    # Encontramos el valor mínimo de la lista invertida (lo que corresponde al máximo original)
    max_value = -min(lista_invertida)
    
    # Imprime el valor máximo
    print(f"El valor máximo es: {max_value}")
    
    return max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    # Llama a vendor.launch solo con la función run
    vendor.launch(run)
