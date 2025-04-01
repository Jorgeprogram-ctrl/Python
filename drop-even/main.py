def run(items: list) -> list:
    # Creamos una nueva lista con los elementos en posiciones impares
    result = [items[i] for i in range(1, len(items), 2)]
    print(result)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
