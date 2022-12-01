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
# Establecemos condiciones de victoria
win1 = tablero[0][0] == tablero[0][1] == tablero[0][2]
win2 = tablero[1][0] == tablero[1][1] == tablero[1][2]
win3 = tablero[2][0] == tablero[2][1] == tablero[2][2]
win4 = tablero[0][0] == tablero[1][0] == tablero[2][0]
win5 = tablero[0][1] == tablero[1][1] == tablero[2][1]
win6 = tablero[0][2] == tablero[1][2] == tablero[2][2]
win7 = tablero[0][0] == tablero[1][1] == tablero[2][2]
win8 = tablero[0][2] == tablero[1][1] == tablero[2][0]
win_condition_circle = (
    all([win1, win2, win3, win4, win5, win6, win7, win8]) == figura_jugador1
)
win_condition_x = (
    all([win1, win2, win3, win4, win5, win6, win7, win8]) == figura_jugador2
)
victory = "Congratulations! You win the game"
draw = "The game is tied"

while moves_count < moves_limit:
    if player_flow == True:
        print(
            "Le toca a",
            jugador1,
            "⭕, selecciona una fila (0,1 o 2) y una columna(0, 1, o 2)",
        )
        fila = int(input("Fila de colocación: "))
        columna = int(input("Columna: "))
        # Restamos uno al tamaño del tablero ya que empezamos en 0
        if tablero[fila][columna] == espacio_blanco:
            tablero[fila][columna] = figura_jugador1
            result = avaiable_square
            moves_count += 1
            player_flow = not player_flow
        else:
            result = occupied_square
        if win_condition_circle:
            print(victory)
            break
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
        if win_condition_x:
            print(victory)
            break
        print(fila1, fila2, fila3, sep="\n")
        print(result)
