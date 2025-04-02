def run(text: str) -> list:
    # Usamos una lista por comprensión para generar las palabras junto a su longitud
    words_with_length = [f"{word}:{len(word)}" for word in text.split()]
    print(words_with_length)
    return words_with_length


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
