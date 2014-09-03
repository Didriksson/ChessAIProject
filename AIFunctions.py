import pygame
import RulesPieces
import RuleController

class AIFunctions():
	
	def __init__(self,lightPieces, darkPieces):
		self.lightPieces = lightPieces
		self.darkPieces = darkPieces
		self.ruleController = RuleController.RuleController(self.lightPieces, self.darkPieces)
	def evalutate(self, board):
		whitePieces = self.getWhitePiecesOnBoard(board)
		darkPieces = self.getDarkPiecesOnBoard(board)	
		whiteMaterial = 0
		darkMaterial = 0
		for piece in whitePieces:
			whiteMaterial = whiteMaterial + self.evaluteScoreForPiece(piece, whitePieces[piece])
		for piece in darkPieces:
			darkMaterial = darkMaterial + self.evaluteScoreForPiece(piece, darkPieces[piece])
		
		return whiteMaterial - darkMaterial
		
		
	def max(self, board):
		moves = self.getAllMovesForPieces(board,self.getWhitePiecesOnBoard(board))
		bestScore = -9999
		bestMove = None
		for move in moves:
			moveAfterBoard = self.ruleController.makeMove(board, move[1], move[2], False)
			evalutedBoard = self.evalutate(moveAfterBoard)
			if  evalutedBoard > bestScore:
				bestScore = evalutedBoard
				bestMove = move
		return self.ruleController.makeMove(board, bestMove[1], bestMove[2], True)

			
			
	def getAllMovesForPieces(self,board,pieces):
		moves = []
		for piece in pieces:
			nameOfPiece = type(piece).__name__
			moveOkay = getattr(RulesPieces, nameOfPiece.lower())
			source = self.getPositionForPiece(piece, board)
			for row in range(8):
				for col in range(8):
					destination = (row,col)
					if moveOkay(source, destination, board):
						moves.append((piece,source, destination))
		return moves
		
	def evaluteScoreForPiece(self, piece, position):
		score = piece.pieceScore
		score = score + piece.pieceTable[position[0]][position[1]]
		return score
		

	def getPositionForPiece(self,piece, board):
		for row in range(0,len(board)):
			if piece in board[row]:
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