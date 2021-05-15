def jugar_ppt(jugada_a, jugada_b):
    if jugada_a == jugada_b:
        ganador = "No hay un gandor porque hay Empate"
    elif (jugada_a == "Piedra" and jugada_b == "Tijera"):
        ganador = "Jugador 1"
    elif jugada_a == "Papel" and jugada_b == "Piedra":
        ganador = "Jugador 1"
    elif jugada_a == "Tijera" and jugada_b == "Papel":
        ganador = "Jugador 1"
    else:
        ganador = "Jugador 2"
    return ganador


def run():
    print("Bienvenid@, vamos a jugar Piedra, Papel o Tijera" )
    i = 1
    jugada = [" ","Piedra", "Papel", "Tijera"]
    while i < 3:
        print("Es turno del jugador " + str(i))
        menu = """
        
        1 - Piedra
        2 - Papel
        3 - Tijera

        Elige una opción: """
        opcion = int(input(menu))
        
        if 0 < opcion <= 3:
            if i == 1:
                jugada_a = jugada[opcion]
                i += 1
            elif i == 2:
                jugada_b = jugada[opcion]
                i += 1
        else:
            print("Selecciona una opción correcta")
    print("El ganador es: " + jugar_ppt(jugada_a, jugada_b))

if __name__ == '__main__':
    run()