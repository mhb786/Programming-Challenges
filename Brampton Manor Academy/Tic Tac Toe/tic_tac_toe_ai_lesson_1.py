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
            if board[Column][Row] == '':
                empty.append([Column, Row])

    return empty


def player_turn(player_sign, board, empty_cells):
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
    br = True
    while br:
        try:
          turn = [random.randint(0, 2), random.randint(0, 2)]
          Column = int(turn[0])
          Row = int(turn[1])

          if Column and Row not in range(3):
              raise Exception
          elif [Column, Row] in empty_cells:
              br = False
          else:
              raise Exception
        except Exception:
          print()

    board[Column][Row] = player_sign

    return board


def CheckBoard(board):
    pass

def reset_board():
    board = [['' for Column in range(3)] for Row in range(3)]
    return board


def display_board(board):
    for i in board:
        print(i)
    print('\n')


def main():
    print("Welcome to Tic Tac Toe")
    board = reset_board()
    empty = empty_cells(board)
    display_board(board)
    Finished = False

    while not Finished:
        print("Player 1 turn")
        player_turn(PLAYER, board, empty)
        empty = empty_cells(board)
        display_board(board)

        print("AI turn")
        ai_turn(AI, board, empty)
        empty = empty_cells(board)
        display_board(board)


main()
