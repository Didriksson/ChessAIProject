import pygame
import RulesPieces
class AIFunctions():
	def __init__(self,board, darkPieces, lightPieces):
		self.board = board
		self.lightPieces = lightPieces
		self.darkPieces = darkPieces

	def getAllMovesForPieces(self,pieces):
		moves = []
		for piece in pieces.values():
			nameOfPiece = type(piece).__name__
			moveOkay = getattr(RulesPieces, nameOfPiece.lower())
			source = self.getPositionForPiece(piece)
			for row in range(8):
				for col in range(8):
					destination = (row,col)
					if moveOkay(source, destination, self.board, self.lightPieces, self.darkPieces):
						moves.append((piece,source, destination))
		return moves
			

			
	def getPositionForPiece(self,piece):
		for row in range(0,len(self.board)):
			if piece in self.board[row]:
				col = self.board[row].index(piece)
				break
		return (row, col)