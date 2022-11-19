# X/0 game using server and two players (clients)
# tic-tac-toe
import sys

from colorama import Fore
from colorama import Style

print('\t ***TIC TAC TOE***')
print('Let the game begin...')

# coordinates of moves
theBoard = {'7': '7', '8': '8', '9': '9',
            '4': '4', '5': '5', '6': '6',
            '1': '1', '2': '2', '3': '3'}

theBoardNew = {'7': '7', '8': '8', '9': '9',
               '4': '4', '5': '5', '6': '6',
               '1': '1', '2': '2', '3': '3'}

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

player1 = 'Mykola'
player2 = 'Valeriia'


# graphical representation of the board
def printBoard(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])


# Main function
def game(player1, player2):
    option = input(f'\n{Fore.BLUE}{player1}{Style.RESET_ALL}, will you play with X? [Y/N]')
    if option.lower() == 'y':
        playerX = player1
        playerY = player2
        print(f"{Fore.BLUE}{player1}{Style.RESET_ALL}, you play with X"
              f"\n{Fore.YELLOW}{player2}{Style.RESET_ALL} you play with 0\n")

    else:
        playerX = player2
        playerY = player1
        print(f"{Fore.YELLOW}{player2}{Style.RESET_ALL}, you play with X"
              f"\n{Fore.BLUE}{player1}{Style.RESET_ALL}, you play with 0\n")

    turns(playerX, playerY)


def turns(playerX, playerY):
    # Player X
    for i in range(10):
        # prints board with input from players
        printBoard(theBoard)
        print(f"It's your turn, {Fore.BLUE}{playerX}{Style.RESET_ALL}. Select cell.")

        move = str(input())

        # (1) check if cell is in the list 1-9, if yes, put player's sign (X or O)
        if theBoard[move] in options:
            theBoard[move] = 'X'

        else:
            print("That place is already filled. Select different cell.")
            continue

        # (2) check if there is a winning combination
        check_results()

        # (3) Player Y
        printBoard(theBoard)
        print(f"It's your turn, {Fore.YELLOW}{playerY}{Style.RESET_ALL}. Select cell.")

        move = str(input())

        # (1) check if cell is in the list 1-9, if yes, put player's sign (X or O)
        if theBoard[move] in options:
            theBoard[move] = '0'

        else:
            print("That place is already filled. Select different cell.")
            continue

        # (2) check if there is a winning combination
        check_results()


def check_results():
    if theBoard['7'] == theBoard['8'] == theBoard['9']:
        printBoard(theBoard)
        go_on(player1, player2)
    elif theBoard['4'] == theBoard['5'] == theBoard['6']:
        printBoard(theBoard)
        go_on(player1, player2)
    elif theBoard['1'] == theBoard['2'] == theBoard['3']:
        printBoard(theBoard)
        go_on(player1, player2)
    elif theBoard['1'] == theBoard['4'] == theBoard['7']:
        printBoard(theBoard)
        go_on(player1, player2)
    elif theBoard['2'] == theBoard['5'] == theBoard['8']:
        printBoard(theBoard)
        go_on(player1, player2)
    elif theBoard['3'] == theBoard['6'] == theBoard['9']:
        printBoard(theBoard)
        go_on(player1, player2)
    elif theBoard['7'] == theBoard['5'] == theBoard['3']:
        printBoard(theBoard)
        go_on(player1, player2)
    elif theBoard['1'] == theBoard['5'] == theBoard['9']:
        printBoard(theBoard)
        go_on(player1, player2)


def go_on(player1, player2):
    global theBoard

    print('Game over!')
    option = input("Do you want to continue?[Y/N] ")

    if option.lower() == "y":
        theBoard = theBoardNew
        game(player1, player2)
    else:
        print('Session terminated...')
        sys.exit()


game(player1, player2)
