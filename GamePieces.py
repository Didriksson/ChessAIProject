import pygame
import RuleController


class GamePieces(object):

	def __init__(self, image, position, color):
		self.image = image
		self.position = position
		self.color = color

class Empty(GamePieces):
		def __init__(self):
			GamePieces.__init__(self, '',0,"EMPTY")

		
class Knight(GamePieces):
	def __init__(self, image, position, color):
		GamePieces.__init__(self,image, position, color)
		self.pieceScore = 320
		self.pieceTable = [
		[-50,-40,-30,-30,-30,-30,-40,-50],
		[-40,-20,  0,  0,  0,  0,-20,-40],
		[-30, 0, 10, 15, 15, 10, 0, -30],
		[-30, 5, 15, 20, 20, 15, 5,-30],
		[-30, 0, 15, 20, 20, 15, 0,-30],
		[-30, 5, 10, 15, 15, 10,  5,-30],
		[-40,-20, 0, 5, 5, 0,-20,-40],
		[-50,-40,-30,-30,-30,-30,-40,-50]
		]
class King(GamePieces):
	def __init__(self, image, position, color):
		GamePieces.__init__(self,image, position, color)
		self.pieceScore = 20000
		self.pieceTable = [
		[-30,-40,-40,-50,-50,-40,-40,-30],
		[-30,-40,-40,-50,-50,-40,-40,-30],
		[-30,-40,-40,-50,-50,-40,-40,-30],
		[-30,-40,-40,-50,-50,-40,-40,-30],
		[-20,-30,-30,-40,-40,-30,-30,-20],
		[-10,-20,-20,-20,-20,-20,-20,-10],
		[20, 20,  0,  0,  0,  0, 20, 20],
		[20, 30, 10,  0,  0, 10, 30, 20]
		]
class Rook(GamePieces):
	def __init__(self, image, position, color):
		GamePieces.__init__(self,image, position, color)
		self.pieceScore = 500
		self.pieceTable = [
		 [0,  0,  0,  0,  0,  0,  0,  0],
		 [5, 10, 10, 10, 10, 10, 10,  5],
		 [-5,  0,  0,  0,  0,  0,  0, -5],
		 [-5,  0,  0,  0,  0,  0,  0, -5],
		 [-5,  0,  0,  0,  0,  0,  0, -5],
		 [-5,  0,  0,  0,  0,  0,  0, -5],
		 [-5,  0,  0,  0,  0,  0,  0, -5],
		 [0,  0,  0,  5,  5,  0,  0,  0]
		]
class Queen(GamePieces):
	def __init__(self, image, position, color):
		GamePieces.__init__(self,image, position, color)
		self.pieceScore = 900		
		self.pieceTable = [
		[-20,-10,-10, -5, -5,-10,-10,-20],
		[-10,  0,  0,  0,  0,  0,  0,-10],
		[-10,  0,  5,  5,  5,  5,  0,-10],
		[-5,  0,  5,  5,  5,  5,  0, -5],
		[0,  0,  5,  5,  5,  5,  0, -5],
		[-10,  5,  5,  5,  5,  5,  0,-10],
		[-10,  0,  5,  0,  0,  0,  0,-10],
		[-20,-10,-10, -5, -5,-10,-10,-20],
		]

class Pawn(GamePieces):
	def __init__(self, image, position, color):
		GamePieces.__init__(self,image, position, color)
		self.pieceScore = 100
		self.pieceTable = [
		[0,  0,  0,  0,  0,  0,  0,  0],
		[50, 50, 50, 50, 50, 50, 50, 50],
		[10, 10, 20, 30, 30, 20, 10, 10],
		[5,  5, 10, 25, 25, 10,  5,  5,],
		[0,  0,  0, 20, 20,  0,  0,  0],
		[5, -5,-10,  0,  0,-10, -5,  5],
		[5, 10, 10,-20,-20, 10, 10,  5],
		[0,  0,  0,  0,  0,  0,  0,  0],
		]
class Bishop(GamePieces):
	def __init__(self, image, position, color):
		GamePieces.__init__(self,image, position, color)
		self.pieceScore = 330
		self.pieceTable = [
		[-20,-10,-10,-10,-10,-10,-10,-20],
		[-10,  0,  0,  0,  0,  0,  0,-10],
		[-10,  0,  5, 10, 10,  5,  0,-10],
		[-10,  5,  5, 10, 10,  5,  5,-10],
		[-10,  0, 10, 10, 10, 10,  0,-10],
		[-10, 10, 10, 10, 10, 10, 10,-10],
		[-10,  5,  0,  0,  0,  0,  5,-10],
		[-20,-10,-10,-10,-10,-10,-10,-20],
		]