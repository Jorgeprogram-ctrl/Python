from args import parse_args

def run(texts: list) -> list:
    # Generamos la lista plana de caracteres
    return [char for word in texts for char in word]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    # Llama a la función parse_args para obtener los textos desde la línea de comandos
    texts = parse_args()

    # Llama a la función run con los textos obtenidos y almacena el resultado
    result = run(texts)

    # Imprime el resultado
    print(result)
