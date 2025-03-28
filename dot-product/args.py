import argparse

class Args:
    def __init__(self):
        # Configuración de los argumentos
        self.parser = argparse.ArgumentParser(description="Calcular el producto escalar de dos vectores.")
        self.parser.add_argument(
            '--vector_u', type=int, nargs='+', required=True, 
            help="El primer vector u (como una lista de números separados por espacio)."
        )
        self.parser.add_argument(
            '--vector_v', type=int, nargs='+', required=True, 
            help="El segundo vector v (como una lista de números separados por espacio)."
        )

    def parse(self):
        # Parsear los argumentos
        args = self.parser.parse_args()
        return args.vector_u, args.vector_v
