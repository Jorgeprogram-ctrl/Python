def run(x: int, n: int) -> list:
    # Usamos lista por comprensión para generar los primeros n múltiplos de x
    multiples = [x * i for i in range(1, n + 1)]
    print(multiples)
    return multiples


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
