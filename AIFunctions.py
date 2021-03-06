import pygame
import RulesPieces
import RuleController
import GamePieces
import Move

class AIFunctions():
	
	def __init__(self):
		self.ruleController = RuleController.RuleController()
	def evalutate(self, board):
		whitePieces = self.getPiecesOnBoardForColor(board, 'white')
		darkPieces = self.getPiecesOnBoardForColor(board, 'black')	
		whiteMaterial = 0
		darkMaterial = 0
		for piece in whitePieces:
			whiteMaterial = whiteMaterial + self.evaluteScoreForPiece(piece, whitePieces[piece])
		for piece in darkPieces:
			darkMaterial = darkMaterial + self.evaluteScoreForPiece(piece, darkPieces[piece])
		materialValue = (whiteMaterial - darkMaterial)
		doubledPawnsValue = (self.getDoubledPawns(whitePieces) - self.getDoubledPawns(darkPieces))
		backwardPawnsValue = (self.getBackwardPawns(whitePieces)-self.getBackwardPawns(darkPieces))
		isolatedPawnsValue =  (self.getIsolatedPawns(whitePieces, board)-self.getIsolatedPawns(darkPieces, board))
		mobilityValue =  len(self.getAllMovesForPieces(board,whitePieces)) - len(self.getAllMovesForPieces(board,darkPieces))
	
		return materialValue - 50 * (doubledPawnsValue + backwardPawnsValue + isolatedPawnsValue) + 10 * (mobilityValue) 
		
	def maxIterate(self, board, player, depth, maxDepth):
		if depth == maxDepth:
			return self.evalutate(board), None
		
		if player == 'white':
			bestScore = -99999
		else:
			bestScore = 99999
			
		bestMove = None
		
		moves = self.getAllMovesForPieces(board,self.getPiecesOnBoardForColor(board, player))
		for move in moves:
			boardAfterMove = self.ruleController.makeMove(board, move, False)
			score = self.maxIterate(boardAfterMove,player,depth + 1, maxDepth)[0]
			if depth % 2 == 1:
				score = -score
		
			if score > bestScore:
				bestScore = score
				bestMove = move
		
		return  bestScore, bestMove
	
	def max(self, board):
		score, move = self.maxIterate(board, board.currentPlayer, 0, 1)
		return move
				
	def getAllMovesForPieces(self,board,pieces):
		moves = []
		for piece in pieces:
			nameOfPiece = type(piece).__name__
			moveOkay = getattr(RulesPieces, nameOfPiece.lower())
			source = self.getPositionForPiece(piece, board)
			for row in range(8):
				for col in range(8):
					destination = (row,col)
					move = Move.Move(source, destination)
					if moveOkay(move, board.board):
						moves.append(move)
		return moves
		
	def evaluteScoreForPiece(self, piece, position):
		score = piece.pieceScore
		score = score + piece.pieceTable[position[0]][position[1]]
		return score
		

	def getPositionForPiece(self,piece, board):
		for row in range(0,len(board.board)):
			if piece in board.board[row]:
				col = board.board[row].index(piece)
				break
		return (row, col)
		
	def getPiecesOnBoardForColor(self, board, color):
		currentPieces = {}
		for row in range(8):
			for col in range(8):
				if board.board[row][col] != 'EMPTY':
					if board.board[row][col].color == color:
						currentPieces[board.board[row][col]] = (row,col)
		return currentPieces
		
	def getDoubledPawns(self, pieces):
		doubled = 0
		pawns = self.getAllPawns(pieces)
		for pawn in pawns:
			for otherPawn in pawns:
				if pieces[pawn][1] == pieces[otherPawn][1] and paw is not otherPawn:
					doubled = doubled +1
		return doubled
		
	def getBackwardPawns(self,pieces):
		pawns = self.getAllPawns(pieces)
		return 0
	def getIsolatedPawns(self, pieces, board):
		pawns = self.getAllPawns(pieces)
		isolated = 0
		for pawn in pawns:
			col = pieces[pawn][1] - 1
			col2 = col1 + 2
			if col < 0:
				col = col2
			for otherPawn in pawns:
				if pieces[otherPawn][1] == col or pieces[otherPawn][1] == col2:
					isolated = isolated + 1
		return isolated
					
	def getAllPawns(self, pieces):
		pawns = []
		for piece in pieces:
			if piece is GamePieces.Pawn:
				pawns.append(piece)
		return pawns