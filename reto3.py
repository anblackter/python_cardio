# Imagina que quieres calcular los kilómetros que son cierta cantidad de millas. 
# Para no estar repitiendo este cálculo escribe un programa en que el usuario indique 
# una cantidad de millas y en pantalla se muestre el resultado convertido a kilómetros.
# Toma en cuenta que en cada milla hay 1.609344 Km

# **Bonus: haz que el usuario pueda escoger entre convertir millas a kilómetros o kilómetros a millas.**


def conversor(opcion):
    MILLA = 1.609344
    if opcion == 1:
        millas = float(input("Digita las millas: "))
        kilometros = round((millas / MILLA),2)
        conversion = str(millas) + " millas equivalen a: " + str(kilometros) + " kilómetros"
    else:
        kilometros = float(input("Digita los kilómetros: "))
        millas = round((kilometros * MILLA),2)
        conversion = str(kilometros) + " kilómetros equivalen a: " + str(millas) + " millas"
    return conversion


def run():
    i = 0
    print("Bienvenid@ a este conversor ")
    while i == 0:
        menu = """
            
        1 - De millas a kilómetros
        2 - De kilómetros a millas
            
        Elige una opción: """
        opcion = int(input(menu))
        if 0 < opcion <= 2:
            print(conversor(opcion))
            break
        else:
            print("Digite una opción correcta")
            continue

if __name__ == '__main__':
    run()