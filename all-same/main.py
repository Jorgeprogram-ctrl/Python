def run(items: list) -> bool:
    # Verificar si todos los elementos son iguales al primero
    all_same = all(item == items[0] for item in items)
   
    print(all_same)

    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
