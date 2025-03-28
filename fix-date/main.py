# main.py
from args import input_date, base_year  # Importa las variables de args.py

def run(input_date: str, base_year: int) -> str:
    # Dividir la fecha de entrada en sus componentes
    month, day, year = input_date.split("/")
    
    # Convertir el año de dos dígitos a cuatro dígitos, sumando el año base
    year = base_year + int(year)
    
    # Formatear la salida como día-mes-año
    output_date = f"{int(day):02d}-{int(month):02d}-{year}"
    
    return output_date


# Llamada a la función con los parámetros importados de args.py
if __name__ == '__main__':
    result = run(input_date, base_year)  # Usa las variables de args.py
    print(result)  # Imprime el resultado
