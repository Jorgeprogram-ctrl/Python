def run(items: list) -> list:
    # Lista por comprensión que aplana la lista
    flatten_items = [elem for sublist in items for elem in (sublist if isinstance(sublist, list) else [sublist])]
    
    # Imprimir el resultado a la consola
    print(flatten_items)
    
    return flatten_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
