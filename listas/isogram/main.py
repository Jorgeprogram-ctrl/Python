def run(text: str) -> bool:
    text = text.lower().replace("-", "")
    letrasVistas = set()  

    for letra in text: 
        if letra in letrasVistas:
            return False
        letrasVistas.add(letra)

    return True  


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    test_words = ["Loco", "hola", "six-year-old", "banana", "isogram", "loco"]
    for word in test_words:
        print(f"{word}: {run(word)}")

    import vendor
    vendor.launch(run)
    
