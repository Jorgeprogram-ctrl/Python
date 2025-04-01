def run(items: list) -> int:
    # Sumamos todos los elementos, convirtiendo los str a int si es necesario
    total_sum = sum(int(item) for item in items)
    print(total_sum)
    return total_sum


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
