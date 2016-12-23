#!/usr/bin/python3
# tic-tac-toe game representation using dictionary
board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '
         }

def printBorad(board):
    print('{}|{}|{}'.format(board['top-L'], board['top-M'], board['top-R']))
    print('-+-+-')
    print('{}|{}|{}'.format(board['mid-L'], board['mid-M'], board['mid-R']))
    print('-+-+-')
    print('{}|{}|{}'.format(board['low-L'], board['low-M'], board['low-R']))

turn = 'X'
while ' ' in board.values():
    printBorad(board)
    print("possible moves :")
    for key in board.keys():
        if board[key] == ' ':
            print(key)
    print('Turn for {} . Move on which place?'.format(turn))
    move = input()
    board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
