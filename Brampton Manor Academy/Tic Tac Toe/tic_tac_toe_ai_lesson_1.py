import random
from math import inf as infinity
from random import choice
import platform
import time
from os import system

PLAYER = 'X'
AI = 'O'


def empty_cells(board):
    empty = []
    for Column in range(3):
        for Row in range(3):
            if board[Column][Row] == ' ':
                empty.append([Column, Row])

    return empty


def player_turn(player_sign, board, empty_cells):
    print("Player 1 turn")
    br = True
    while br:
        turn = input("Enter a coordinate: ")
        Column = int(turn[0])
        Row = int(turn[1])

        if Column and Row not in range(3):
            print("Enter a valid coordinate")
        elif [Column, Row] in empty_cells:
            board[Column][Row] = player_sign
            br = False
        else:
            print("This position is already filled.")

    return board


def ai_turn(player_sign, board, empty_cells):
    print("AI turn")
    choice = random.choice(empty_cells)
    Column, Row = choice[0], choice[1]

    board[Column][Row] = player_sign
    return board


def CheckBoard(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            print("You are the winner")
            return row[0]

    for Column in range(3):
        x = set([board[Column][Row] for Row in range(3)])
        print(x)
        if len(x) == 1 and x[0] != ' ':
            print("You are the winner")
            return x[0]



    # if len(set([board[i][i] for i in range(len(board))])) == 1:
    #     print("yay")
    #     return board[0][0]
    # if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
    #     print("yay")
    #     return board[0][len(board) - 1]

    return 0


def reset_board():
    board = [[' ' for Column in range(3)] for Row in range(3)]
    return board


def display_board(board):
    str_line = '---------------'
    print('\n' + str_line)
    for row in board:
        for cell in row:
            print(f'| {cell} |', end='')
        print('\n' + str_line)


def main():
    print("Welcome to Tic Tac Toe")
    board = reset_board()
    empty = empty_cells(board)
    display_board(board)
    Finished = False

    while not Finished:
        player_turn(PLAYER, board, empty)
        empty = empty_cells(board)
        display_board(board)
        if CheckBoard(board):
            break

        ai_turn(AI, board, empty)
        empty = empty_cells(board)
        display_board(board)
        if CheckBoard(board):
            break

    print("Game has ended")

main()

