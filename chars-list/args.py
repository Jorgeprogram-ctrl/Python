import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Procesar una lista de cadenas.')
    parser.add_argument(
        'texts', 
        nargs='+',  # El + indica que se pueden pasar múltiples argumentos
        help='Lista de cadenas que se procesarán'
    )
    args = parser.parse_args()
    return args.texts
