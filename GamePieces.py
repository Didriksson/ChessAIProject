import pygame
import RuleController

class GamePieces(object):
	def __init__(self, image, position):
		self.image = image
		self.position = position
		
class Knight(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
		
class King(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
		
class Rook(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)

class Queen(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)	


class Pawn(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)	

class Bishop(GamePieces):
	def __init__(self, image, position):
		GamePieces.__init__(self,image, position)
