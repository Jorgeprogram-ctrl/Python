def run(decimal: int) -> str:
    # Si el número es 0, la representación binaria es '0'
    if decimal == 0:
        return '0'
    
    # Lista para almacenar los restos
    binary_digits = []
    
    # Convertir el número decimal a binario
    while decimal > 0:
        remainder = decimal % 2
        binary_digits.append(str(remainder))  # Guardamos el resto como cadena
        decimal //= 2  # Dividimos el número entre 2
    
    # Los restos están en orden inverso, por lo que los invertimos antes de unirlos
    binary_representation = ''.join(binary_digits[::-1])
    print(binary_representation)
    return binary_representation


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
