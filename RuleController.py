import RulesPieces

class RuleController():
	
	def __init__(self, board, darkPieces,lightPieces):
		self.board = board
		self.darkPieces = darkPieces
		self.lightPieces = lightPieces
	
	def presentMove(self,source, destination):
		sourcePiece = self.board[source[0]][source[1]]
		destinationPiece = self.board[destination[0]][destination[1]]
		if sourcePiece == 'EMPTY':
			return False

		if not ((sourcePiece in self.lightPieces.values() and destinationPiece in self.lightPieces.values()) or (sourcePiece in self.darkPieces.values() and destinationPiece in self.darkPieces.values())):
			nameOfPiece = type(sourcePiece).__name__
			moveOkay = getattr(RulesPieces, nameOfPiece.lower())
			if moveOkay(source, destination, self.board, self.lightPieces, self.darkPieces):
				if(destinationPiece != 'EMPTY'):
					self.removePieceFromList(destinationPiece)
				self.board[destination[0]][destination[1]] = self.board[source[0]][source[1]]
				self.board[source[0]][source[1]].position = destination
				self.board[source[0]][source[1]] = "EMPTY"
				return True
		else:
			return False
			
			
	def removePieceFromList(self,piece):
		for key, value in self.lightPieces.iteritems():
			if value is piece:
				del self.lightPieces[key]
				break
		
		for key, value in self.darkPieces.iteritems():
			if value is piece:
				del self.darkPieces[key]
				break

	def isChess(self, currentPlayer):
		if currentPlayer == self.lightPieces:
			kingsPosition = self.getPositionForPiece(self.darkPieces['darkKing'])
		else:
			kingsPosition = self.getPositionForPiece(self.lightPieces['lightKing'])
			
		for piece in currentPlayer.values():
			nameOfPiece = type(piece).__name__
			moveOkay = getattr(RulesPieces, nameOfPiece.lower())
			source = self.getPositionForPiece(piece)
			if moveOkay(source, kingsPosition, self.board, self.lightPieces, self.darkPieces):
				return True
		return False
		
	def getPositionForPiece(self,piece):
		for row in range(0,len(self.board)):
			if piece in self.board[row]:
				col = self.board[row].index(piece)
				break
		return (row, col)