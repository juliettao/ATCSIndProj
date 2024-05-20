#!/usr/bin/env python3

"""
connect4.py
This program creates a connect 4 game where the computer will play a player.
"""

__author__ = "Juliet Lord"
__version__ = "2024-05-21"

import random

class Connect4:
    def __init__(self):
        """
        This function initializes a 6x7 board using for loops 
        for connect 4 and intializes a variable that keeps track
        of the most recent move by the computer
        """
        self.board = []
        for i in range(6):
            row = []
            for i in range(7):
                row.append('')  # visualizes the board
            self.board.append(row)

        self.last_computer_move = None

    def print_board(self):
        """
        When I tried to put "." in when creating the board above, I could
        not figure out how to place pieces in for the dots, so instead I
        wrote this method to display a dot if the space is empty.
        *referenced GeeksForGeeks website to figure out how to display board
        correctly using .strip()
        """
        for row in self.board:
            row_str = ""
            for cell in row:
                if cell == '':
                    row_str += ". "
                else:
                    row_str += cell + " "
            print(row_str.strip())
        print("0 1 2 3 4 5 6")  #displays columns for user to pick

    def drop_piece(self, col, piece):
        """
        This method goes through each row in the column picked by
        either the player of computer and determines the lowest
        possible empty space to drop the piece into.
        """
        for row in range(5, -1, -1):   #going through rows from bottom to top
            if self.board[row][col] == '':  #checks if space is available
                self.board[row][col] = piece #drops piece into space
                return row, col
        return None   #if no spots available

    def check_winner(self, piece):
        """
        This method checks to see if the most recent piece dropped createcd
        a 4 in a row to win the game. I decided to only check horizontally
        and vertically to simplify the game for time sake.
        *referenced GeeksForGeeks for all() function
        """
        # Check horizontal
        for row in range(6):
            for col in range(4):
                if all(self.board[row][col + i] == piece for i in range(4)): #checks to see if 4 pieces in a row are either x 
                                                                             # or o
                    return True
        # Check vertical
        for row in range(3):
            for col in range(7):
                if all(self.board[row + i][col] == piece for i in range(4)):
                    return True
        return False

    def player_move(self):
        """
        This function first prompts the player to enter a column to place a piece in.
        Then, the function will place the piece at the lowest place available in
        the column
        """
        while True:  # makes sure that computer detects when a column is full
            col = input("Enter column (0-6): ")  #player input column
            col = int(col)                      #converts the column to an int to use in if statement below
            if 0 <= col <= 6:
                if self.board[0][col] == '':   #if the board is empty...
                    return self.drop_piece(col, 'X')  #place x in empty space
                else:
                    print("Column is full. Try again.")

    def computer_move(self):
        """
        This method models the computer moves. I designed the computer to 
        only place pieces near its previous pieces, or random for the first
        move or if there are no spaces near avaliable
        *referenced GeeksForGeeks on ways to shuffle a list, shuffle()
        """
        if self.last_computer_move:    #if  the computer made a move
            row, col = self.last_computer_move
            possible_moves = [                  #all the possible moves that are near the piece previously placed
                (row, col + 1), (row, col - 1), 
                (row + 1, col), (row - 1, col)
            ]
            random.shuffle(possible_moves)   #randomizes the possible order of moves
            for r, c in possible_moves:
                if 0 <= c < 7 and 0 <= r < 6 and self.board[0][c] == '':  #checks if space is free to put a piece
                    move = self.drop_piece(c, 'O')  #puts an O in lowest possible place
                    if move == True:      #if the move was made, no need to fall back to random option
                        self.last_computer_move = move      #updates the last computer move variable
                        return move   #exits function
        # makes random move if no nearby moves are valid
        while True:
            col = random.randint(0, 6)
            if self.board[0][col] == '':
                move = self.drop_piece(col, 'O')
                self.last_computer_move = move
                return move

    def play_game(self):
        """
        sets the game to keep playing until either the player
        of computer wins.
        """
        self.print_board()
        while True:
            # Player's move
            player_move = self.player_move()
            self.print_board()
            if self.check_winner('X'):
                print("Player wins!")
                break
            # Computer's move
            computer_move = self.computer_move()
            self.print_board()
            if self.check_winner('O'):
                print("Computer wins!")
                break


def main():
    # Play the game
    game = Connect4()
    game.play_game()


if __name__ == "__main__":
    main()