#author: Rahul Nadkarni
# date: July 5, 2021
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board

from board import Board
from player import Player,Random_AI
# main program
print("Welcome to TIC-TAC-TOE Game!")
while True:
    board = Board()
    player1 = Player("Player 1", "X")
    player2 = Random_AI("Player 2", "O",board)
    turn = True
    while True:
        board.show()
        if turn:
            player1.choose(board)
            turn = False
        else:
            player2.choose(board)
            turn = True
        if board.isdone():
            break
    board.show()
    if board.get_winner() == player1.get_sign():
        print(f"{player1.get_name()} is the winner!")
    elif board.get_winner() == player2.get_sign():
        print(f"{player2.get_name()} is the winner!")
    else:
        print("It is a tie!")
    ans = input("Would you like to play again? [Y/N]\n").upper()
    if (ans != "Y"):
        break
print("Goodbye!")