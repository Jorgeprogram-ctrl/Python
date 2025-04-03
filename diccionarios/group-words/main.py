def run(words: list) -> dict:
    palabras_agrupadas = {}
    for word in words:
        primera_letra = word[0].lower()
        if primera_letra not in palabras_agrupadas:
            palabras_agrupadas[primera_letra] = []
        palabras_agrupadas[primera_letra].append(word)
    print(palabras_agrupadas)
    return palabras_agrupadas        


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
