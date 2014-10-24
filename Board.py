import GamePieces
import copy

class Board():
	board = []
	winner = None
	
	def __init__(self):
		self.setUpBoard()
		self.currentPlayer = 'White'
		
	def setUpBoard(self):
		#Initialize board with pieces
		self.board = [["BlackRook","BlackKnight","BlackBishop", "BlackQueen", "BlackKing", "BlackBishop", "BlackKnight", "BlackRook"],
					  ["BlackPawn","BlackPawn","BlackPawn","BlackPawn","BlackPawn","BlackPawn","BlackPawn","BlackPawn"],
  					  ["","","","","","","",""],
  					  ["","","","","","","",""],
  					  ["","","","","","","",""],
  					  ["","","","","","","",""],
  					  ["WhitePawn","WhitePawn","WhitePawn","WhitePawn","WhitePawn","WhitePawn","WhitePawn","WhitePawn"],
					  ["WhiteRook","WhiteKnight","WhiteBishop", "WhiteQueen", "WhiteKing", "WhiteBishop", "WhiteKnight", "WhiteRook"]]

	def nextPlayer(self):
		if self.currentPlayer == 'White':
			self.currentPlayer = 'Black'
		else:
			self.currentPlayer = 'White'
			
	def copyBoard(self):
		newBoard = Board()
		newBoard.board = copy.deepcopy(self.board)
		newBoard.currentPlayer = self.currentPlayer
		return newBoard
