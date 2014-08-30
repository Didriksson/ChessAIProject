
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
			if sourcePiece.pieceSpecificMove(source, destination, self.board, self.lightPieces, self.darkPieces):
				self.board[destination[0]][destination[1]] = self.board[source[0]][source[1]]
				self.board[source[0]][source[1]].position = destination
				self.board[source[0]][source[1]] = "EMPTY"
				return True
		else:
			return False