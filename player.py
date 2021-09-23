import random
from board import Board
class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            # return an instance sign
            return self.sign
      def get_name(self):
            # return an instance name
            return self.name
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            choose_cell = input('Where do you want to move? ')
            cell_list = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
            choose_cell = choose_cell.upper()
            if choose_cell in cell_list:
              if board.isempty(choose_cell):
                board.set(choose_cell,self.sign)
              else:
                print("Cell is already occupied.")
                self.choose(board)
            else:
              print("Cell does not exist.")
              self.choose(board)

#Create a child class RandomAI that selects a board spot at random. If the spot is taken then the AI should pick another open spot to place down. 

class Random_AI(Player):
      def __init__(self,name,sign,board):
        super().__init__(name,sign)
        self.name = name
        self.sign = sign
        self.board=board
      def choose(self, board): 
        while True:
          cell_list = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
          chosen_cell = random.choice(cell_list)
          if board.isempty(chosen_cell):
            board.set(chosen_cell,self.sign)
            break
          else:
            cell_list.remove(chosen_cell)
            continue
        #somehow remove that cell 
        #continue the while loop until it sets down a sign
class Minimax(Random_AI):
      def choose(self,board):
        print("pick a cell from A1 - B3")
        cell = Minimax.minimax(self,board,True,False) 
        #print cell 
        print(cell)
        board.set(cell,self.sign)
        #Set cell down on the board
       
        
                              #bool. #bool
      def minimax(self,board,player,start):
        max_score = float("-inf")
        min_score = float("inf")
        bestmove = ""
        if board.isdone():
          if board.getwinner() == self.sign():
          #.getwinner(), self.sign:
            return 1 
          elif board.getwinner() == " ":#something:
            return 0 
          elif board.getwinner() != self.sign():
            return -1 
        for move in board.possiblemoves():
          #check if move is empty 
            #see if it is you who is playing
              #place that move down 
              #AI needs to play the game <--------
              
              if board.isempty(move) == True:
                if self.player == True:
                  board.set(move,self.sign)
                  score = Minimax.minimax(board,player,start)
                  
              
        if start:
          return bestmove
        elif self.player == True:
          return max_score 
        else:
          return min_score 
