class Board:
       def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""
      def get_size(self): 
             # optional, return the board size (an instance size)
      def get_winner(self):
            # return the winner's sign O or X (an instance winner)     
      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # you can use a tuple ("A1", "B1",...) to obtain indexes 
            # this implementation is up to you 
      def isempty(self, cell):
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # return True if the cell is empty (not marked with X or O)
      def isdone(self):
            done = False
            self.winner = ''
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            return done
      def show(self):
            print("  \n   A   B   C ")
            print(" +---+---+---+")
            print("1| {} | {} | {} |".format(self.board[0],self.board[3],self.board[6]))
            print(" +---+---+---+")
            print("2| {} | {} | {} |" .format(self.board[1],self.board[4],self.board[7]))
            print(" +---+---+---+")
            print("3| {} | {} | {} |".format(self.board[2],self.board[5],self.board[8]))
            print(" +---+---+---+")