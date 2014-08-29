import pygame

class GamePieces(object):
	def __init__(self, image, position):
		self.image = image
		self.position = position
		
		
		
class Knight(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
	def pieceSpecificMove(self,source, destination):
		return True

		
class Rook(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
	def pieceSpecificMove(self,source, destination):
		return True
		
class King(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)		
	def pieceSpecificMove(self,source, destination):
		return True

class Queen(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)		
	def pieceSpecificMove(self,source, destination):
		return True

class Pawn(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)	
	def pieceSpecificMove(self,source, destination, board, lightPieces, darkPieces):
		if board[destination[0]][destination[1]] != 'EMPTY':
			return False
			
		if board[source[0]][source[1]] in lightPieces.values():
			if (source[0] - destination[0]) == 1:
				return True
			elif (source[0] - destination[0]) == 2 and source[0] == 6:
				return True
		elif board[source[0]][source[1]] in darkPieces.values():
			if (source[0] - destination[0]) == -1:
				return True
			elif (source[0] - destination[0]) == -2 and source[0] == 1:
				return True

		else:
			return False

class Bishop(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
	def pieceSpecificMove(self,source, destination):
		return True
		
