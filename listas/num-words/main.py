def run(text: str) -> int:
    # Cuenta las palabras en el texto
    words = text.split()  # Divide el texto en palabras usando espacios
    num_words = len(words)  # Cuenta el número de palabras
    return num_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    # El texto a analizar
    text = 'All you need is love'

    # Llamar a la función run
    result = run(text)

    # Mostrar el resultado
    print(f"Numero de palabras: {result}")
