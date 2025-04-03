def run(items: list) -> dict:
    unpack_items = {sublist[0]: sublist[1:] for sublist in items}
    print(unpack_items)
    return unpack_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
