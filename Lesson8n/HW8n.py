# tic tac toe
print('tic tac toe')
print('Let the game begin...')

# coordinates of moves
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


# graphical representation of the board
def printBoard(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])


# Main function
def game():
    player = 'X'

    # Enable turns of players
    for i in range(10):
        # prints board with input from players
        printBoard(theBoard)
        print("It's your turn, " + player + ". Select cell.")

        move = input()

        # (1) check if cell is blank, if yes, put player's sign (X or O)
        if theBoard[move] == ' ':
            theBoard[move] = player
            # count += 1
        else:
            print("That place is already filled. Select different cell.")
            continue

        # (2) check if there is a winning combination
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            break
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            break

        # (3) change the player after every move
        if player == 'X':
            player = 'O'
        else:
            player = 'X'


game()
