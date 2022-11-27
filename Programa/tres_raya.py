jugador1 = input("Nombre del juagdor 1 (usará círculo): ") 
jugador2 = input("Nombre del jugador 2 (usará cruz): ")
figura_jugador1 = "⭕"
figura_jugador2 = "❌"
espacio_blanco = "⬛"
player_flow = True #Que irá cambiando para cada turno
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
            n = 0
        elif fila == 1 and columna.lower() == 'b':
            n = 1
        elif fila == 1 and columna.lower() == 'c':
            n = 2
        elif fila == 2 and columna.lower() == 'a':
            n = 3
        elif fila == 2 and columna.lower() == 'b':
            n = 4
        elif fila == 2 and columna.lower() == 'c':
            n = 5
        elif fila == 3 and columna.lower() == 'a':
            n = 6
        elif fila == 3 and columna.lower() == 'b':
            n = 7
        elif fila == 3 and columna.lower() == 'c':
            n = 8
        if tablero[n] != espacio_blanco:
            result = occupied_square
        else: 
            result = avaiable_square   
            tablero[n] = figura_jugador1
            player_flow = not player_flow
            fila1 = f'{tablero[0]} | {tablero[1]} | {tablero[2]}'
            fila2 = f'{tablero[3]} | {tablero[4]} | {tablero[5]}'
            fila3 = f'{tablero[6]} | {tablero[7]} | {tablero[8]}'
        print(fila1, fila2, fila3, sep="\n")
        print(result)
        

    elif player_flow == False:
        print("Le toca a", jugador2, "❌, selecciona una fila (1,2 o 3) y una columna(a, b, o c)")
        fila = int(input("Fila de colocación: "))
        columna = input("Columna: ")    
        if fila == 1 and columna.lower() == 'a':
            n = 0
        elif fila == 1 and columna.lower() == 'b':
            n = 1
        elif fila == 1 and columna.lower() == 'c':
            n = 2
        elif fila == 2 and columna.lower() == 'a':
            n = 3
        elif fila == 2 and columna.lower() == 'b':
            n = 4
        elif fila == 2 and columna.lower() == 'c':
            n = 5
        elif fila == 3 and columna.lower() == 'a':
            n = 6
        elif fila == 3 and columna.lower() == 'b':
            n = 7
        elif fila == 3 and columna.lower() == 'c':
            n = 8
        if tablero[n] != espacio_blanco:
            result = occupied_square
        else: 
            result = avaiable_square   
            tablero[n] = figura_jugador2
            player_flow = not player_flow
            fila1 = f'{tablero[0]} | {tablero[1]} | {tablero[2]}'
            fila2 = f'{tablero[3]} | {tablero[4]} | {tablero[5]}'
            fila3 = f'{tablero[6]} | {tablero[7]} | {tablero[8]}'
        print(fila1, fila2, fila3, sep="\n")
        print(result)

            

'''#Establecemos las condiciones de victoria, clarificando que si son espacios en blanco no se gana
    if tablero[0] and tablero[1] and tablero[2] != espacio_blanco:
        if tablero[0] == tablero[1] and tablero[2]:
            print("Ganates loco")
            print(fila1, fila2, fila3, sep="\n")
            break
    elif tablero[3] and tablero[4] and tablero[5] != espacio_blanco:
        if tablero[3] == tablero[4] and tablero[5]:
            print("Ganates loco")
            print(fila1, fila2, fila3, sep="\n")
            break
    elif tablero[6] and tablero[7] and tablero[8] != espacio_blanco:
        if tablero[6] == tablero[7] and tablero[8]:
            print("Ganates loco")
            print(fila1, fila2, fila3, sep="\n")
            break
    elif tablero[0] and tablero[4] and tablero[8] != espacio_blanco:
        if tablero[0] == tablero[4] and tablero[8]:
            print("Ganates loco")
            print(fila1, fila2, fila3, sep="\n")
            break
    elif tablero[2] and tablero[4] and tablero[6] != espacio_blanco:
        if tablero[2] == tablero[4] and tablero[6]:
            print("Ganates loco")
            print(fila1, fila2, fila3, sep="\n")
            break
    elif tablero[0] and tablero[3] and tablero[6] != espacio_blanco:
        if tablero[0] == tablero[3] and tablero[6]:
            print("Ganates loco")
            print(fila1, fila2, fila3, sep="\n")
            break
    elif tablero[1] and tablero[4] and tablero[7] != espacio_blanco:
        if tablero[1] == tablero[4] and tablero[7]:
            print("Ganates loco")
            print(fila1, fila2, fila3, sep="\n")
            break
    elif tablero[2] and tablero[5] and tablero[8] != espacio_blanco:
        if tablero[2] == tablero[5] and tablero[8]:
            print("Ganates loco")
            print(fila1, fila2, fila3, sep="\n")
            break'''
            

