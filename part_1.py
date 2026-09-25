board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

player = "X"
turns = 0
game_over = False
print("Player 1 is X. Player 2 is O. To enter a value for the spot you want to place your symbol, you must enter the row number and column number. They are labelled 0, 1, 2.")

while game_over == False:
#so not game over while loop
    print("    0   1   2")
    print("  °❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")
    print("0 |", board[0][0], "|", board[0][1], "|", board[0][2], "|")
    print("  °❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")
    print("1 |", board[1][0], "|", board[1][1], "|", board[1][2], "|")
    print("  °❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")
    print("2 |", board[2][0], "|", board[2][1], "|", board[2][2], "|")
    print("  °❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")#columns

    print(f"{player}'s turn")

    row = int(input("Row (0-2): "))
    col = int(input("Column (0-2): "))

    good = True

    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid place! Try agai!")
       good = False


    if good == True:
        board[row][col] = player
        turns = turns + 1
        #only 9 turns

        for r in range(3):
            if board[r][0] == player and board[r][1] == player and board[r][2] == player:
                print(player, "wins!")
                game_over = True

        for c in range(3):
            if board[0][c] == player and board[1][c] == player and board[2][c] == player:
                print(player, "wins!")
                game_over = True

        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            print(player, "win!s")
            game_over = True

        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            print(player, "wins!")
            game_over = True

        if turns == 9 and game_over == False:
            print("Tie!")
            game_over = True

        if game_over == False:
            if player == "X":
                player = "O"
            else:
                player = "X"
