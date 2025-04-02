def run(nums: list, v: int) -> list:
    # Primera sublista: los valores menores que v
    less_than_v = [num for num in nums if num < v]
    
    # Segunda sublista: los valores mayores o iguales a v
    greater_than_or_equal_v = [num for num in nums if num >= v]
    
    # Retornar ambas sublistas dentro de una lista
    print([less_than_v, greater_than_or_equal_v])
    return [less_than_v, greater_than_or_equal_v]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
