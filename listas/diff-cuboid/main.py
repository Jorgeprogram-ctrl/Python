def run(c1: tuple, c2: tuple) -> int:
    # Calculamos el volumen de cada cuboide
    v1 = c1[0] * c1[1] * c1[2]
    v2 = c2[0] * c2[1] * c2[2]
    
    print(abs(v1-v2))
    return abs(v1 - v2)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)