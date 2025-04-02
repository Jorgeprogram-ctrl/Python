def run(points: list) -> list:
    # Desempaquetamos las coordenadas de los puntos A, B y C
    xA, yA = points[0]
    xB, yB = points[1]
    xC, yC = points[2]
    
    # Calculamos el baricentro usando las fórmulas proporcionadas
    xP = (xA + xB + xC) / 3
    yP = (yA + yB + yC) / 3
    
    # Redondeamos a 4 decimales
    baricentro = [round(xP, 4), round(yP, 4)]
    print(baricentro)
    return baricentro


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
