jugador1 = input("Nombre del juagdor 1 (usará ⭕): ")
jugador2 = input("Nombre del jugador 2 (usará cruz ❌): ")
figura_jugador1 = "⭕"
figura_jugador2 = "❌"
# Establecemos una condición para cambiar turnos de jugadores
player_flow = True
# Definimos un contador que recogerá cada movimiento
moves_count = 0
# Definimos los movimientos límite o máximos
moves_limit = 9
tablero = [["⬛", "⬛", "⬛"], ["⬛", "⬛", "⬛"], ["⬛", "⬛", "⬛"]]
# Definimos una variable para cuando la casilla está "ocupada"
occupied_square = "Casilla ocupada, vuelve a intentarlo"
# Definimos una variable para cuando la casilla NO está "ocupada"
avaiable_square = "Turno del oponente"
# Definimos una variable para valores fuera de rango
out_of_range = "Los valores no están dentro del rango correcto, introduce otros que sean correctos"
# Variables que irá tomando valores dentro del bucle
error_message = ""
jugando = True
victory = ""
while jugando:
    for fila in tablero:
        for columna in fila:
            print(columna, end=" ")
        print()
    if player_flow:
        print("Le toca a",jugador1,"⭕, selecciona una fila (1,2 o 3) y una columna(1, 2, o 3)")
        fila = int(input("Fila de colocación: "))
        columna = int(input("Columna: "))
        # Restamos uno al tamaño del tablero ya que empezamos en 0
        if 1 <= fila <= 3 and 1 <= columna <= 3 and tablero[fila - 1][columna - 1] == "⬛":
            tablero[fila - 1][columna - 1] = figura_jugador1
            moves_count += 1
            player_flow = not player_flow
        else:
            if 1 > fila or fila > 3 or 1 > columna or columna > 3:
                error_message = out_of_range
            elif tablero[fila - 1][columna - 1] != "⬛":
                error_message = occupied_square
            print(error_message)
    else:
        print("Le toca a",jugador2,"❌, selecciona una fila (1,2 o 3) y una columna(1, 2, o 3)")
        fila = int(input("Fila de colocación: "))
        columna = int(input("Columna: "))
        if 1 <= fila <= 3 and 1 <= columna <= 3 and tablero[fila - 1][columna - 1] == "⬛":
            tablero[fila - 1][columna - 1] = figura_jugador2
            moves_count += 1
            player_flow = not player_flow
        else:
            if 1 > fila or fila > 3 or 1 > columna or columna > 3:
                error_message = out_of_range
            elif tablero[fila - 1][columna - 1] != "⬛":
                error_message = occupied_square
            print(error_message)

#Definimos las condiciones de victoria
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] != "⬛":
            victory = f'¡¡Ha ganado el jugador con {tablero[fila][0]}!!'
            jugando = not jugando
            break
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] != "⬛":
            victory = f'¡¡Ha ganado el jugador con {tablero[0][columna]}!!'
            jugando = not jugando
            break
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "⬛":
        victory = f'¡¡Ha ganado el jugador con {tablero[0][0]}!!'
        jugando = not jugando
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] != "⬛":
        victory = f'¡¡Ha ganado el jugador con {tablero[0][2]}!!'
        jugando = not jugando
    else:
        if moves_count == moves_limit:
            victory = "La partida ha quedado en empate"
            jugando = not jugando

for fila in tablero:
    for columna in fila:
        print(columna, end=" ")
    print()
print(victory)