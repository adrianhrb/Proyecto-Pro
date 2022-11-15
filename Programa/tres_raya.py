jugador1 = input("Nombre del juagdor 1 (usará círculo): ") 
jugador2 = input("Nombre del jugador 2 (usará cruz): ")
figura_juagdor1 = "⭕"
figura_jugador2 = "❌"
espacio_blanco = "⬛"
player_switch = True #True = Jugador 1, False = Jugador 2
tablero = ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"]
fila1 = f'{tablero[0]} | {tablero[1]} | {tablero[2]}'
fila2 = f'{tablero[3]} | {tablero[4]} | {tablero[5]}'
fila3 = f'{tablero[6]} | {tablero[7]} | {tablero[8]}'

#Pedimos posiciones por filas y columnas
while True:
    if player_switch == True:
        print("Le toca al jugador 1 ⭕, selecciona una fila (1,2 o 3) y la posición que sea dentro de la fila(1,2 o 3)")
        fila = int(input("Fila de colocación: "))
        columna = int(input("Posición dentro de la fila: "))
        if fila == 1 and columna == 1:
            tablero[0] = figura_juagdor1
        print(fila1)
        print(fila2)
        print(fila3)
