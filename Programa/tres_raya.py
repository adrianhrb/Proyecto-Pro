jugador1 = input("Nombre del juagdor 1 (usará círculo): ")
jugador2 = input("Nombre del jugador 2 (usará cruz): ")
figura_jugador1 = "⭕"
figura_jugador2 = "❌"
espacio_blanco = "⬛"
# Establecemos una condición para cambiar turnos de jugadores
player_flow = True
# Definimos un contador que recogerá cada movimiento
moves_count = 0
# Definimos los movimientos límite o máximos
moves_limit = 9
tablero = [["⬛", "⬛", "⬛"], ["⬛", "⬛", "⬛"], ["⬛", "⬛", "⬛"]]
fila1 = tablero[0]
fila2 = tablero[1]
fila3 = tablero[2]
# Definimos una variable para cuando la casilla está "ocupada"
occupied_square = "Casilla ocupada, vuelve a intentarlo"
# Definimos una variable para cuando la casilla NO está "ocupada"
avaiable_square = "Turno del oponente"
# Definimos una variable para valores fuera de rango
out_of_range = "Los valores no están dentro del rango correcto, introduce otros"


while moves_count < moves_limit:
    # Condiciones de victoria
    # Filas
    for fi in range(3):
        for co in range(3):
            if tablero[fi][co] == figura_jugador1 or figura_jugador2:
                print("Felicidades, ganaste")
                break
    # Columnas
    for fi in range(3):
        for co in range(3):
            if tablero[co][fi] == figura_jugador1 or figura_jugador2:
                print("Felicidades, ganaste")
                break
    # Diagonales
    for posi in range(3):
        if tablero[posi][posi] == figura_jugador1 or figura_jugador2:
            print("Felicidades, ganaste")
            break
    if player_flow == True:
        print(
            "Le toca a",
            jugador1,
            "⭕, selecciona una fila (0, 1 o 2) y una columna(0, 1, o 2)",
        )
        fila = int(input("Fila de colocación: "))
        columna = int(input("Columna: "))
        if tablero[fila][columna] == espacio_blanco:
            tablero[fila][columna] = figura_jugador1
            result = avaiable_square
            moves_count += 1
            player_flow = not player_flow
        else:
            result = occupied_square
        print(fila1, fila2, fila3, sep="\n")
        print(result)

    elif player_flow == False:
        print(
            "Le toca a",
            jugador2,
            "❌, selecciona una fila (1,2 o 3) y una columna(1, 2, o 3)",
        )
        fila = int(input("Fila de colocación: "))
        columna = int(input("Columna: "))
        if tablero[fila][columna] == espacio_blanco:
            tablero[fila][columna] = figura_jugador2
            result = avaiable_square
            moves_count += 1
            player_flow = not player_flow
        else:
            result = occupied_square
        print(fila1, fila2, fila3, sep="\n")
        print(result)
