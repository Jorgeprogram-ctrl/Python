def run(items: dict) -> dict:
    fitems = {key.replace(" ",""): value for key, value in items.items()}
    print(fitems)
    return fitems


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
