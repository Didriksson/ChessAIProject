import RulesPieces
import copy
import GamePieces

class RuleController():
	
	def __init__(self, darkPieces,lightPieces):
		self.darkPieces = darkPieces
		self.lightPieces = lightPieces
	
	def presentMove(self,board,source, destination):
		sourcePiece = board[source[0]][source[1]]
		destinationPiece = board[destination[0]][destination[1]]
		if sourcePiece == 'EMPTY':
			return False

		if not sourcePiece.color == destinationPiece.color:
			nameOfPiece = type(sourcePiece).__name__
			moveOkay = getattr(RulesPieces, nameOfPiece.lower())
			if moveOkay(source, destination, board):
				return True
		else:
			return False
			
	def makeMove(self, board, source, destination, realMove):
		newBoard = copy.deepcopy(board)
		sourcePiece = newBoard[source[0]][source[1]]
		destinationPiece = newBoard[destination[0]][destination[1]]
		if(destinationPiece != 'EMPTY') and realMove:
			self.removePieceFromList(destinationPiece)
		newBoard[destination[0]][destination[1]] = newBoard[source[0]][source[1]]
		newBoard[source[0]][source[1]].position = destination
		newBoard[source[0]][source[1]] = GamePieces.Empty()
		return newBoard
			
			
	def removePieceFromList(self,piece):
		for key, value in self.lightPieces.iteritems():
			if value is piece:
				del self.lightPieces[key]
				break
		
		for key, value in self.darkPieces.iteritems():
			if value is piece:
				del self.darkPieces[key]
				break

	def isChess(self,board,currentPlayer):
		if currentPlayer == self.lightPieces:
			kingsPosition = self.getPositionForPiece(board,GamePieces.King,'dark')
		else:
			kingsPosition = self.getPositionForPiece(board,GamePieces.King,'light')
			
		for piece in currentPlayer.values():
			nameOfPiece = type(piece).__name__
			moveOkay = getattr(RulesPieces, nameOfPiece.lower())
			source = self.getPositionForPiece(board,piece)
			if moveOkay(source, kingsPosition, board, self.lightPieces, self.darkPieces):
				return True
		return False
		
	def getPositionForPiece(self,board,piece, color):
		for row in range(len(board)):
			if piece is board[row] and piece.color == color:
				col = board[row].index(piece)
				break
		return (row, col)
			
	def getWhitePiecesOnBoard(self, board):
		currentPieces = {}
		for row in range(8):
			for col in range(8):
				if board[row][col] != 'EMPTY':
					if board[row][col].color == 'white':
						currentPieces[board[row][col]] = (row,col)
		return currentPieces
		
	def getDarkPiecesOnBoard(self, board):
		currentPieces = {}
		for row in range(8):
			for col in range(8):
				if board[row][col] != 'EMPTY':
					if board[row][col].color == 'dark':
						currentPieces[board[row][col]] = (row,col)
		return currentPieces