import GamePieces
import copy

class Board():
	board = []
	winner = None
	
	def __init__(self):
		self.createPieces()
		self.setUpBoard()
		self.currentPlayer = 'white'
		
	def setUpBoard(self):
		#Initialize board with pieces
		for y in range (8):
			line = []
			for x in range(8):
				line.append(GamePieces.Empty())
			self.board.append(line)
		
		for piece in self.lightPieces.itervalues():
			self.board[piece.position[0]][piece.position[1]] = piece
	
		for piece in self.darkPieces.itervalues():
			self.board[piece.position[0]][piece.position[1]] = piece	
	
	def createPieces(self):
		self.darkPieces = {
		'darkKing' : GamePieces.King('darkKing',(0,4), 'black'),
		'darkQueen' : GamePieces.Queen('darkQueen',(0,3),'black'),
		'darkRook1' : GamePieces.Rook('darkRook', (0,0),'black'),
		'darkRook2' : GamePieces.Rook('darkRook', (0,7),'black'),
		'darkKnight1' : GamePieces.Knight('darkKnight',(0,1),'black'),
		'darkKnight2' : GamePieces.Knight('darkKnight',(0,6),'black'),
		'darkBishop1' : GamePieces.Bishop('darkBishop',(0,5),'black'),
		'darkBishop2' : GamePieces.Bishop('darkBishop',(0,2),'black'),
		'darkPawn1' : GamePieces.Pawn('darkPawn',(1,0),'black'),
		'darkPawn2' : GamePieces.Pawn('darkPawn',(1,1),'black'),
		'darkPawn3' : GamePieces.Pawn('darkPawn',(1,2),'black'),	
		'darkPawn4' : GamePieces.Pawn('darkPawn',(1,3),'black'),
		'darkPawn5' : GamePieces.Pawn('darkPawn',(1,4),'black'),
		'darkPawn6' : GamePieces.Pawn('darkPawn',(1,5),'black'),
		'darkPawn7' : GamePieces.Pawn('darkPawn',(1,6),'black'),
		'darkPawn8' : GamePieces.Pawn('darkPawn',(1,7),'black'),
		}

		self.lightPieces = {
		'lightKing' : GamePieces.King(('lightKing'),(7,4),'white'),
		'lightQueen' : GamePieces.Queen(('lightQueen'),(7,3),'white'),
		'lightRook1' : GamePieces.Rook(('lightRook'), (7,0),'white'),
		'lightRook2' : GamePieces.Rook(('lightRook'), (7,7),'white'),
		'lightKnight1' : GamePieces.Knight(('lightKnight'),(7,1),'white'),
		'lightKnight2' : GamePieces.Knight(('lightKnight'),(7,6),'white'),
		'lightBishop1' : GamePieces.Bishop(('lightBishop'),(7,5),'white'),
		'lightBishop2' : GamePieces.Bishop(('lightBishop'),(7,2),'white'),
		'lightPawn1' : GamePieces.Pawn(('lightPawn'),(6,0),'white'),
		'lightPawn2' : GamePieces.Pawn(('lightPawn'),(6,1),'white'),
		'lightPawn3' : GamePieces.Pawn(('lightPawn'),(6,2),'white'),		
		'lightPawn4' : GamePieces.Pawn(('lightPawn'),(6,3),'white'),
		'lightPawn5' : GamePieces.Pawn(('lightPawn'),(6,4),'white'),
		'lightPawn6' : GamePieces.Pawn(('lightPawn'),(6,5),'white'),
		'lightPawn7' : GamePieces.Pawn(('lightPawn'),(6,6),'white'),
		'lightPawn8' : GamePieces.Pawn(('lightPawn'),(6,7),'white'),
		}
		
	def nextPlayer(self):
		if self.currentPlayer == 'white':
			self.currentPlayer = 'black'
		else:
			self.currentPlayer = 'white'
			
	def copyBoard(self):
		newBoard = Board()
		newBoard.board = copy.deepcopy(self.board)
		newBoard.currentPlayer = self.currentPlayer
		return newBoard