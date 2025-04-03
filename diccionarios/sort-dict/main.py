def run(unsorted_items: dict) -> list[tuple]:
    # Ordenar por los valores de las tuplas (segundo elemento) de manera ascendente
    sorted_items = sorted(unsorted_items.items(), key=lambda x: x[1])  # orden lexicográfico de valores
    print(sorted_items)
    return sorted_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
