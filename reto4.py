# Sigamos con matemáticas elementales para no perder la costumbre y retar nuestras habilidades. 
# Escribe un programa donde apliques las diferentes fórmulas matemáticas para calcular el volumen de un cilindro.
# Recuerda que la base del cilindro es un círculo y necesitarás calcular su área. 
# Aplica las fórmulas en tu programa recibiendo datos como altura y radio.

# **Bonus: agrega otras figuras geométricas a tu programa y que el usuario pueda escoger cuál calcular.**
# Fórmulas de un cilindro:
# Área base = pi * radio²
# Volumen = área base *altura

# A un cono aplicamos las siguientes fórmulas:
# Base = pi * Radio^2
# Volumen = 1/3 * base * altura

# A prismas se aplican las siguientes fórmulas:
# Volumen = base * altura

def calculadora(opcion, altura, radio):
    PI = 3.1416
    if opcion ==  1:
        volumen = round((PI * radio**2 * altura),4)
    else:
        volumen = round((((PI * radio**2)/3) * altura),4)
    volumen = str(volumen)
    return volumen


def run():
    i = 0
    FIGURAS = [" ", "Cilindro", "Cono"]
    print("Bienvenid@ a esta calculadora de volumenes")
    while i == 0:
        menu = """
            
        1 - Cilindro
        2 - Cono
                    
        Elige una opción: """
        opcion = int(input(menu))
        if 0 < opcion <= 2:
            altura = float(input("Digita la altura de tu figura: "))
            radio = float(input("Digita el radio de tu figura: "))
            print("El volumen del " + FIGURAS[opcion] + " es: " + calculadora(opcion, altura, radio))
            break
        else:
            print("Digite una opción correcta")
            continue

if __name__ == '__main__':
    run()