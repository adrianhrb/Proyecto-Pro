player1 = input("Name of player 1 (figure = ⭕): ")
player2 = input("Name of player 2 (figure = ❌): ")
figure_player1 = "⭕"
figure_player2 = "❌"
# Establecemos una condición para cambiar turnos entre jugadores
player_flow = True
# Definimos un contador que recogerá cada movimiento
moves_count = 0
# Definimos los movimientos límite o máximos
moves_limit = 9
board = [["⬛", "⬛", "⬛"], ["⬛", "⬛", "⬛"], ["⬛", "⬛", "⬛"]]
# Variables que representan posibles errores
occupied_square = "Occupied position, try again"
out_of_range = "Values are not in correct range, please introduce another position"
# Variables que van tomando valores dentro del bucle
error_message = ""
playing = True
victory = ""
while playing:
#Bucle que va a mostrar el tablero
    for line in board:
        for column in line:
            print(column, end=" ")
        print()
    if player_flow:
        print("It's",player1,"⭕ turn, select a line (1,2 o 3) and a column (1,2, o 3)")
        line = int(input("line in board: "))
        column = int(input("column: "))
        # Restamos uno al tamaño del board ya que empezamos en 0
        if 1 <= line <= 3 and 1 <= column <= 3 and board[line - 1][column - 1] == "⬛":
            board[line - 1][column - 1] = figure_player1
            moves_count += 1
            player_flow = not player_flow
        else:
            if 1 > line or line > 3 or 1 > column or column > 3:
                error_message = out_of_range
            elif board[line - 1][column - 1] != "⬛":
                error_message = occupied_square
            print(error_message)
    else:
        print("It's",player2,"❌ turn, select a line (1,2 o 3) and a column (1,2, o 3)")
        line = int(input("line in board: "))
        column = int(input("column: "))
        if 1 <= line <= 3 and 1 <= column <= 3 and board[line - 1][column - 1] == "⬛":
            board[line - 1][column - 1] = figure_player2
            moves_count += 1
            player_flow = not player_flow
        else:
            if 1 > line or line > 3 or 1 > column or column > 3:
                error_message = out_of_range
            elif board[line - 1][column - 1] != "⬛":
                error_message = occupied_square
            print(error_message)

#Definimos las condiciones de victoria
    for line in range(3):
        if board[line][0] == board[line][1] == board[line][2] != "⬛":
            victory = f'¡¡{board[line][0]} figure has won!!'
            playing = not playing
            break
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != "⬛":
            victory = f'¡¡{board[0][column]} figure has won!!'
            playing = not playing
            break
    if board[0][0] == board[1][1] == board[2][2] != "⬛":
        victory = f'¡¡{board[0][0]} figure has won!!'
        playing = not playing
    elif board[0][2] == board[1][1] == board[2][0] != "⬛":
        victory = f'¡¡{board[0][2]} has won!!'
        playing = not playing
    else:
        if moves_count == moves_limit:
            victory = "The game is a draw"
            playing = not playing

#Tablero final con victoria
for line in board:
    for column in line:
        print(column, end=" ")
    print()
print(victory) 
