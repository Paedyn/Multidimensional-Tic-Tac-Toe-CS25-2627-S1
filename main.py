print("Hi! Welcome to Tic-Tac-Toe.")
turns=0
player_1=(input("Player one. Enter your name here."))
symbol_1= "X"
player_2=(input("Player two. Enter your name here."))
symbol_2= "0"
print(f"{player_1}, your symbol is {symbol_1}")
print(f"{player_2}, your symbol is {symbol_2}")
board=[
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
print(list)
print("Here is your tic-tac-toe board.")
turns= 0
current_player= 1

while True:
    #PRINT BOARD
    print("    0   1   2")
    print("  +---+---+---+")
    for r in range(3):
        print(f"{r} | {board[r][0]} | {board[r][1]} | {board[r][2]} |")
        print("  +---+---+---+")
    if current_player == 1:
        symbol = symbol_1
        name = player_1
    else:
          symbol = symbol_2
          name = player_2
          print("")

    print(f"{name}'s turn ({symbol}).")

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid position! Must be between 0 and 2.")

    board[row][col] = symbol
    turns += 1

    # Check rows
    for r in range(3):
        if board[r][0] == symbol and board[r][1] == symbol and board[r][2] == symbol:
            print(f"{name} wins by row!")


    # Check columns
    for c in range(3):
        if board[0][c] == symbol and board[1][c] == symbol and board[2][c] == symbol:
         print(f"{name} wins by column!")if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        print(f"{name} wins by diagonal!")
        exit()

    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        print(f"{name} wins by diagonal!")
        exit()

    # Check tie
    if turns == 9:
        print("It's a tie! No more spaces left.")
        exit()

    # Switch players
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1




# while turns<=9:
#
#
# #hile True
# #PLAYER PLAYING
# print("To enter your symbols, you must input indexes based of columns and rows. Ex,0, 0 for the top left corner")
# player = (input("Are you player 1 or 2"))
# if player=1:
#     "Enter your indexes."
# else:
#     print("Sorry! Player 1 must go first.")
# position = (input(f"Player {player}, choose your position (1-9):"))
# if position < 0 or position > 9:
#  print("Position must be between 1 and 9!")
# else:
#     print()
#
# #     current_player = player_1
# # (input("Are you player 1 or 2"))
# #     current_symbol = "X"
# #     turns = 0
# #
# # #while turns_count < 9:
# # print()
# # turn=(input("Enter two indexes to place your X"))
# #
# # if WIN WIN Win
# # for x or 0
# #     print win