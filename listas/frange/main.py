def frange(start, stop, step):
    result = []
    current = start
    while current < stop:
        result.append(round(current, 4))  # Redondeamos a 4 decimales para mantener la precisión
        current += step
    print(result)    
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(frange)
