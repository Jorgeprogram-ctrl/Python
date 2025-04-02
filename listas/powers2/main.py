def run(n: int) -> list:
    # Generar la lista de potencias de 2 desde 2^0 hasta 2^n
    powers_of_two = [2**i for i in range(n + 1)]
    print(powers_of_two)
    return powers_of_two


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
