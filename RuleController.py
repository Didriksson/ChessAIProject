import RulesPieces
import copy
import GamePieces

class RuleController():
	
	def presentMove(self,board,move):
		sourcePiece = board.board[move.source[0]][move.source[1]]
		destinationPiece = board.board[move.destination[0]][move.destination[1]]
		if sourcePiece == 'EMPTY':
			return False

		if not sourcePiece.color == destinationPiece.color:
			nameOfPiece = type(sourcePiece).__name__
			moveOkay = getattr(RulesPieces, nameOfPiece.lower())
			if moveOkay(move, board.board):
				return True
		else:
			return False
			
	def makeMove(self, board, move, realMove):
		print board
		newBoard = board.copyBoard()
		sourcePiece = newBoard.board[move.source[0]][move.source[1]]
		destinationPiece = newBoard.board[move.destination[0]][move.destination[1]]
		if destinationPiece is GamePieces.King:
			newBoard.winner = newBoard.currentPlayer
		newBoard.board[move.destination[0]][move.destination[1]] = newBoard.board[move.source[0]][move.source[1]]
		newBoard.board[move.source[0]][move.source[1]] = GamePieces.Empty()
		newBoard.nextPlayer()
		return newBoard

	def isChess(self,board,currentPlayer):
		if currentPlayer == board.lightPieces:
			kingsPosition = self.getPositionForPiece(board,GamePieces.King,'dark')
		else:
			kingsPosition = self.getPositionForPiece(board,GamePieces.King,'light')
			
		for piece in currentPlayer.values():
			nameOfPiece = type(piece).__name__
			moveOkay = getattr(RulesPieces, nameOfPiece.lower())
			source = self.getPositionForPiece(board,piece)
			if moveOkay(source, kingsPosition, board):
				return True
		return False
	
	def getPositionForPiece(self,board,piece, color):
		for row in range(len(board)):
			if piece is board[row] and piece.color == color:
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