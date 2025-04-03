def run(stock: dict, articulo: str, cantidad: int) -> bool:
    print(stock.get(articulo, 0) >= cantidad)
    return stock.get(articulo, 0) >= cantidad


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
