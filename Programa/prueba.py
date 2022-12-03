jugador1 = input("Nombre del juagdor 1 (usará ⭕): ")
jugador2 = input("Nombre del jugador 2 (usará cruz ❌): ")
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
out_of_range = (
    "Los valores no están dentro del rango correcto, introduce otros que sean correctos"
)
victory = "Felicidads, has ganado"
# Variables que irá tomando valores dentro del bucle
result = None
figura = None

while moves_count < moves_limit:
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] != espacio_blanco:
            result = victory
            figura = tablero[fila][0]
    for columna in range(3):
        if (
            tablero[0][columna]
            == tablero[1][columna]
            == tablero[2][columna]
            != espacio_blanco
        ):
            result = victory
            figura = tablero[0][columna]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != espacio_blanco:
        result = victory
        ficha = tablero[0][0]
        break
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] != espacio_blanco:
        result = victory
        ficha = tablero[0][0]
        break
    elif player_flow == True:
        if result == victory:
            break
        else:
            print(
                "Le toca a",
                jugador1,
                "⭕, selecciona una fila (1,2 o 3) y una columna(1, 2, o 3)",
            )
            fila = int(input("Fila de colocación: "))
            columna = int(input("Columna: "))
            if fila > 3 or columna > 3:
                result = out_of_range
            # Restamos uno al tamaño del tablero ya que empezamos en 0
            elif tablero[fila - 1][columna - 1] == espacio_blanco:
                tablero[fila - 1][columna - 1] = figura_jugador1
                result = avaiable_square
                moves_count += 1
                player_flow = not player_flow
            else:
                result = occupied_square
            print(fila1, fila2, fila3, sep="\n")
            print(result)

    elif player_flow == False:
        if result == victory:
            print(result)
            break
        else:
            print(
                "Le toca a",
                jugador2,
                "❌, selecciona una fila (1,2 o 3) y una columna(1, 2, o 3)",
            )
            fila = int(input("Fila de colocación: "))
            columna = int(input("Columna: "))
            if fila > 3 or columna > 3:
                result = out_of_range
            elif tablero[fila - 1][columna - 1] == espacio_blanco:
                tablero[fila - 1][columna - 1] = figura_jugador2
                result = avaiable_square
                moves_count += 1
                player_flow = not player_flow
            else:
                result = occupied_square
            print(fila1, fila2, fila3, sep="\n")
            print(result)
