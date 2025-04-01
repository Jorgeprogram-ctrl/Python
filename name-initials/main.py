def run(name: str) -> str:
    # Separar apellido y nombre
    last_name, first_name = name.split(', ')
    
    # Obtener las iniciales del nombre (solo la primera parte)
    name_initial = first_name[0].upper()
    
    # Obtener las iniciales del apellido (todas las partes del apellido)
    last_name_parts = last_name.split()
    last_name_initials = ''.join([part[0].upper() for part in last_name_parts])
    
    # Formar el resultado con las iniciales
    result = f"{name_initial}.{last_name_initials}."
    print(result)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
