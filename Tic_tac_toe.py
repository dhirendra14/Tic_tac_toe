# Tic-Tac-Toe Program using


# importing all necessary libraries

import numpy as np

from os import system, name


# Creates an empty board

def create_board(N):
    return (np.full((N, N), '_'))


# Check for empty places on board

def possibilities(board):
    l = []

    for i in range(len(board)):

        for j in range(len(board)):

            if board[i][j] == '_':
                l.append((i, j))

    return (l)


# player can enter the position

def player_place(board, player):
    selection = possibilities(board)

    flag = False

    while flag == False:

        player_enter = input("please enter the position in the format x,y: ")

        lis = player_enter.split(',')

        x = int(lis[0]) - 1

        y = int(lis[1]) - 1

        current_loc = (x, y)

        if current_loc in selection:

            flag = True

        else:

            print('enter a valid input')

    # current_loc = random.choice(selection)

    board[current_loc] = player

    return (board)


# define our clear function

def clear():
    # for windows

    if name == 'nt':

        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')

    else:

        _ = system('clear')


# Checks whether the player has three

# of their marks in a horizontal row

def row_win(board, player):
    for x in range(len(board)):

        win = True

        for y in range(len(board)):

            if board[x, y] != player:
                win = False

                continue

        if win == True:
            return (win)

    return (win)


# Checks whether the player has three

# of their marks in a vertical row

def col_win(board, player):
    for x in range(len(board)):

        win = True

        for y in range(len(board)):

            if board[y][x] != player:
                win = False

                continue

        if win == True:
            return (win)

    return (win)


# Checks whether the player has three

# of their marks in a diagonal row

def diag_win(board, player):
    win = True

    for x in range(len(board)):

        if board[x, x] != player:
            win = False

    return (win)


# Evaluates whether there is

# a winner or a tie

def evaluate(board):
    winner = '_'

    for player in ['X', 'O']:

        if (row_win(board, player) or

                col_win(board, player) or

                diag_win(board, player)):
            winner = player

    if np.all(board != '_') and winner == '_':
        winner = -1

    return winner


# Main function to start the game

def play_game():
    try:

        N = int(input('size of the board: '))

        board, winner, counter = create_board(N), '_', 1

        print(board)

        while winner == '_':

            for player in ['X', 'O']:

                board = player_place(board, player)

                clear()

                print("Board after " + str(counter) + " move")

                print(board)

                counter += 1

                winner = evaluate(board)

                if winner != '_':
                    break

        if winner == 'X':

            winner = 'player 1'

        elif winner == 'O':

            winner = 'player 2'

        return (winner)

    except Exception as e:

        print(e)


# Driver Code

print("Winner is: " + str(play_game()))
