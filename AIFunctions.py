import pygame
import RulesPieces
import RuleController
import GamePieces
import Move

class AIFunctions():
	
	
	def __init__(self):
		self.ruleController = RuleController.RuleController()
		self.gamePieceInformation = {
			'Pawn' : GamePieces.Pawn(),
			'Rook' : GamePieces.Rook(),
			'Bishop' : GamePieces.Pawn(),
			'Queen' : GamePieces.Pawn(),
			'King' : GamePieces.Pawn(),
			'Knight' : GamePieces.Pawn()	
		}

	def evalutate(self, board):
		whitePieces = self.getPiecesOnBoardForColor(board, 'White')
		blackPieces = self.getPiecesOnBoardForColor(board, 'Black')
		whiteMaterial = 0
		blackMaterial = 0
		for piece in whitePieces:
			whiteMaterial = whiteMaterial + self.evaluteScoreForPiece(piece[0], piece[1])
		for piece in blackPieces:
			blackMaterial = blackMaterial + self.evaluteScoreForPiece(piece[0], piece[1])
		materialValue = (whiteMaterial - blackMaterial)

		return materialValue
		
	def negaMax(self, board, depth):
		if depth == 0:
			return self.evalutate(board)
		
		bestscore = -9999999
		moves = self.getAllMovesForPieces(board,self.getPiecesOnBoardForColor(board, board.currentPlayer))

		for move in moves:
			boardAfterMove = self.ruleController.makeMove(board, move, False)
			score = - self.negaMax(boardAfterMove,depth - 1)
			bestscore = max(bestscore,score)
		return bestscore

	def max(self, board):
		DEPTH = 2

		bestscore = -9999999
		bestmove = None
		moves = self.getAllMovesForPieces(board,self.getPiecesOnBoardForColor(board, board.currentPlayer))
		for move in moves:
			boardAfterMove = self.ruleController.makeMove(board, move, False)
			score = -self.negaMax(boardAfterMove,DEPTH -1)
			if score > bestscore:
				bestscore = score
				bestmove = move
		return bestmove
				
	def getAllMovesForPieces(self,board,pieces):
		moves = []
		for piece in pieces:
			nameOfPiece = piece[0].replace('Black', '').replace('White','')
			moveOkay = getattr(RulesPieces, nameOfPiece.lower())
			source = piece[1]
			for row in range(8):
				for col in range(8):
					destination = (row,col)
					move = Move.Move(source, destination)
					if moveOkay(move, board.board):
						moves.append(move)
		return moves
		
	def evaluteScoreForPiece(self, piece, position):
		nameOfPiece = piece.replace('Black', '').replace('White','')
		score = self.gamePieceInformation[nameOfPiece].pieceScore
	#	score = score + self.gamePieceInformation[nameOfPiece].pieceTable[position[0]][position[1]]
		return score
		

	def getPositionForPiece(self,piece, board):
		for row in range(0,len(board.board)):
			if piece in board.board[row]:
				col = board.board[row].index(piece)
				break
		return (row, col)
		
	def getPiecesOnBoardForColor(self, board, color):
		currentPieces = []
		for row in range(8):
			for col in range(8):
				if board.board[row][col] != '':
					if color in board.board[row][col]:
						currentPieces.append((board.board[row][col],(row,col)))
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