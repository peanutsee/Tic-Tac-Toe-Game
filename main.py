from support import TicTacToe, Player

# Instantiate Players
print("***Enter Player 1***")
player1 = Player().create_player()

print("***Enter Player 2***")
player2 = Player().create_player()

# Instantiate TicTacToe
TTT = TicTacToe(player1, player2)

# Current player tracker
current_player = 1

# Game Over
not_gameover = TTT.validate_board()


while not_gameover:
    print("***Current Board Display***")
    TTT.display()
    if current_player == 1:
        print(f"{player1[0]}'s turn!")
        TTT.user_input(player1)
    else:
        print(f"{player2[0]}'s turn!")
        TTT.user_input(player2)
    not_gameover = TTT.validate_board()
    current_player *= -1

print("WE HAVE A WINNER!!")
print(f"{player1[0]} WON!!" if current_player*-1 == 1 else f"{player2[0]} WON!!")
