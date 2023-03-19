# Shahria Abeed

# makes an empty board with 9 slots
# slots 0 - 3 represent row 1 and so on
def makeBoard():
    output = [" " for _ in range(9)]
    return output
# makeBoard()


# displays the board
def printBoard(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")

        # don't print division at the end
        if i != 6:
            print("-----------")
# printBoard(board)


# will be used to ensure the player enters a valid move
def isValid(usr_inp):
    try:
        usr_inp = int(usr_inp)
        return usr_inp >= 1 and usr_inp <= 3
    except:
        return False
# isValid(usr_inp)


# lets players make their move
def playerMove(board, player):
    def selectPos():
        row = input(f"{player}, enter a row (1 - 3): ")
        while not isValid(row):
            print("\nInvalid row entered.\n")
            row = input(f"{player}, enter a row (1 - 3): ")
        
        column = input(f"{player}, enter a column (1 - 3): ")
        while not isValid(column):
            print("\nInvalid column entered.\n")
            column = input(f"{player}, enter a column (1 - 3): ")
        
        return ((int(row) - 1) * 3) + int(column) - 1
    # selectPos()


    position = selectPos()
    while(board[position] != " "):
        print("\nThat position is already taken. Try again.\n")
        position = selectPos()
    
    board[position] = player
# playerMove(board, player)
    


def checkWin(board):
    # horizontal
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            print("\n" + board[i] + " wins!\n" )
            return True
        
    # vertical
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            print("\n" + board[i] + " wins!")
            return True
        
    # diagonals
    if board[0] == board[4] == board[8] != " ": 
        print("\n" + board[0] + " wins!\n")
        return True
    if board[2] == board[4] == board[6] != " ":
        print("\n" + board[2] + " wins!\n")
        return True
    
    return False     
# checkWin(board)



def TicTacToe():
    # initialize game
    current_player = "X"
    turn = 0 # check for draw without looping through board
    board = makeBoard()
    printBoard(board)
    print()


    while(not checkWin(board)):
        playerMove(board, current_player)
        print()

        if(current_player) == "X":
            current_player = "O"
        else:
            current_player = "X"
        printBoard(board)
        print()

        turn += 1
        if(turn == 9):
            print("\nDraw!\n")
            break
# TicTacToe()       


def main():
    play_again = "y"
    
    while(play_again.lower() == "y" or play_again.lower() == "yes"):
        TicTacToe()
        play_again = input("Would you like to play again (y/n): ")

    print("\nThank you for playing!")
# main()    
    

main()
