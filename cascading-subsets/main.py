def run(values: list, n: int) -> list:
    # Generar los subconjuntos en cascada utilizando listas por comprensión
    subsets = [tuple(values[i:i + n]) for i in range(len(values) - n + 1)]
    print(subsets)
    return subsets


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
