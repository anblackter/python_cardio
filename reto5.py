# Para este reto final juguemos con números. En tu programa pide al usuario ingresar 3 números: un límite inferior, un límite superior y uno de comparación.
# Si tu número de comparación se encuentra en el rango de los dos límites, imprímelo en pantalla.
# En caso de estar por debajo del inferior o arriba del superior, también muéstralo en pantalla y pide ingresar otro número para repetir el proceso.

def jugar(a, b, c):
    i = 0
    while i == 0:
        if a < c < b:
            print("Tú mejor número es: " + str(c))
            break
        elif c < a or c > b:
            print("Tú número es: " + str(c))
            c = int(input("Digita otro número: "))
            


def run():
    print("Bienvenid@, piensa en 3 números, al menos uno que sea menor al que escogas como mayor y el último que sea de tu elección: ")
    a = int(input("Digita el menor: " ))
    b = int(input("Digita el mayor: " ))
    c = int(input("Digita tu último número: " ))
    jugar(a, b, c)

if __name__ == '__main__':
    run()