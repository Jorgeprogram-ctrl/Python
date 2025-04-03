def run(items: dict) -> bool:
    todos_iguales = len(set(items.values())) == 1
    print(todos_iguales)
    return todos_iguales

if __name__ == "__main__":
    test_items = {"a": 1, "b": 1, "c": 1, "d": 1}
    run(test_items)  # Prueba sin usar vendor
