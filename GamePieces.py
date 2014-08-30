import pygame

class GamePieces(object):
	def __init__(self, image, position):
		self.image = image
		self.position = position
		
		
		
class Knight(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
	def pieceSpecificMove(self,source, destination, board, lightPieces, darkPieces):
		#Light!

		deltaY = (source[0] - destination[0])
		deltaX = (source[1] - destination[1])
		if abs(deltaX) == 2 and abs(deltaY) == 1 or abs(deltaX) == 1 and abs(deltaY) == 2:
			return True
		else:
			return False

		
class Rook(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
	def pieceSpecificMove(self,source, destination):
		return True
		
class King(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)		
	def pieceSpecificMove(self,source, destination, board, lightPieces, darkPieces):
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
		#Light!
		if board[source[0]][source[1]] in lightPieces.values():
			#Destination empty
			if board[destination[0]][destination[1]] == "EMPTY":
				if (source[0] - destination[0]) == 1:
					if (source[1] - destination[1] != 0):
						return False
					return True
				elif (source[0] - destination[0]) == 2 and source[0] == 6:
					if (source[1] - destination[1] != 0):
						return False
					return True
			#Destination occupado
			else:
				print "Indeedeo"
				if abs((source[1] - destination[1])) == 1:
						if(board[destination[0]][destination[1]] in darkPieces.values()):
							return True
						else:
							return False
		#Dark!
		elif board[source[0]][source[1]] in darkPieces.values():
				#Destination empty
				if board[destination[0]][destination[1]] == "EMPTY":
					if (source[0] - destination[0]) == -1:
						if (source[1] - destination[1] != 0):
							return False
						return True
					elif (source[0] - destination[0]) == -2 and source[0] == 1:
						if (source[1] - destination[1] != 0):
							return False
						return True
				#Destination occupado
				else:
					if abs((source[1] - destination[1])) == 1:
							if(board[destination[0]][destination[1]] in lightPieces.values()):
								return True
							else:
								return False
			
		else:
			return False

class Bishop(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
	def pieceSpecificMove(self,source, destination):
		return True
		
