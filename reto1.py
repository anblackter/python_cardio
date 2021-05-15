def area_triangulo():
    base = float(input("Digita la base del triángulo: "))
    altura = float(input("Digita la altura del triángulo: "))
    area = (base * altura)/2
    area = round(area, 2)
    print("El área del triángulo es: " + str(area))


def tipo_triangulo():
    a = float(input("Digita la medida del lado a: "))
    b = float(input("Digita la medida del lado b: "))
    c = float(input("Digita la medida del lado c: "))
    if a == b and a == c:
        tipo = "Equilatero"
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a): 
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    print("El triangulo es: " + tipo)


def run():
    menu = """
    Bienvenido a operaciones con triangulos 

    1 - Calcular el área de un tríangulo
    2 - Comprobar el tipo de triángulo

    Elige una opción: """

    opcion = int(input(menu))

    if opcion == 1:
        area_triangulo()
    elif opcion == 2:
        tipo_triangulo()
    else:
        print('Ingresa una opción correcta por favor')


if __name__ == '__main__':
    run()