def run(text: str) -> str:
    # Dividir la cadena en una lista de números
    numbers = text.split(',')
    
    # Eliminar el primer y el último número
    numbers = numbers[1:-1]
    
    # Unir los números restantes con un espacio
    result = ' '.join(numbers)
    print(result)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
