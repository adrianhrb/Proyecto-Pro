jugador1 = input("Nombre del juagdor 1 (usará círculo): ") 
jugador2 = input("Nombre del jugador 2 (usará cruz): ")
figura_jugador1 = "⭕"
figura_jugador2 = "❌"
espacio_blanco = "⬛"
player_flow = True #True = Jugador 1, False = Jugador 2
tablero = ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"]
fila1 = f'{tablero[0]} | {tablero[1]} | {tablero[2]}'
fila2 = f'{tablero[3]} | {tablero[4]} | {tablero[5]}'
fila3 = f'{tablero[6]} | {tablero[7]} | {tablero[8]}'
occupied_square = 'Casilla ocupada, vuelve a intentarlo'
avaiable_square = 'Turno del oponente'

while True:
    if player_flow == True:
        print("Le toca a", jugador1, "⭕, selecciona una fila (1,2 o 3) y una columna(a, b, o c)")
        fila = int(input("Fila de colocación: "))
        columna = input("Columna: ")    
        if fila == 1 and columna.lower() == 'a':
            if tablero[0] != espacio_blanco:
                result = occupied_square
            else:
                tablero[0] = figura_jugador1
                fila1 = f'{tablero[0]} | {tablero[1]} | {tablero[2]}'
                result = avaiable_square
        elif fila == 1 and columna.lower() == 'b':
            if tablero[1] != espacio_blanco:
                result = occupied_square
            else:
                tablero[1] = figura_jugador1
                fila1 = f'{tablero[0]} | {tablero[1]} | {tablero[2]}'
        elif fila == 1 and columna.lower() == 'c':
            if tablero[2] != espacio_blanco:
                result = occupied_square
            else:
                tablero[2] = figura_jugador1
                fila1 = f'{tablero[0]} | {tablero[1]} | {tablero[2]}'
                result = avaiable_square
        elif fila == 2 and columna.lower() == 'a':
            if tablero[3] != espacio_blanco:
                result = occupied_square
            else:
                tablero[3] = figura_jugador1
                fila2 = f'{tablero[3]} | {tablero[4]} | {tablero[5]}'
                result = avaiable_square
        elif fila == 2 and columna.lower() == 'b':
            if tablero[4] != espacio_blanco:
                result = occupied_square
            else:
                tablero[4] = figura_jugador1
                fila2 = f'{tablero[3]} | {tablero[4]} | {tablero[5]}'
                result = avaiable_square
        elif fila == 2 and columna.lower() == 'c':
            if tablero[5] != espacio_blanco:
                result = occupied_square
            else:
                tablero[5] = figura_jugador1
                fila2 = f'{tablero[3]} | {tablero[4]} | {tablero[5]}'
                result = avaiable_square
        elif fila == 3 and columna.lower() == 'a':
            if tablero[6] != espacio_blanco:
                result = occupied_square
            else:
                tablero[6] = figura_jugador1
                fila3 = f'{tablero[6]} | {tablero[7]} | {tablero[8]}'
                result = avaiable_square
        elif fila == 3 and columna.lower() == 'b':
            if tablero[7] != espacio_blanco:
                result = occupied_square
            else:
                tablero[7] = figura_jugador1
                fila3 = f'{tablero[6]} | {tablero[7]} | {tablero[8]}'
                result = avaiable_square
        elif fila == 3 and columna.lower() == 'c':
            if tablero[8] != espacio_blanco:
                result = occupied_square
            else:
                tablero[8] = figura_jugador1
                fila3 = f'{tablero[6]} | {tablero[7]} | {tablero[8]}'
                result = avaiable_square
        print(fila1, fila2, fila3, sep="\n")
        print(result)
        if result == avaiable_square:
            player_flow = not player_flow

    elif player_flow == False:
        print("Le toca a", jugador2, "❌, selecciona una fila (1,2 o 3) y una columna(a, b, o c)")
        fila = int(input("Fila de colocación: "))
        columna = input("Columna: ")    
        if fila == 1 and columna.lower() == 'a':
            if tablero[0] != espacio_blanco:
                result = occupied_square
            else:
                tablero[0] = figura_jugador2
                fila1 = f'{tablero[0]} | {tablero[1]} | {tablero[2]}'
        elif fila == 1 and columna.lower() == 'b':
            if tablero[1] != espacio_blanco:
                result = occupied_square
            else:
                tablero[1] = figura_jugador2
                fila1 = f'{tablero[0]} | {tablero[1]} | {tablero[2]}'
                result = avaiable_square
        elif fila == 1 and columna.lower() == 'c':
            if tablero[2] != espacio_blanco:
                result = occupied_square
            else:
                tablero[2] = figura_jugador2
                fila1 = f'{tablero[0]} | {tablero[1]} | {tablero[2]}'
                result = avaiable_square
        elif fila == 2 and columna.lower() == 'a':
            if tablero[3] != espacio_blanco:
                result = occupied_square
            else:
                tablero[3] = figura_jugador2
                fila2 = f'{tablero[3]} | {tablero[4]} | {tablero[5]}'
                result = avaiable_square
        elif fila == 2 and columna.lower() == 'b':
            if tablero[4] != espacio_blanco:
                result = occupied_square
            else:
                tablero[4] = figura_jugador2
                fila2 = f'{tablero[3]} | {tablero[4]} | {tablero[5]}'
                result = avaiable_square
        elif fila == 2 and columna.lower() == 'c':
            if tablero[5] != espacio_blanco:
                result = occupied_square
            else:
                tablero[5] = figura_jugador2
                fila2 = f'{tablero[3]} | {tablero[4]} | {tablero[5]}'
                result = avaiable_square
        elif fila == 3 and columna.lower() == 'a':
            if tablero[6] != espacio_blanco:
                result = occupied_square
            else:
                tablero[6] = figura_jugador2
                fila3 = f'{tablero[6]} | {tablero[7]} | {tablero[8]}'
                result = avaiable_square
        elif fila == 3 and columna.lower() == 'b':
            if tablero[7] != espacio_blanco:
                result = occupied_square
            else:
                tablero[7] = figura_jugador2
                fila3 = f'{tablero[6]} | {tablero[7]} | {tablero[8]}'
                result = avaiable_square
        elif fila == 3 and columna.lower() == 'c':
            if tablero[8] != espacio_blanco:
                result = occupied_square
            else:
                tablero[8] = figura_jugador2
                fila3 = f'{tablero[6]} | {tablero[7]} | {tablero[8]}'
                result = avaiable_square
        print(fila1, fila2, fila3, sep="\n")
        print(result)
        if result == avaiable_square:
            player_flow = not player_flow


        
