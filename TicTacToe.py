#-----------------Tic Tac Toe Game------------------

#-----------------initialize the board--------------
board=[" " for _ in range(9)]

#-----------------display the board-----------------
def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")

#-------------check for win--------------------------
def check_win(player):
    win_conditions=[
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i]==player for i in condition):
            return True
    return False

#---------------check for draw-----------------------
def check_draw():
    return " " not in board

#---------------main game loop------------------------
def play_game():
    current_player="X"
    while True:
        display_board()
        try:
            move=int(input(f"Player {current_player}, enter your move (1-9): "))-1
            if board[move]==" ":
                board[move]=current_player
                if check_win(current_player):
                    display_board()
                    print(f"***Player {current_player} wins!***")
                    break
                elif check_draw():
                    display_board()
                    print("---It's a draw!---")
                    break
                #--------switch player----------
                current_player="0" if current_player=="X" else "X"
            else:
                print("XXXX That spot is already taken. try again. ")
        except (IndexError,ValueError):
            print("Invalid input, Enter a number between 1 and 9")

#----------------------Start the Game-----------------------------------
play_game()

#----------------------END OF PROGRAM-----------------------------------