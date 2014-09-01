import pygame
import RuleController

class GamePieces(object):
	def __init__(self, image, position):
		self.image = image
		self.position = position
		
class Knight(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
	def pieceSpecificMove(self,source, destination, board, lightPieces, darkPieces):
		deltaY = (source[0] - destination[0])
		deltaX = (source[1] - destination[1])
		if abs(deltaX) == 2 and abs(deltaY) == 1 or abs(deltaX) == 1 and abs(deltaY) == 2:
			return True
		else:
			return False
		
class King(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
	def pieceSpecificMove(self,source, destination, board, lightPieces, darkPieces):
		return True

		
class Rook(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
	def pieceSpecificMove(self,source, destination, board, lightPieces, darkPieces):
		deltaY = (source[0] - destination[0])
		deltaX = (source[1] - destination[1])
		
		#Going wide!
		if abs(deltaX) > 0 and abs(deltaY) == 0:
			#Leftie!
			if(deltaX < 0):
				self.deltaPositions = range(source[1]+1, destination[1])
			#Rightie!
			else:
				self.deltaPositions = range(destination[1]+1, source[1])
			
			for index in self.deltaPositions:
				if board[source[0]][index] != 'EMPTY':
					return False
			return True
			
		#Going high!
		elif abs(deltaX) == 0 and abs(deltaY) > 0:
			#Upsie!
			print (destination[0],destination[1])
			if(deltaY < 0):
				self.deltaPositions = range(source[0]+1, destination[0])
			#Downie!
			else:
				self.deltaPositions = range(destination[0]+1, source[0])
			
			print self.deltaPositions
			for index in self.deltaPositions:
				print board[index][source[1]]
				if board[index][source[1]] != 'EMPTY':
					return False
			return True
		
		else:
			return False


class Queen(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)	
	def pieceSpecificMove(self,source, destination):
		return True

class Pawn(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)	
	def pieceSpecificMove(self,source, destination, board, lightPieces, darkPieces):
		deltaY = source[0] - destination[0]
		deltaX = source[1] - destination[1]
		#Light!
		if board[source[0]][source[1]] in lightPieces.values():
			#Moves up or down on the board.
			if (deltaY == 2 and source[0] == 6) or (deltaX == 0 and deltaY == 1):
				if board[destination[0]][destination[1]] == "EMPTY" and deltaX == 0:
					return True
				else:
					return False
			#Take another.
			else:
				print "Indeedeo"
				if deltaY == 1 and (abs(deltaX) == 1):
						if(board[destination[0]][destination[1]] in darkPieces.values()):
							return True
						else:
							return False
		#Dark!
		if board[source[0]][source[1]] in darkPieces.values():
			#Moves up or down on the board.
			if (deltaY == -2 and source[0] == 1) or (deltaX == 0 and deltaY == -1):
				if board[destination[0]][destination[1]] == "EMPTY" and deltaX == 0:
					return True
				else:
					return False
			#Take another.
			else:
				print "Indeedeo"
				if deltaY == -1 and (abs(deltaX) == 1):
						if(board[destination[0]][destination[1]] in lightPieces.values()):
							return True
						else:
							return False				
		else:
			return False

class Bishop(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
	def pieceSpecificMove(self,source, destination, board, lightPieces, darkPieces):
		deltaY = destination[0]-source[0]
		deltaX = destination[1]-source[1]
		
		if (deltaX !=0 and deltaY !=0) and abs(deltaX/deltaY) == 1:
			if(deltaY < 0):
				self.deltaPositions = range(source[0], destination[0])
				self.xModifier = 1
			else:
				self.deltaPositions = range(destination[0], destination[0])
				self.xModifier = -1
			for index in self.deltaPositions:
				if board[index][source[1] + self.xModifier] != 'EMPTY':
					if not board[source[0]][source[1]]:
						return False
			return True
		else:
			return False