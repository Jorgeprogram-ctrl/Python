def run(formula: list) -> bool:
    # Verificar las reglas una por una
    
    # Regla 1: El componente 1 y el componente 2 no se pueden seleccionar al mismo tiempo.
    if 1 in formula and 2 in formula:
        return False
    
    # Regla 2: El componente 3 y el componente 4 no se pueden seleccionar al mismo tiempo.
    if 3 in formula and 4 in formula:
        return False
    
    # Regla 3: El componente 5 y el componente 6 tienen que seleccionarse al mismo tiempo.
    if 5 in formula and 6 not in formula:
        return False
    if 6 in formula and 5 not in formula:
        return False
    
    # Regla 4: El componente 7 o el componente 8 tienen que seleccionarse.
    if 7 not in formula and 8 not in formula:
        return False
    
    # Si todas las reglas se cumplen, la fórmula es válida.
    print("Formula completada")
    return True


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
