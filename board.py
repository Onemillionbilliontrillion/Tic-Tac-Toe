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
             return self.get_size
      def get_winner(self):
            # return the winner's sign O or X (an instance winner)
            return self.winner   
              
      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # you can use a tuple ("A1", "B1",...) to obtain indexes 
            # this implementation is up to you 
            values =('A1','A2','A3','B1','B2','B3','C1','C2','C3')
            cell_numbers = values.index(cell)
            if self.board[cell_numbers]:
              self.board[cell_numbers] = sign
      def isempty(self, cell):
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # return True if the cell is empty (not marked with X or O)
            values =('A1','A2','A3','B1','B2','B3','C1','C2','C3')
            cell_numbers = values.index(cell)
            if self.board[cell_numbers] == ' ':
              return True
            else:
              return False     
      def isdone(self):
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
          for i in range(0,len(self.board),3):
            # i = 0,3,6
             #if board[i value] value = x, if i +1 = x and i + 2 = x: self.winner = x, 
            if self.board[i] == 'X' and self.board[i + 1] == 'X' and self.board[i + 2] == 'X':
              self.winner = 'X'
              return self.winner 
            elif self.board[i] == 'O' and self.board[i + 1] == 'O' and self.board[i + 2] == 'O':
              self.winner = 'O'
              return self.winner 
          for i in range(3): #0 - > 2
            if self.board[i] == 'X' and self.board[i + 3] == 'X' and self.board[i + 6] == 'X':
              self.winner = 'X'
              return self.winner 
            elif self.board[i] == 'O' and self.board[i + 3] == 'O' and self.board[i + 6] == 'O':
              self.winner = 'O'
              return self.winner 
          if self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X':
              self.winner = 'X'
              return self.winner 
          elif self.board[2] == 'O' and self.board[4] == 'O' and self.board[6] == 'O':
              self.winner = 'O'
              return self.winner 
          occupied = 0
          istie = False
          while not istie: 
            for i in range(len(self.board)):
              if self.board[i] != " ":
                occupied += 1
            if occupied == 9:
              istie = True 
              if istie:
                self.winner = " "
              return istie
            break         
          #Return True if there is a tie
          #All spaces are full 
          #No Winner Check 
          #No 3 in a Row Check 
          
          #self.board is a list of signs(Xs and Os)
          #using a loop, check if each value is an X/O, or you can check if that spot is != " "
          #If the value is not empty, then occupied should increase by one 
          #if occupied is equal to 9, return istie = True, self.winner = " "
      def possibleMoves(self):
            cell_list = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
            empty = []
            for x in range(len(cell_list)):
              if self.isempty(cell_list[x]) == True:
                empty.append(x)
            return empty
      def show(self):
            print("  \n   A   B   C ")
            print(" +---+---+---+")
            print("1| {} | {} | {} |".format(self.board[0],self.board[3],self.board[6]))
            print(" +---+---+---+")
            print("2| {} | {} | {} |" .format(self.board[1],self.board[4],self.board[7]))
            print(" +---+---+---+")
            print("3| {} | {} | {} |".format(self.board[2],self.board[5],self.board[8]))
            print(" +---+---+---+")
#.  0. 3. 6 
#.  1  4  7 
#.  2. 5. 8